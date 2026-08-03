def fix_file(filename, title):
    with open(filename, 'r') as f:
        content = f.read()
    
    # If it ends abruptly at whitespace after the opening <p> tag
    if not '</body>' in content:
        ending = f"""Experience the transformative care of Medshine Clinic with our specialized {title} treatments. Medshine experts utilize the latest clinical advancements and customized protocols to ensure safe, effective, and outstanding results for your unique needs.
          </p>
          <div class="mt-10 reveal-anim">
            <a href="contact.html" class="inline-flex items-center justify-center bg-cream text-ink px-8 py-4 rounded-full font-medium hover:bg-white transition-colors hover-scale">
              Book Appointment
            </a>
          </div>

        </section>

      </div>
    </div>

    <!-- Floating WhatsApp Button -->
    <a href="https://wa.me/917506251933" target="_blank" class="fixed bottom-6 right-6 z-[9999] bg-[#25D366] text-white w-14 h-14 rounded-full shadow-[0_4px_14px_0_rgba(37,211,102,0.39)] hover:scale-110 hover:shadow-[0_6px_20px_rgba(37,211,102,0.23)] transition-all duration-300 flex items-center justify-center group" aria-label="Chat on WhatsApp">
      <svg viewBox="0 0 32 32" class="w-8 h-8 fill-current" xmlns="http://www.w3.org/2000/svg">
        <path d="M16.002 2.016C8.28 2.016 2.016 8.28 2.016 16.002c0 2.457.636 4.839 1.845 6.945L2.016 30l7.218-1.89c2.046 1.107 4.35 1.692 6.768 1.692 7.722 0 13.986-6.264 13.986-13.986S23.724 2.016 16.002 2.016zm0 25.434c-2.073 0-4.113-.537-5.901-1.554l-.423-.243-4.383 1.149 1.167-4.275-.27-.429a11.602 11.602 11.602 0 0 1-1.776-6.195c0-6.426 5.232-11.658 11.658-11.658 6.426 0 11.658 5.232 11.658 11.658 0 6.426-5.232 11.658-11.658 11.658zM22.39 19.34c-.348-.174-2.064-1.02-2.382-1.137-.318-.117-.549-.174-.783.174-.234.348-.9 1.137-1.104 1.371-.204.234-.408.261-.756.087-.348-.174-1.473-.543-2.805-1.731-1.035-.924-1.734-2.067-1.938-2.415-.204-.348-.021-.537.153-.711.156-.156.348-.405.522-.609.174-.204.234-.348.348-.582.114-.234.057-.441-.03-.615-.087-.174-.783-1.89-1.074-2.589-.285-.681-.573-.588-.783-.597-.204-.009-.441-.009-.675-.009s-.615.087-.939.441C9.692 11.77 8.798 12.64 8.798 14.41c0 1.77 1.095 3.483 1.248 3.687.153.204 2.517 3.843 6.096 5.391 3.579 1.548 3.579 1.035 4.236.978.657-.057 2.064-.843 2.355-1.659.291-.816.291-1.515.204-1.659-.087-.144-.318-.231-.666-.405z"/>
      </svg>
    </a>

    <script type="module" src="/src/main.js"></script>
    <script type="module" src="/src/transition.js"></script>
    <script type="module" src="/src/animations.js"></script>
  </body>
</html>"""
        
        with open(filename, 'a') as f:
            f.write(ending)
        print(f"Fixed {filename}")

fix_file("treatment-injectables-skin-booster.html", "Skin booster")
fix_file("treatment-injectables-scar-subscision-treatment.html", "Scar subscision treatment")
