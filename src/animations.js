document.addEventListener('DOMContentLoaded', () => {
  // Intersection Observer for scroll animations
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15 // Trigger when 15% of the element is visible
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Add the visible class to trigger the CSS transition
        entry.target.classList.add('is-visible');
        // Stop observing once it's visible so it doesn't animate out when scrolling back up (optional, but standard for reveals)
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Select all elements that have a reveal class
  const revealElements = document.querySelectorAll('.reveal-anim, .reveal-fade, .reveal-slide-left');
  
  revealElements.forEach(el => {
    observer.observe(el);
  });
});
