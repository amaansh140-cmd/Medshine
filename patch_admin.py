with open('admin.html', 'r') as f:
    content = f.read()

treatments_html = """
            <!-- View: Treatments -->
            <div id="view-treatments" class="p-8 view-section hidden h-full flex flex-col">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 flex-1 min-h-0">
                    <!-- Treatments List -->
                    <div class="md:col-span-1 bg-white rounded-2xl shadow-sm border border-ink/10 p-6 flex flex-col min-h-0">
                        <div class="flex justify-between items-center mb-4 shrink-0">
                            <h2 class="text-lg font-semibold">All Treatments</h2>
                            <button id="new-treatment-btn" class="text-sm bg-ink/10 text-ink px-3 py-1 rounded hover:bg-ink/20 transition-colors">+ New</button>
                        </div>
                        <div id="treatments-list" class="flex-1 overflow-y-auto space-y-2 pr-2">
                            <div class="text-inkmute text-sm text-center py-4">Loading treatments...</div>
                        </div>
                    </div>

                    <!-- Treatment Editor -->
                    <div class="md:col-span-2 bg-white rounded-2xl shadow-sm border border-ink/10 p-6 flex flex-col min-h-0">
                        <h2 id="treatment-editor-title" class="text-lg font-semibold mb-4 shrink-0">Create New Treatment</h2>
                        <form id="treatment-form" class="flex-1 flex flex-col min-h-0">
                            <input type="hidden" id="treatment-id">
                            <div class="space-y-4 flex-1 overflow-y-auto pr-2 pb-4">
                                <div class="grid grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-sm font-medium mb-1">Title</label>
                                        <input type="text" id="treatment-title" required class="w-full px-4 py-2 rounded-lg border border-ink/20 focus:outline-none focus:border-ink bg-transparent">
                                    </div>
                                    <div>
                                        <label class="block text-sm font-medium mb-1">Category</label>
                                        <select id="treatment-category" required class="w-full px-4 py-2 rounded-lg border border-ink/20 focus:outline-none focus:border-ink bg-transparent">
                                            <option value="hair">Hair</option>
                                            <option value="skin">Skin</option>
                                            <option value="laser">Laser</option>
                                            <option value="medical">Medical</option>
                                            <option value="injectables">Injectables</option>
                                            <option value="non-surgical">Non-Surgical</option>
                                            <option value="regenerative">Regenerative</option>
                                            <option value="bridal">Bridal</option>
                                        </select>
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-sm font-medium mb-1">Image URL</label>
                                    <div class="flex gap-2">
                                        <input type="text" id="treatment-image" placeholder="/assets/image.jpg" class="flex-1 px-4 py-2 rounded-lg border border-ink/20 focus:outline-none focus:border-ink bg-transparent">
                                        <button type="button" onclick="window.triggerUpload('treatment-image')" class="px-4 py-2 bg-ink/10 text-ink rounded-lg font-medium hover:bg-ink/20 transition-colors">Upload</button>
                                    </div>
                                </div>
                                <div class="flex-1 flex flex-col min-h-[200px]">
                                    <label class="block text-sm font-medium mb-1">Description</label>
                                    <textarea id="treatment-description" required class="w-full flex-1 p-4 rounded-lg border border-ink/20 focus:outline-none focus:border-ink bg-transparent resize-none"></textarea>
                                </div>
                            </div>
                            <div class="flex justify-end gap-3 pt-4 border-t border-ink/10 shrink-0 mt-auto">
                                <button type="button" id="delete-treatment-btn" class="hidden px-4 py-2 rounded-lg border border-red-200 text-red-600 hover:bg-red-50 transition-colors font-medium">Delete</button>
                                <button type="submit" id="save-treatment-btn" class="bg-ink text-white px-6 py-2 rounded-lg hover:bg-inkmute transition-colors font-medium">Save Treatment</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
"""
content = content.replace('<!-- View: Blogs -->', treatments_html + '\n            <!-- View: Blogs -->')
with open('admin.html', 'w') as f:
    f.write(content)
