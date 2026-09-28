with open('src/admin.js', 'r') as f:
    content = f.read()

treatments_js = """
    // ----------------------------------------------------
    // TREATMENTS
    // ----------------------------------------------------
    const treatmentsList = document.getElementById('treatments-list');
    const treatmentForm = document.getElementById('treatment-form');
    const newTreatmentBtn = document.getElementById('new-treatment-btn');
    const deleteTreatmentBtn = document.getElementById('delete-treatment-btn');
    const treatmentEditorTitle = document.getElementById('treatment-editor-title');
    let currentTreatments = [];

    async function loadTreatments() {
        if(!treatmentsList) return;
        try {
            const res = await authFetch(`${API_URL}/treatments.php`);
            currentTreatments = await res.json();
            
            if (currentTreatments.length === 0) {
                treatmentsList.innerHTML = '<div class="text-center text-sm py-4 text-inkmute">No treatments found.</div>';
                return;
            }
            
            treatmentsList.innerHTML = '';
            currentTreatments.forEach(t => {
                const div = document.createElement('div');
                div.className = "p-3 rounded-lg border border-ink/10 hover:bg-ink/5 cursor-pointer transition-colors";
                div.innerHTML = `
                    <div class="font-medium text-sm truncate">${t.title}</div>
                    <div class="text-xs text-inkmute mt-1 capitalize">${t.category}</div>
                `;
                div.onclick = () => editTreatment(t);
                treatmentsList.appendChild(div);
            });
        } catch (e) {
            treatmentsList.innerHTML = '<div class="text-red-500 text-sm py-4">Error loading treatments</div>';
        }
    }

    if(newTreatmentBtn) {
        newTreatmentBtn.addEventListener('click', () => {
            treatmentForm.reset();
            document.getElementById('treatment-id').value = '';
            treatmentEditorTitle.textContent = "Create New Treatment";
            deleteTreatmentBtn.classList.add('hidden');
        });
    }

    function editTreatment(t) {
        document.getElementById('treatment-id').value = t.id;
        document.getElementById('treatment-title').value = t.title;
        document.getElementById('treatment-category').value = t.category;
        document.getElementById('treatment-description').value = t.description;
        document.getElementById('treatment-image').value = t.image || '';
        treatmentEditorTitle.textContent = "Edit Treatment";
        deleteTreatmentBtn.classList.remove('hidden');
    }

    if(treatmentForm) {
        treatmentForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = document.getElementById('save-treatment-btn');
            btn.textContent = "Saving...";
            
            const id = document.getElementById('treatment-id').value;
            const data = {
                title: document.getElementById('treatment-title').value,
                category: document.getElementById('treatment-category').value,
                description: document.getElementById('treatment-description').value,
                image: document.getElementById('treatment-image').value,
            };

            try {
                let res;
                if (id) {
                    res = await authFetch(`${API_URL}/treatments.php?id=${id}`, { method: 'PUT', body: JSON.stringify(data) });
                } else {
                    res = await authFetch(`${API_URL}/treatments.php`, { method: 'POST', body: JSON.stringify(data) });
                }
                if (!res.ok) throw new Error('Error saving');
                await loadTreatments();
                newTreatmentBtn.click();
            } catch (err) {
                alert("Error saving treatment");
            } finally {
                btn.textContent = "Save Treatment";
            }
        });
    }

    if(deleteTreatmentBtn) {
        deleteTreatmentBtn.addEventListener('click', async () => {
            const id = document.getElementById('treatment-id').value;
            if(!id) return;
            if(confirm("Delete this treatment?")) {
                await authFetch(`${API_URL}/treatments.php?id=${id}`, { method: 'DELETE' });
                loadTreatments();
                newTreatmentBtn.click();
            }
        });
    }

"""

# Insert right after the blogs section
content = content.replace('// Start auth check', treatments_js + '\n    // Start auth check')

# Also modify loadView to load treatments
content = content.replace("if(viewName === 'pages') loadPages();", "if(viewName === 'pages') loadPages();\n            if(viewName === 'blogs') loadBlogs();\n            if(viewName === 'treatments') loadTreatments();")

with open('src/admin.js', 'w') as f:
    f.write(content)
