// Base URL for the Node.js API
const API_URL = 'http://localhost:3000/api';

// DOM Elements
const loginScreen = document.getElementById('login-screen');
const dashboardScreen = document.getElementById('dashboard-screen');
const loginForm = document.getElementById('login-form');
const loginError = document.getElementById('login-error');
const logoutBtn = document.getElementById('logout-btn');
const postsList = document.getElementById('posts-list');
const postForm = document.getElementById('post-form');
const newPostBtn = document.getElementById('new-post-btn');
const deleteBtn = document.getElementById('delete-btn');
const editorTitle = document.getElementById('editor-title');

let currentPosts = [];

// Check auth state on load
function checkAuth() {
    const token = localStorage.getItem('admin_token');
    if (token) {
        loginScreen.classList.add('hidden');
        dashboardScreen.classList.remove('hidden');
        dashboardScreen.classList.add('flex');
        loadPosts();
    } else {
        loginScreen.classList.remove('hidden');
        dashboardScreen.classList.add('hidden');
        dashboardScreen.classList.remove('flex');
    }
}
checkAuth();

// Login
loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
    try {
        const response = await fetch(`${API_URL}/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Login failed');
        }
        
        localStorage.setItem('admin_token', data.token);
        loginError.classList.add('hidden');
        checkAuth();
    } catch (error) {
        loginError.textContent = error.message;
        loginError.classList.remove('hidden');
    }
});

// Logout
logoutBtn.addEventListener('click', () => {
    localStorage.removeItem('admin_token');
    checkAuth();
});

// Helper for authenticated fetch
async function authFetch(url, options = {}) {
    const token = localStorage.getItem('admin_token');
    const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
        ...options.headers
    };
    const response = await fetch(url, { ...options, headers });
    
    if (response.status === 401 || response.status === 403) {
        localStorage.removeItem('admin_token');
        checkAuth();
        throw new Error('Session expired');
    }
    return response;
}

// Load Posts
async function loadPosts() {
    postsList.innerHTML = '<div class="text-center text-sm py-4">Loading...</div>';
    try {
        const response = await fetch(`${API_URL}/blogs`);
        const data = await response.json();
        
        if (!response.ok) throw new Error(data.error);
        
        currentPosts = data;
        renderPostList();
    } catch (error) {
        console.error("Error loading posts:", error);
        postsList.innerHTML = '<div class="text-red-500 text-sm py-4 text-center">Error loading posts</div>';
    }
}

function renderPostList() {
    if (currentPosts.length === 0) {
        postsList.innerHTML = '<div class="text-center text-sm py-4 text-inkmute">No posts found. Create one!</div>';
        return;
    }
    postsList.innerHTML = '';
    currentPosts.forEach(post => {
        const div = document.createElement('div');
        div.className = "p-3 rounded-lg border border-ink/10 hover:bg-ink/5 cursor-pointer transition-colors";
        div.innerHTML = `
            <div class="font-medium text-sm truncate">${post.title}</div>
            <div class="text-xs text-inkmute mt-1">${post.category} • ${post.read_time}</div>
        `;
        div.onclick = () => editPost(post);
        postsList.appendChild(div);
    });
}

// Prepare New Post
newPostBtn.addEventListener('click', () => {
    postForm.reset();
    document.getElementById('post-id').value = '';
    editorTitle.textContent = "Create New Post";
    deleteBtn.classList.add('hidden');
});

// Edit Post
function editPost(post) {
    document.getElementById('post-id').value = post.id;
    document.getElementById('post-title').value = post.title;
    document.getElementById('post-category').value = post.category || '';
    document.getElementById('post-readtime').value = post.read_time || '';
    document.getElementById('post-image').value = post.image || '';
    document.getElementById('post-content').value = post.content;
    editorTitle.textContent = "Edit Post";
    deleteBtn.classList.remove('hidden');
}

// Save/Update Post
postForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const submitBtn = document.getElementById('save-btn');
    submitBtn.textContent = "Saving...";
    submitBtn.disabled = true;

    const id = document.getElementById('post-id').value;
    const postData = {
        title: document.getElementById('post-title').value,
        category: document.getElementById('post-category').value,
        read_time: document.getElementById('post-readtime').value,
        image: document.getElementById('post-image').value,
        content: document.getElementById('post-content').value
    };

    try {
        let response;
        if (id) {
            // Update
            response = await authFetch(`${API_URL}/blogs/${id}`, {
                method: 'PUT',
                body: JSON.stringify(postData)
            });
        } else {
            // Create
            response = await authFetch(`${API_URL}/blogs`, {
                method: 'POST',
                body: JSON.stringify(postData)
            });
        }
        
        const data = await response.json();
        if (!response.ok) throw new Error(data.error);
        
        await loadPosts();
        newPostBtn.click(); // Reset form
        alert("Post saved successfully!");
    } catch (error) {
        console.error("Error saving post:", error);
        alert("Error saving post: " + error.message);
    } finally {
        submitBtn.textContent = "Publish Post";
        submitBtn.disabled = false;
    }
});

// Delete Post
deleteBtn.addEventListener('click', async () => {
    const id = document.getElementById('post-id').value;
    if (!id) return;
    
    if (confirm("Are you sure you want to delete this post? This cannot be undone.")) {
        deleteBtn.textContent = "Deleting...";
        deleteBtn.disabled = true;
        try {
            const response = await authFetch(`${API_URL}/blogs/${id}`, {
                method: 'DELETE'
            });
            
            const data = await response.json();
            if (!response.ok) throw new Error(data.error);
            
            await loadPosts();
            newPostBtn.click(); // Reset form
        } catch (error) {
            console.error("Error deleting post:", error);
            alert("Error deleting post: " + error.message);
        } finally {
            deleteBtn.textContent = "Delete";
            deleteBtn.disabled = false;
        }
    }
});
