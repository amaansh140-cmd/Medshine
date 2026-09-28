const API_URL = 'http://localhost:3000/api';

document.addEventListener('DOMContentLoaded', async () => {
    const blogContainer = document.getElementById('blog-container');
    if (!blogContainer) return;

    try {
        const response = await fetch(`${API_URL}/blogs`);
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Failed to fetch blogs');
        }

        if (data.length === 0) {
            blogContainer.innerHTML = '<div class="col-span-full text-center text-inkmute py-10">No blog posts found yet. Add some in the admin panel!</div>';
            return;
        }

        let html = '';
        data.forEach((post) => {
            // Format date if it exists
            let dateStr = "Recently";
            if (post.created_at) {
                const date = new Date(post.created_at);
                dateStr = date.toLocaleDateString('en-US', { month: 'long', year: 'numeric' });
            }

            html += `
            <article class="flex flex-col gap-6 group reveal-anim">
                <div class="aspect-video w-full rounded-[24px] overflow-hidden border border-ink/10 bg-ink/5">
                    <img src="${post.image}" alt="${post.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 reveal-fade" onerror="this.src='/src/assets/treatment_facial.jpg'">
                </div>
                <div class="flex flex-col gap-3">
                    <div class="flex items-center gap-4 text-xs font-semibold text-inkmute">
                        <span class="uppercase tracking-widest text-ink">${post.category || 'General'}</span>
                        <span>•</span>
                        <span>${post.read_time || '5 Min Read'}</span>
                        <span>•</span>
                        <span>${dateStr}</span>
                    </div>
                    <h3 class="font-serif text-3xl font-semibold text-ink group-hover:text-inkmute transition-colors leading-tight">
                        ${post.title}
                    </h3>
                    <p class="text-inkmute font-light leading-relaxed line-clamp-3">
                        ${post.content.substring(0, 150)}...
                    </p>
                </div>
            </article>
            `;
        });

        blogContainer.innerHTML = html;
        
    } catch (error) {
        console.error("Error fetching blogs:", error);
        blogContainer.innerHTML = '<div class="col-span-full text-center text-red-500 py-10">Error loading blogs. Ensure the backend server is running.</div>';
    }
});
