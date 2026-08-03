document.addEventListener('DOMContentLoaded', () => {
  // Create and inject page transition overlay if it doesn't exist
  let overlay = document.querySelector('.page-transition-overlay');
  if (!overlay) {
    overlay = document.createElement('div');
    overlay.className = 'page-transition-overlay';
    document.body.appendChild(overlay);
  }
  
  // Fade out the overlay on load
  requestAnimationFrame(() => {
    overlay.classList.add('is-hidden');
  });

  // Intercept link clicks for fade-in
  document.querySelectorAll('a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      
      // If it's an internal page link (not an anchor #, not external http, not mailto)
      if (href && !href.startsWith('#') && !href.startsWith('http') && !href.startsWith('mailto')) {
        e.preventDefault();
        
        // Fade in the overlay
        overlay.classList.remove('is-hidden');
        
        setTimeout(() => {
          window.location.href = href;
        }, 400);
      }
    });
  });
});

// Ensure page is visible if loaded from bfcache (Back/Forward browser buttons)
window.addEventListener('pageshow', (event) => {
  const overlay = document.querySelector('.page-transition-overlay');
  if (overlay && event.persisted) {
    overlay.classList.add('is-hidden');
  }
});
