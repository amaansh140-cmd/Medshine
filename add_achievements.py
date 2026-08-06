import re
import shutil

html_code = """
<!-- Achievements Marquee -->
<section class="w-full bg-[#0a0a0a] text-cream py-8 md:py-12 overflow-hidden relative z-10 border-y border-[#222]">
  <div class="flex whitespace-nowrap marquee-container items-center w-max">
    <div class="marquee-content flex items-center">
      <!-- Item 1 -->
      <div class="flex flex-col items-center justify-center px-12 md:px-24 border-r border-cream/15 min-w-[280px]">
        <div class="flex items-baseline text-4xl md:text-[3.2rem] font-serif font-semibold tracking-tight mb-3">
          <span class="counter-value" data-target="10000">0</span>
          <span class="text-inkmute/90 text-3xl md:text-4xl">+</span>
        </div>
        <span class="text-[11px] md:text-xs tracking-[0.25em] font-semibold text-cream/70 uppercase">Happy Patients</span>
      </div>
      <!-- Item 2 -->
      <div class="flex flex-col items-center justify-center px-12 md:px-24 border-r border-cream/15 min-w-[280px]">
        <div class="flex items-baseline text-4xl md:text-[3.2rem] font-serif font-semibold tracking-tight mb-3">
          <span class="counter-value" data-target="15">0</span>
          <span class="text-inkmute/90 text-3xl md:text-4xl">+ Yrs</span>
        </div>
        <span class="text-[11px] md:text-xs tracking-[0.25em] font-semibold text-cream/70 uppercase">Experience</span>
      </div>
      <!-- Item 3 -->
      <div class="flex flex-col items-center justify-center px-12 md:px-24 border-r border-cream/15 min-w-[280px]">
        <div class="flex items-baseline text-4xl md:text-[3.2rem] font-serif font-semibold tracking-tight mb-3">
          <span class="counter-value" data-target="50">0</span>
          <span class="text-inkmute/90 text-3xl md:text-4xl">+</span>
        </div>
        <span class="text-[11px] md:text-xs tracking-[0.25em] font-semibold text-cream/70 uppercase">Advanced Treatments</span>
      </div>
      <!-- Item 4 -->
      <div class="flex flex-col items-center justify-center px-12 md:px-24 border-r border-cream/15 min-w-[280px]">
        <div class="flex items-baseline text-4xl md:text-[3.2rem] font-serif font-semibold tracking-tight mb-3">
          <span class="counter-value" data-target="100">0</span>
          <span class="text-inkmute/90 text-3xl md:text-4xl">%</span>
        </div>
        <span class="text-[11px] md:text-xs tracking-[0.25em] font-semibold text-cream/70 uppercase">Evidence-Based</span>
      </div>
    </div>
    
    <!-- Duplicate for seamless scroll -->
    <div class="marquee-content flex items-center" aria-hidden="true">
      <div class="flex flex-col items-center justify-center px-12 md:px-24 border-r border-cream/15 min-w-[280px]">
        <div class="flex items-baseline text-4xl md:text-[3.2rem] font-serif font-semibold tracking-tight mb-3">
          <span class="counter-value" data-target="10000">0</span>
          <span class="text-inkmute/90 text-3xl md:text-4xl">+</span>
        </div>
        <span class="text-[11px] md:text-xs tracking-[0.25em] font-semibold text-cream/70 uppercase">Happy Patients</span>
      </div>
      <div class="flex flex-col items-center justify-center px-12 md:px-24 border-r border-cream/15 min-w-[280px]">
        <div class="flex items-baseline text-4xl md:text-[3.2rem] font-serif font-semibold tracking-tight mb-3">
          <span class="counter-value" data-target="15">0</span>
          <span class="text-inkmute/90 text-3xl md:text-4xl">+ Yrs</span>
        </div>
        <span class="text-[11px] md:text-xs tracking-[0.25em] font-semibold text-cream/70 uppercase">Experience</span>
      </div>
      <div class="flex flex-col items-center justify-center px-12 md:px-24 border-r border-cream/15 min-w-[280px]">
        <div class="flex items-baseline text-4xl md:text-[3.2rem] font-serif font-semibold tracking-tight mb-3">
          <span class="counter-value" data-target="50">0</span>
          <span class="text-inkmute/90 text-3xl md:text-4xl">+</span>
        </div>
        <span class="text-[11px] md:text-xs tracking-[0.25em] font-semibold text-cream/70 uppercase">Advanced Treatments</span>
      </div>
      <div class="flex flex-col items-center justify-center px-12 md:px-24 border-r border-cream/15 min-w-[280px]">
        <div class="flex items-baseline text-4xl md:text-[3.2rem] font-serif font-semibold tracking-tight mb-3">
          <span class="counter-value" data-target="100">0</span>
          <span class="text-inkmute/90 text-3xl md:text-4xl">%</span>
        </div>
        <span class="text-[11px] md:text-xs tracking-[0.25em] font-semibold text-cream/70 uppercase">Evidence-Based</span>
      </div>
    </div>
  </div>
</section>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before <!-- Image Slider Section -->
if "<!-- Achievements Marquee -->" not in content:
    content = content.replace('<!-- Image Slider Section -->', html_code + '\n<!-- Image Slider Section -->')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected HTML into index.html")
else:
    print("HTML already exists in index.html")

css_code = """
/* Marquee Animation */
.marquee-container {
  display: flex;
  width: max-content;
  animation: scrollMarquee 25s linear infinite;
}
.marquee-container:hover {
  animation-play-state: paused;
}
@keyframes scrollMarquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
"""

with open('src/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if "scrollMarquee" not in css_content:
    with open('src/style.css', 'a', encoding='utf-8') as f:
        f.write('\n' + css_code)
    print("Injected CSS into src/style.css")

js_code = """
// Number Counter Animation
document.addEventListener('DOMContentLoaded', () => {
  const counters = document.querySelectorAll('.counter-value');
  const speed = 200; // The lower the slower

  const animateCounter = (counter) => {
    const target = +counter.getAttribute('data-target');
    const count = +counter.innerText;
    
    // Calculate increment step based on target size
    const inc = target / speed;

    if (count < target) {
      counter.innerText = Math.ceil(count + inc);
      setTimeout(() => animateCounter(counter), 10);
    } else {
      // For large numbers, format with commas
      if (target >= 1000) {
        counter.innerText = target.toLocaleString();
      } else {
        counter.innerText = target;
      }
    }
  };

  const counterObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(counter => {
    counterObserver.observe(counter);
  });
});
"""

with open('src/animations.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

if "counterObserver" not in js_content:
    with open('src/animations.js', 'a', encoding='utf-8') as f:
        f.write('\n' + js_code)
    print("Injected JS into src/animations.js")

