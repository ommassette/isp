// Toast notification function
function showToast(message, duration = 3000) {
  const toast = document.getElementById('toast');
  toast.textContent = message;
  toast.style.opacity = '1';
  setTimeout(() => {
    toast.style.opacity = '0';
  }, duration);
}

// Dark Mode Toggle with local storage
const darkModeToggle = document.getElementById('darkModeToggle');
const body = document.body;

if (localStorage.getItem('darkMode') === 'enabled') {
  body.classList.add('dark');
  darkModeToggle.textContent = 'Theme';
}

darkModeToggle.addEventListener('click', (e) => {
  e.preventDefault();
  body.classList.toggle('dark');
  if (body.classList.contains('dark')) {
    localStorage.setItem('darkMode', 'enabled');
    darkModeToggle.textContent = 'Theme';
    showToast('🌙 Dark mode activated');
  } else {
    localStorage.setItem('darkMode', 'disabled');
    darkModeToggle.textContent = 'Theme';
    showToast('☀️ Light mode activated');
  }
});

// Get Started button smooth scroll
const getStartedBtn = document.getElementById('getStartedBtn');
getStartedBtn.addEventListener('click', () => {
  const contactFormSection = document.querySelector('.feedback');
  contactFormSection.scrollIntoView({ behavior: 'smooth', block: 'center' });
  showToast('✨ Fill out the form to get connected!');
});

// Form submission handler with validation and Django integration
const contactForm = document.getElementById('contactForm');

contactForm.addEventListener('submit', (e) => {
  // Prevent immediate submission to run validation first
  e.preventDefault();
  
  const fullName = document.getElementById('fullName').value.trim();
  const email = document.getElementById('email').value.trim();
  const phone = document.getElementById('phone').value.trim();
  const message = document.getElementById('message').value.trim();
  
  // Validation
  if (!fullName) {
    showToast('❌ Please enter your full name', 2500);
    return;
  }
  if (!email) {
    showToast('❌ Please enter your email address', 2500);
    return;
  }
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    showToast('❌ Please enter a valid email address', 2500);
    return;
  }
  if (!phone) {
    showToast('❌ Please enter your phone number', 2500);
    return;
  }
  const phoneRegex = /^[\d\s\+\(\)\-]{8,}$/;
  if (!phoneRegex.test(phone)) {
    showToast('❌ Please enter a valid phone number', 2500);
    return;
  }
  
  // If validation passes, manually trigger the form submission to the Django backend
  contactForm.submit();
});

// Add hover effect for area cards with additional info
const areaCards = document.querySelectorAll('.kinoo');
const areaInfo = {
  'Kinoo': '📡 Up to 500 Mbps coverage',
  '87 Area': '🏢 Business district - 24/7 support',
  'Muthiga': '🏠 Residential fiber-ready',
  'Regency': '⭐ Premium zone - 1Gbps available'
};

areaCards.forEach(card => {
  const title = card.querySelector('h3').textContent;
  card.addEventListener('mouseenter', () => {
    const info = areaInfo[title] || '✅ Full coverage available';
    const tooltip = document.createElement('div');
    tooltip.className = 'area-tooltip';
    tooltip.textContent = info;
    tooltip.style.position = 'absolute';
    tooltip.style.bottom = '80px';
    tooltip.style.left = '20px';
    tooltip.style.backgroundColor = 'rgba(0,0,0,0.8)';
    tooltip.style.backdropFilter = 'blur(5px)';
    tooltip.style.padding = '5px 12px';
    tooltip.style.borderRadius = '20px';
    tooltip.style.fontSize = '0.8rem';
    tooltip.style.color = 'white';
    tooltip.style.zIndex = '10';
    tooltip.style.whiteSpace = 'nowrap';
    
    const existing = card.querySelector('.area-tooltip');
    if (existing) existing.remove();
    card.style.position = 'relative';
    card.appendChild(tooltip);
  });
  
  card.addEventListener('mouseleave', () => {
    const tooltip = card.querySelector('.area-tooltip');
    if (tooltip) tooltip.remove();
  });
});

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const href = this.getAttribute('href');
    if (href !== '#' && href.startsWith('#')) {
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    }
  });
});

// Card click effects
const cards = document.querySelectorAll('.speed, .wires, .connect');
cards.forEach(card => {
  card.addEventListener('click', () => {
    const title = card.querySelector('h3').textContent;
    showToast(`✨ ${title} - our premium feature!`, 2000);
  });
});

// Welcome toast on page load
window.addEventListener('load', () => {
  setTimeout(() => {
    showToast('🚀 Welcome to TorNet - Your wireless internet solution!', 3500);
  }, 500);
});