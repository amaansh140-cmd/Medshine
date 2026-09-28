require('dotenv').config();
const express = require('express');
const cors = require('cors');
const mysql = require('mysql2/promise');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 3000;
const JWT_SECRET = process.env.JWT_SECRET || 'your_super_secret_jwt_key_here';

// MySQL Connection Pool
const pool = mysql.createPool({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0
});

// Initialize Database Tables
async function initDB() {
    try {
        const connection = await pool.getConnection();
        
        // Create users table
        await connection.query(`
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        `);

        // Create blogs table
        await connection.query(`
            CREATE TABLE IF NOT EXISTS blogs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                category VARCHAR(100),
                read_time VARCHAR(50),
                image VARCHAR(500),
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
        `);

        // Check if admin user exists, if not, create default
        const [users] = await connection.query('SELECT * FROM users');
        if (users.length === 0) {
            const defaultPassword = await bcrypt.hash('admin123', 10);
            await connection.query('INSERT INTO users (email, password) VALUES (?, ?)', ['admin@medshineclinic.com', defaultPassword]);
            console.log('Created default admin user: admin@medshineclinic.com / admin123');
            console.log('PLEASE CHANGE THIS PASSWORD IMMEDIATELY!');
        }

        connection.release();
        console.log('Database initialized successfully');
    } catch (error) {
        console.error('Error initializing database. Check your .env credentials!', error.message);
    }
}
initDB();

// Middleware to protect routes
const authenticateToken = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];
    
    if (!token) return res.status(401).json({ error: 'Access denied' });

    jwt.verify(token, JWT_SECRET, (err, user) => {
        if (err) return res.status(403).json({ error: 'Invalid token' });
        req.user = user;
        next();
    });
};

// --- ROUTES ---

// 1. Admin Login
app.post('/api/login', async (req, res) => {
    try {
        const { email, password } = req.body;
        const [rows] = await pool.query('SELECT * FROM users WHERE email = ?', [email]);
        
        if (rows.length === 0) return res.status(401).json({ error: 'Invalid credentials' });
        
        const user = rows[0];
        const validPassword = await bcrypt.compare(password, user.password);
        
        if (!validPassword) return res.status(401).json({ error: 'Invalid credentials' });
        
        const token = jwt.sign({ id: user.id, email: user.email }, JWT_SECRET, { expiresIn: '24h' });
        res.json({ token });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// 2. Get All Blogs
app.get('/api/blogs', async (req, res) => {
    try {
        const [rows] = await pool.query('SELECT * FROM blogs ORDER BY created_at DESC');
        res.json(rows);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// 3. Create Blog
app.post('/api/blogs', authenticateToken, async (req, res) => {
    try {
        const { title, category, read_time, image, content } = req.body;
        const [result] = await pool.query(
            'INSERT INTO blogs (title, category, read_time, image, content) VALUES (?, ?, ?, ?, ?)',
            [title, category, read_time, image, content]
        );
        res.status(201).json({ id: result.insertId, message: 'Blog created successfully' });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// 4. Update Blog
app.put('/api/blogs/:id', authenticateToken, async (req, res) => {
    try {
        const { id } = req.params;
        const { title, category, read_time, image, content } = req.body;
        await pool.query(
            'UPDATE blogs SET title = ?, category = ?, read_time = ?, image = ?, content = ? WHERE id = ?',
            [title, category, read_time, image, content, id]
        );
        res.json({ message: 'Blog updated successfully' });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// 5. Delete Blog
app.delete('/api/blogs/:id', authenticateToken, async (req, res) => {
    try {
        const { id } = req.params;
        await pool.query('DELETE FROM blogs WHERE id = ?', [id]);
        res.json({ message: 'Blog deleted successfully' });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start Server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
