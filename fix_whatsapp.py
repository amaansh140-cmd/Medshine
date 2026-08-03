import glob
import re

html_files = glob.glob("*.html")

new_whatsapp = """
    <!-- Floating WhatsApp Button -->
    <a href="https://wa.me/" target="_blank" class="fixed bottom-6 right-6 z-[9999] bg-[#25D366] text-white w-14 h-14 rounded-full shadow-[0_4px_14px_0_rgba(37,211,102,0.39)] hover:scale-110 hover:shadow-[0_6px_20px_rgba(37,211,102,0.23)] transition-all duration-300 flex items-center justify-center group" aria-label="Chat on WhatsApp">
      <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 24 24">
        <path d="M12.031 0C5.385 0 0 5.386 0 12.031c0 2.122.551 4.195 1.598 6.015L.103 24l6.111-1.603c1.748.956 3.738 1.46 5.817 1.46 6.645 0 12.03-5.385 12.03-12.03C24.06 5.386 18.675 0 12.031 0zm5.952 17.394c-.27.758-1.56 1.455-2.146 1.536-.587.08-1.341.226-4.043-.896-3.243-1.345-5.321-4.664-5.483-4.88-.162-.215-1.31-1.745-1.31-3.328 0-1.583.824-2.366 1.121-2.689.297-.323.647-.404.862-.404.216 0 .432.002.621.012.2.011.472-.078.728.538.256.619.876 2.143.957 2.304.08.162.134.351.026.566-.108.215-.162.35-.323.539-.162.188-.337.417-.485.566-.162.161-.33.336-.148.647.182.31 .81 1.336 1.742 2.162 1.205 1.07 2.213 1.4 2.523 1.562.31.162.498.134.687-.08.188-.216.809-.942 1.024-1.266.216-.323.432-.27.716-.162.283.108 1.792.845 2.102 1.007.31.162.512.242.587.377.075.134.075.782-.195 1.54z"/>
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
    
    # We replace the previous snippet.
    # The previous snippet started with <!-- Floating WhatsApp Button --> and ended with </a>\n  </body>
    # Let's just use regex to match from <!-- Floating WhatsApp Button --> to </body>
    
    pattern = r'<!-- Floating WhatsApp Button -->.*?</body>'
    new_content = re.sub(pattern, new_whatsapp.strip(), content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Fixed WhatsApp in {filepath}")

print("Done fixing!")
