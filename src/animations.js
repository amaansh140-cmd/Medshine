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

