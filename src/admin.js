const API_URL = '/api';

// Wait for DOM to load before attaching events
document.addEventListener('DOMContentLoaded', () => {

    const loginScreen = document.getElementById('login-screen');
    const dashboardScreen = document.getElementById('dashboard-screen');
    const loginForm = document.getElementById('login-form');
    const loginError = document.getElementById('login-error');
    const logoutBtn = document.getElementById('logout-btn');

    // Navigation
    const navBtns = document.querySelectorAll('.nav-btn');
    const viewSections = document.querySelectorAll('.view-section');

    // Blogs Elements
    const postsList = document.getElementById('posts-list');
    const postForm = document.getElementById('post-form');
    const newPostBtn = document.getElementById('new-post-btn');
    const deleteBtn = document.getElementById('delete-btn');
    const editorTitle = document.getElementById('editor-title');
    let currentPosts = [];

    // Pages Elements
    const pagesList = document.getElementById('pages-list');
    const pageEditorContainer = document.getElementById('page-editor-container');
    const pageEditorTitle = document.getElementById('page-editor-title');
    const pageForm = document.getElementById('page-form');
    const pageFieldsContainer = document.getElementById('page-fields-container');
    
    // File Upload
    const fileUploadInput = document.getElementById('file-upload-input');
    let activeUploadTarget = null; // To know which input field gets the URL

    // ----------------------------------------------------
    // AUTHENTICATION
    // ----------------------------------------------------

    async function authFetch(url, options = {}) {
        options.credentials = 'include';
        const response = await fetch(url, options);
        if (response.status === 401 || response.status === 403) {
            loginScreen.classList.remove('hidden');
            dashboardScreen.classList.add('hidden');
            throw new Error('Session expired');
        }
        return response;
    }

    async function checkAuth() {
        try {
            await authFetch(`${API_URL}/check_auth.php`);
            loginScreen.classList.add('hidden');
            dashboardScreen.classList.remove('hidden');
            loadBlogs(); // Load initial data
            loadPages();
        } catch (e) {
            // Not authenticated, stay on login
        }
    }

    if(loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            try {
                const response = await fetch(`${API_URL}/login.php`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password }),
                    credentials: 'include'
                });
                const data = await response.json();
                if (!response.ok) throw new Error(data.error || 'Login failed');
                
                loginError.classList.add('hidden');
                checkAuth();
            } catch (error) {
                loginError.textContent = error.message;
                loginError.classList.remove('hidden');
            }
        });
    }

    if(logoutBtn) {
        logoutBtn.addEventListener('click', async () => {
            await fetch(`${API_URL}/logout.php`, { credentials: 'include' });
            location.reload();
        });
    }

    // ----------------------------------------------------
    // NAVIGATION
    // ----------------------------------------------------

    navBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Update Active State
            navBtns.forEach(b => {
                b.classList.remove('bg-ink/5', 'text-ink');
                b.classList.add('text-inkmute', 'hover:bg-ink/5');
            });
            btn.classList.add('bg-ink/5', 'text-ink');
            btn.classList.remove('text-inkmute');

            // Switch Views
            viewSections.forEach(sec => sec.classList.add('hidden'));
            document.getElementById(`view-${btn.dataset.view}`).classList.remove('hidden');
        });
    });

    // ----------------------------------------------------
    // PAGES CMS
    // ----------------------------------------------------

    async function loadPages() {
        try {
            const res = await authFetch(`${API_URL}/pages.php`);
            const pages = await res.json();
            
            pagesList.innerHTML = '';
            pages.forEach(page => {
                const btn = document.createElement('button');
                btn.className = 'w-full text-left px-4 py-3 rounded-lg border border-ink/10 hover:bg-ink/5 transition-colors font-medium flex justify-between items-center';
                btn.innerHTML = `<span>${page.name}</span> <span class="text-inkmute text-xs">Edit</span>`;
                btn.onclick = () => editPage(page.slug, page.name);
                pagesList.appendChild(btn);
            });
        } catch (e) {
            console.error(e);
        }
    }

    async function editPage(slug, name) {
        pageEditorTitle.textContent = `Editing: ${name}`;
        pageEditorContainer.classList.remove('hidden');
        document.getElementById('edit-page-slug').value = slug;
        pageFieldsContainer.innerHTML = '<div class="text-sm text-inkmute">Loading fields...</div>';

        try {
            const res = await authFetch(`${API_URL}/page_content.php?slug=${slug}&admin=true`);
            const fields = await res.json();
            
            pageFieldsContainer.innerHTML = '';
            
            if(fields.length === 0) {
                pageFieldsContainer.innerHTML = '<div class="text-sm text-inkmute">No editable fields found for this page.</div>';
                return;
            }

            fields.forEach(field => {
                const div = document.createElement('div');
                div.className = 'mb-4';
                
                let inputHtml = '';
                if (field.content_type === 'textarea') {
                    inputHtml = `<textarea id="field_${field.section_key}" data-key="${field.section_key}" class="w-full min-h-[100px] p-3 rounded-lg border border-ink/20 focus:outline-none focus:border-ink bg-transparent">${field.content_value || ''}</textarea>`;
                } else if (field.content_type === 'image') {
                    inputHtml = `
                        <div class="flex gap-2">
                            <input type="text" id="field_${field.section_key}" data-key="${field.section_key}" value="${field.content_value || ''}" class="flex-1 px-4 py-2 rounded-lg border border-ink/20 focus:outline-none focus:border-ink bg-transparent">
                            <button type="button" onclick="triggerUpload('field_${field.section_key}')" class="px-4 py-2 bg-ink/10 text-ink rounded-lg font-medium hover:bg-ink/20 transition-colors">Upload</button>
                        </div>
                        ${field.content_value ? `<img src="${field.content_value}" class="mt-2 h-20 rounded border border-ink/10 object-cover">` : ''}
                    `;
                } else {
                    inputHtml = `<input type="text" id="field_${field.section_key}" data-key="${field.section_key}" value="${field.content_value || ''}" class="w-full px-4 py-2 rounded-lg border border-ink/20 focus:outline-none focus:border-ink bg-transparent">`;
                }

                div.innerHTML = `
                    <label class="block text-sm font-medium mb-1">${field.label}</label>
                    ${inputHtml}
                `;
                pageFieldsContainer.appendChild(div);
            });
        } catch (e) {
            console.error(e);
            pageFieldsContainer.innerHTML = '<div class="text-red-500 text-sm">Failed to load fields.</div>';
        }
    }

    if(pageForm) {
        pageForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = document.getElementById('save-page-btn');
            btn.textContent = 'Saving...';
            btn.disabled = true;

            const slug = document.getElementById('edit-page-slug').value;
            const payload = {};
            
            // Gather all inputs with data-key
            const inputs = pageFieldsContainer.querySelectorAll('[data-key]');
            inputs.forEach(input => {
                payload[input.dataset.key] = input.value;
            });

            try {
                const res = await authFetch(`${API_URL}/page_content.php?slug=${slug}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                if(!res.ok) throw new Error('Failed to save');
                alert("Page saved successfully!");
                // Refresh the form to show updated images
                editPage(slug, pageEditorTitle.textContent.replace('Editing: ', ''));
            } catch (error) {
                alert("Error saving page");
            } finally {
                btn.textContent = 'Save Changes';
                btn.disabled = false;
            }
        });
    }

    // ----------------------------------------------------
    // BLOGS
    // ----------------------------------------------------

    async function loadBlogs() {
        if(!postsList) return;
        try {
            const res = await authFetch(`${API_URL}/blogs.php`);
            currentPosts = await res.json();
            
            if (currentPosts.length === 0) {
                postsList.innerHTML = '<div class="text-center text-sm py-4 text-inkmute">No posts found.</div>';
                return;
            }
            
            postsList.innerHTML = '';
            currentPosts.forEach(post => {
                const div = document.createElement('div');
                div.className = "p-3 rounded-lg border border-ink/10 hover:bg-ink/5 cursor-pointer transition-colors";
                div.innerHTML = `
                    <div class="font-medium text-sm truncate">${post.title}</div>
                    <div class="text-xs text-inkmute mt-1">${post.category}</div>
                `;
                div.onclick = () => editPost(post);
                postsList.appendChild(div);
            });
        } catch (e) {
            postsList.innerHTML = '<div class="text-red-500 text-sm py-4">Error loading posts</div>';
        }
    }

    if(newPostBtn) {
        newPostBtn.addEventListener('click', () => {
            postForm.reset();
            document.getElementById('post-id').value = '';
            editorTitle.textContent = "Create New Post";
            deleteBtn.classList.add('hidden');
        });
    }

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

    if(postForm) {
        postForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = document.getElementById('save-btn');
            btn.textContent = "Saving...";
            
            const id = document.getElementById('post-id').value;
            const data = {
                title: document.getElementById('post-title').value,
                category: document.getElementById('post-category').value,
                read_time: document.getElementById('post-readtime').value,
                image: document.getElementById('post-image').value,
                content: document.getElementById('post-content').value
            };

            try {
                let res;
                if (id) {
                    res = await authFetch(`${API_URL}/blog_single.php?id=${id}`, { method: 'PUT', body: JSON.stringify(data) });
                } else {
                    res = await authFetch(`${API_URL}/blogs.php`, { method: 'POST', body: JSON.stringify(data) });
                }
                if (!res.ok) throw new Error('Error saving');
                await loadBlogs();
                newPostBtn.click();
            } catch (err) {
                alert("Error saving blog");
            } finally {
                btn.textContent = "Publish Post";
            }
        });
    }

    if(deleteBtn) {
        deleteBtn.addEventListener('click', async () => {
            const id = document.getElementById('post-id').value;
            if(!id) return;
            if(confirm("Delete this post?")) {
                await authFetch(`${API_URL}/blog_single.php?id=${id}`, { method: 'DELETE' });
                loadBlogs();
                newPostBtn.click();
            }
        });
    }

    // ----------------------------------------------------
    // FILE UPLOAD SYSTEM
    // ----------------------------------------------------
    window.triggerUpload = function(targetInputId) {
        activeUploadTarget = targetInputId;
        fileUploadInput.click();
    };

    if(fileUploadInput) {
        fileUploadInput.addEventListener('change', async (e) => {
            const file = e.target.files[0];
            if(!file || !activeUploadTarget) return;

            // In blog editor, activeUploadTarget might be set by a button click we add
            // Wait, we need to bind the blog image upload button!
            
            const formData = new FormData();
            formData.append('file', file);

            try {
                const targetInput = document.getElementById(activeUploadTarget);
                targetInput.value = 'Uploading...';
                
                const res = await fetch(`${API_URL}/upload.php`, {
                    method: 'POST',
                    body: formData,
                    credentials: 'include'
                });
                const data = await res.json();
                if(!res.ok) throw new Error(data.error);
                
                targetInput.value = data.url;
            } catch (err) {
                alert(err.message || 'Upload failed');
                document.getElementById(activeUploadTarget).value = '';
            } finally {
                fileUploadInput.value = ''; // reset
            }
        });
    }

    // Bind Blog image upload button specifically
    const blogImageInput = document.getElementById('post-image');
    if (blogImageInput) {
        const uploadBtn = blogImageInput.nextElementSibling;
        if (uploadBtn && uploadBtn.tagName === 'BUTTON') {
            uploadBtn.onclick = () => window.triggerUpload('post-image');
        }
    }

    // Start auth check
    checkAuth();
});
