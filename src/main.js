// Configuration for blob mask trails
const POINTS_COUNT = 8;
const START_RADIUS = 150;
const END_RADIUS = 30;

// Setup mask circles
const maskGroup = document.getElementById('mask-group');
const circles = [];
const points = [];

// Initialize points and SVG circles
for (let i = 0; i < POINTS_COUNT; i++) {
  // Add SVG circle
  const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  
  // Calculate decreasing radius
  const radius = START_RADIUS - ((START_RADIUS - END_RADIUS) * (i / (POINTS_COUNT - 1)));
  circle.setAttribute('r', radius);
  
  // Default position offscreen
  circle.setAttribute('cx', -1000);
  circle.setAttribute('cy', -1000);
  
  maskGroup.appendChild(circle);
  circles.push(circle);
  
  // Data for physics
  points.push({ x: -1000, y: -1000 });
}

// Mouse and touch tracking for gooey reveal on desktop and mobile
let clientX = window.innerWidth / 2;
let clientY = window.innerHeight / 2;

// Track active scale factor for touch device transitions
let targetScale = window.innerWidth > 768 ? 1.0 : 0.0;
let currentScale = targetScale;
let isTouched = false;

window.addEventListener('mousemove', (e) => {
  // If we detect mouse movement, ensure targetScale is 1.0 (desktop mode)
  if (window.innerWidth > 768) {
    targetScale = 1.0;
  }
  clientX = e.clientX;
  clientY = e.clientY;
}, { passive: true });

window.addEventListener('touchstart', (e) => {
  isTouched = true;
  targetScale = 1.0;
  if (e.touches && e.touches[0]) {
    clientX = e.touches[0].clientX;
    clientY = e.touches[0].clientY;
  }
}, { passive: true });

window.addEventListener('touchmove', (e) => {
  isTouched = true;
  targetScale = 1.0;
  if (e.touches && e.touches[0]) {
    clientX = e.touches[0].clientX;
    clientY = e.touches[0].clientY;
  }
}, { passive: true });

window.addEventListener('touchend', () => {
  isTouched = false;
  if (window.innerWidth <= 768) {
    targetScale = 0.0;
  }
}, { passive: true });

window.addEventListener('touchcancel', () => {
  isTouched = false;
  if (window.innerWidth <= 768) {
    targetScale = 0.0;
  }
}, { passive: true });

// Listen for resize to adjust default scale
window.addEventListener('resize', () => {
  if (window.innerWidth > 768) {
    targetScale = 1.0;
  } else if (!isTouched) {
    targetScale = 0.0;
  }
}, { passive: true });


// Animation loop
function animate() {
  if (!document.getElementById('mask-group') || window.innerWidth <= 768) {
    requestAnimationFrame(animate);
    return;
  }

  // Smoothly transition the scale factor (expanding/shrinking)
  currentScale += (targetScale - currentScale) * 0.15;

  const targetX = clientX;
  const targetY = clientY + window.scrollY;

  // Smooth follow for the lead point
  points[0].x += (targetX - points[0].x) * 0.15;
  points[0].y += (targetY - points[0].y) * 0.15;
    
  // Subsequent points follow the previous point
  for (let i = 1; i < POINTS_COUNT; i++) {
    points[i].x += (points[i-1].x - points[i].x) * 0.35;
    points[i].y += (points[i-1].y - points[i].y) * 0.35;
  }
  
  // Update SVG circles (both position and dynamic radius scaling!)
  for (let i = 0; i < POINTS_COUNT; i++) {
    const baseRadius = START_RADIUS - ((START_RADIUS - END_RADIUS) * (i / (POINTS_COUNT - 1)));
    circles[i].setAttribute('cx', points[i].x);
    circles[i].setAttribute('cy', points[i].y);
    circles[i].setAttribute('r', baseRadius * currentScale);
  }
  
  requestAnimationFrame(animate);
}

// Start animation loop
animate();

