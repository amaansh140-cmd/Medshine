import glob
import re

html_files = glob.glob("*.html")

whatsapp_snippet = """
    <!-- Floating WhatsApp Button -->
    <a href="https://wa.me/" target="_blank" class="fixed bottom-6 right-6 z-[9999] bg-[#25D366] text-white p-4 rounded-full shadow-[0_4px_14px_0_rgba(37,211,102,0.39)] hover:scale-110 hover:shadow-[0_6px_20px_rgba(37,211,102,0.23)] transition-all duration-300 reveal-anim flex items-center justify-center group" aria-label="Chat on WhatsApp">
      <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 256 256">
        <path d="M187.58,144.84l-32-16a8,8,0,0,0-8,1.2l-16.23,12.17a71.75,71.75,0,0,1-37.49-37.49l12.17-16.23a8,8,0,0,0,1.2-8l-16-32a8,8,0,0,0-10.61-4.22c-9.61,4-20,13.25-22.18,25.6-2.58,14.65,3,32.35,21.56,50.94,20,20,38.83,24.89,53.8,21.6,12.35-2.22,21.59-12.57,25.6-22.18A8,8,0,0,0,187.58,144.84ZM128,24A104,104,0,0,0,36.18,176.88L24.83,210.93a16,16,0,0,0,20.24,20.24l34.05-11.35A104,104,0,1,0,128,24Zm0,192a87.87,87.87,0,0,1-44.06-11.81,8,8,0,0,0-6.54-1.08L44,214.25l11.15-33.43a8,8,0,0,0-1.08-6.54A88,88,0,1,1,128,216Z"></path>
      </svg>
      <!-- Tooltip -->
      <span class="absolute right-full mr-4 bg-ink text-cream text-sm px-3 py-1.5 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap pointer-events-none font-sans">
        Chat with us
      </span>
    </a>
  </body>
"""

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    if "Floating WhatsApp Button" not in content:
        # Replace </body> with snippet + </body>
        new_content = re.sub(r'</body>', whatsapp_snippet, content)
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Added WhatsApp to {filepath}")
    else:
        print(f"WhatsApp already in {filepath}")

print("Done!")
