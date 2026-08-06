import os
import shutil

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace the old footer classes with the new glassmorphism classes
        # Old: <footer class="bg-ink text-cream relative overflow-hidden mt-20">
        # New: <footer class="bg-ink/90 backdrop-blur-2xl border border-cream/20 shadow-2xl text-cream relative overflow-hidden mt-20 mx-4 md:mx-8 mb-6 rounded-[2.5rem]">
        
        # We will also add a subtle background glow behind the footer so the glass effect is visible
        # We can wrap the footer in a div with a subtle gradient, but that's complex.
        # Instead, let's just make the footer float and be glassy. The content scrolling behind it (if any) or the cream body will show through slightly.
        # Let's use bg-ink/85 to make it translucent enough.
        
        old_footer_tag = '<footer class="bg-ink text-cream relative overflow-hidden mt-20">'
        new_footer_tag = '<footer class="bg-ink/85 backdrop-blur-3xl border border-cream/20 shadow-2xl text-cream relative overflow-hidden mt-20 mx-4 md:mx-8 mb-6 rounded-[2.5rem] ring-1 ring-cream/10">'
        
        if old_footer_tag in content:
            content = content.replace(old_footer_tag, new_footer_tag)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
                
            if os.path.exists(f'../Medshine/{filename}'):
                shutil.copy(filename, f'../Medshine/{filename}')

print("Glassmorphism footer applied!")
