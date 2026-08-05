function initScrollAnimations() {
  const observerOptions = {
    root: null,
    rootMargin: '50px',
    threshold: 0.05
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  const revealElements = document.querySelectorAll('.reveal-anim, .reveal-fade, .reveal-slide-left');
  revealElements.forEach(el => observer.observe(el));
  
  // Failsafe: if IntersectionObserver fails to fire for elements already in viewport on load, force them visible after a short delay
  setTimeout(() => {
    document.querySelectorAll('.reveal-anim, .reveal-fade, .reveal-slide-left').forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom >= 0) {
        el.classList.add('is-visible');
      }
    });
  }, 100);
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initScrollAnimations);
} else {
  initScrollAnimations();
}



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
