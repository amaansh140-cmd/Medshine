with open('src/admin.js', 'r') as f:
    content = f.read()

# Replace direct injection with escaped value
import re

# We need to escape double quotes in content_value before using it in HTML
replacement = """
                const safeValue = (field.content_value || '').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
                if (field.content_type === 'textarea') {
                    inputHtml = `<textarea id="field_${field.section_key}" data-key="${field.section_key}" class="w-full min-h-[100px] p-3 rounded-lg border border-ink/20 focus:outline-none focus:border-ink bg-transparent">${safeValue}</textarea>`;
                } else if (field.content_type === 'image') {
                    inputHtml = `
                        <div class="flex gap-2">
                            <input type="text" id="field_${field.section_key}" data-key="${field.section_key}" value="${safeValue}" class="flex-1 px-4 py-2 rounded-lg border border-ink/20 focus:outline-none focus:border-ink bg-transparent">
                            <button type="button" onclick="triggerUpload('field_${field.section_key}')" class="px-4 py-2 bg-ink/10 text-ink rounded-lg font-medium hover:bg-ink/20 transition-colors">Upload</button>
                        </div>
                        ${field.content_value ? `<img src="${safeValue}" class="mt-2 h-20 rounded border border-ink/10 object-cover">` : ''}
                    `;
                } else {
                    inputHtml = `<input type="text" id="field_${field.section_key}" data-key="${field.section_key}" value="${safeValue}" class="w-full px-4 py-2 rounded-lg border border-ink/20 focus:outline-none focus:border-ink bg-transparent">`;
                }
"""

# Find the block to replace
start_idx = content.find("if (field.content_type === 'textarea') {")
end_idx = content.find("div.innerHTML = `", start_idx)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + replacement + content[end_idx:]
    with open('src/admin.js', 'w') as f:
        f.write(content)
    print("Fixed admin.js")
else:
    print("Could not find block to replace")