// Universal Mobile & Tablet Navigation Drawer Initialization
document.addEventListener('DOMContentLoaded', () => {
  const nav = document.querySelector('nav');
  if (!nav || document.getElementById('mobile-drawer')) return;

  // Find inner flex container of nav
  const navInner = nav.querySelector('.max-w-\\[1240px\\]') || nav.querySelector('.flex.items-center.justify-between') || nav;

  // Create Hamburger Button
  const menuBtn = document.createElement('button');
  menuBtn.id = 'mobile-menu-btn';
  menuBtn.className = 'mobile-menu-btn flex items-center justify-center px-4 py-2 rounded-md border border-ink/20 bg-ink/5 text-ink hover:bg-ink/10 focus:outline-none ml-2 text-sm font-semibold tracking-wide transition-colors';
  menuBtn.setAttribute('aria-label', 'Open Menu');
  menuBtn.innerHTML = 'Menu';

  // Insert hamburger button right next to the CTA button or inside navInner
  const ctaBtn = navInner.querySelector('a[href="contact.html"]');
  if (ctaBtn && ctaBtn.parentNode === navInner) {
    const btnWrapper = document.createElement('div');
    btnWrapper.className = 'flex items-center gap-2';
    navInner.insertBefore(btnWrapper, ctaBtn);
    btnWrapper.appendChild(ctaBtn);
    btnWrapper.appendChild(menuBtn);
  } else {
    navInner.appendChild(menuBtn);
  }

  // Create Backdrop
  const backdrop = document.createElement('div');
  backdrop.className = 'mobile-drawer-backdrop';
  backdrop.id = 'mobile-drawer-backdrop';

  // Create Drawer
  const drawer = document.createElement('div');
  drawer.className = 'mobile-drawer';
  drawer.id = 'mobile-drawer';
  drawer.innerHTML = `
    <div>
      <div class="flex items-center justify-between pb-6 mb-6 border-b border-ink/10">
        <span class="font-serif font-bold tracking-wider text-lg text-ink">MEDSHINE CLINIC</span>
        <button id="close-drawer-btn" class="p-2 text-ink hover:text-magenta transition-colors focus:outline-none" aria-label="Close Menu">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>
      <nav class="flex flex-col">
        <a href="index.html" class="mobile-drawer-link"><span>Home</span></a>
        <a href="about.html" class="mobile-drawer-link"><span>About Us</span></a>
        <a href="treatments.html" class="mobile-drawer-link"><span>Treatments</span></a>
        <a href="blog.html" class="mobile-drawer-link"><span>Blog</span></a>
        <a href="contact.html" class="mobile-drawer-link"><span>Contact</span></a>
      </nav>
    </div>
    <div class="mt-auto pt-8 border-t border-ink/10 w-full flex items-center justify-center" style="gap: 2.5rem !important; margin-top: auto !important; padding-bottom: 1rem !important;">
      <a href="#" aria-label="Facebook" style="color: #1a1a1a !important; display: inline-flex !important; padding: 0.5rem !important; transition: transform 0.2s ease, color 0.2s ease;" onmouseover="this.style.color='#10b981'; this.style.transform='scale(1.15)'" onmouseout="this.style.color='#1a1a1a'; this.style.transform='scale(1)'">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24" style="width: 24px !important; height: 24px !important; display: block !important;"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
      </a>
      <a href="#" aria-label="Instagram" style="color: #1a1a1a !important; display: inline-flex !important; padding: 0.5rem !important; transition: transform 0.2s ease, color 0.2s ease;" onmouseover="this.style.color='#10b981'; this.style.transform='scale(1.15)'" onmouseout="this.style.color='#1a1a1a'; this.style.transform='scale(1)'">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24" style="width: 24px !important; height: 24px !important; display: block !important;"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
      </a>
      <a href="#" aria-label="Google" style="color: #1a1a1a !important; display: inline-flex !important; padding: 0.5rem !important; transition: transform 0.2s ease, color 0.2s ease;" onmouseover="this.style.color='#10b981'; this.style.transform='scale(1.15)'" onmouseout="this.style.color='#1a1a1a'; this.style.transform='scale(1)'">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24" style="width: 24px !important; height: 24px !important; display: block !important;"><path d="M12.48 10.92v3.28h7.84c-.24 1.84-.853 3.187-1.787 4.133-1.147 1.147-2.933 2.4-6.053 2.4-4.827 0-8.6-3.893-8.6-8.72s3.773-8.72 8.6-8.72c2.6 0 4.507 1.027 5.907 2.347l2.307-2.307C18.747 1.44 16.133 0 12.48 0 5.867 0 .307 5.387.307 12s5.56 12 12.173 12c3.573 0 6.267-1.173 8.373-3.36 2.16-2.16 2.84-5.213 2.84-7.667 0-.76-.053-1.467-.173-2.053H12.48z"/></svg>
      </a>
    </div>
  `;

  document.body.appendChild(backdrop);
  document.body.appendChild(drawer);

  const closeBtn = drawer.querySelector('#close-drawer-btn');

  const openDrawer = () => {
    backdrop.classList.add('is-open');
    drawer.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  };

  const closeDrawer = () => {
    backdrop.classList.remove('is-open');
    drawer.classList.remove('is-open');
    document.body.style.overflow = '';
  };

  menuBtn.addEventListener('click', openDrawer);
  closeBtn.addEventListener('click', closeDrawer);
  backdrop.addEventListener('click', closeDrawer);
});

