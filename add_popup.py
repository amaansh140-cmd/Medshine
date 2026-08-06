import shutil

popup_code = """
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
"""

with open('src/main.js', 'a', encoding='utf-8') as f:
    f.write(popup_code)

shutil.copy('src/main.js', '../Medshine/src/main.js')