// Global Appointment Popup Modal
document.addEventListener('DOMContentLoaded', () => {
  const lastPopupTime = sessionStorage.getItem('popupShownTime');
  const now = new Date().getTime();
  
  const modalHTML = `
    <div id="booking-modal" class="fixed inset-0 z-[100] flex items-center justify-center pointer-events-none opacity-0 transition-opacity duration-500">
      <div class="absolute inset-0 bg-ink/40 backdrop-blur-sm modal-bg pointer-events-auto cursor-pointer"></div>
      <div class="relative bg-cream w-full max-w-md mx-4 rounded-3xl p-8 shadow-2xl border border-ink/10 transform scale-95 transition-transform duration-500 pointer-events-auto flex flex-col modal-content">
        <button id="close-modal" class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center rounded-full bg-ink/5 hover:bg-ink/10 text-ink transition-colors cursor-pointer">
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M1 1L13 13M1 13L13 1" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
        <h3 class="font-serif text-2xl font-semibold text-ink mb-2">Book Your Appointment</h3>
        <p class="text-inkmute text-sm mb-6">Take the first step towards your aesthetic and clinical wellness journey.</p>
        
        <form id="popup-booking-form" class="flex flex-col gap-4">
          <input type="text" placeholder="Full Name" required class="w-full bg-transparent border-b border-ink/20 py-3 text-ink placeholder:text-inkmute/60 focus:outline-none focus:border-ink transition-colors text-sm">
          <input type="tel" placeholder="Phone Number" required class="w-full bg-transparent border-b border-ink/20 py-3 text-ink placeholder:text-inkmute/60 focus:outline-none focus:border-ink transition-colors text-sm">
          <select required class="w-full bg-transparent border-b border-ink/20 py-3 text-ink focus:outline-none focus:border-ink transition-colors text-sm appearance-none cursor-pointer">
            <option value="" disabled selected>Select Doctor / Department</option>
            <option value="dr_priya">Dr. Priya Jain (Skin & Aesthetics)</option>
            <option value="dr_ankur">Dr. Ankur Jain (Internal Medicine)</option>
          </select>
          <button type="submit" class="mt-4 bg-ink text-cream py-3.5 rounded-full font-medium text-sm hover:bg-magentadeep transition-colors w-full cursor-pointer">Request Appointment</button>
        </form>
      </div>
    </div>
  `;
  
  document.body.insertAdjacentHTML('beforeend', modalHTML);
  
  const modal = document.getElementById('booking-modal');
  const modalContent = modal.querySelector('.modal-content');
  const closeBtn = document.getElementById('close-modal');
  const modalBg = modal.querySelector('.modal-bg');
  
  function openModal() {
    modal.classList.remove('pointer-events-none', 'opacity-0');
    modalContent.classList.remove('scale-95');
    modalContent.classList.add('scale-100');
  }
  
  function closeModal() {
    modal.classList.add('opacity-0', 'pointer-events-none');
    modalContent.classList.remove('scale-100');
    modalContent.classList.add('scale-95');
  }
  
  closeBtn.addEventListener('click', closeModal);
  modalBg.addEventListener('click', closeModal);
  
  document.getElementById('popup-booking-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = e.target.querySelector('button');
    btn.textContent = 'Request Sent!';
    btn.classList.add('bg-inkmute');
    btn.classList.remove('bg-ink', 'hover:bg-magentadeep');
    setTimeout(closeModal, 1500);
  });
  
  // Show popup on navigation with a 1 minute cooldown to prevent spamming
  if (!lastPopupTime || (now - lastPopupTime > 60000)) {
    setTimeout(() => {
      openModal();
      sessionStorage.setItem('popupShownTime', now);
    }, 1200);
  }
});
