// ==========================================
// INTERACTIVE ANIMATIONS & EFFECTS
// ==========================================

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize AOS-like animations
    initializeScrollAnimations();
    
    // Mobile menu handler
    handleMobileMenu();
    
    // Smooth scroll
    handleSmoothScroll();
    
    // Project card hover effects
    initializeProjectCards();
    
    // Initialize tooltips (if needed)
    initializeTooltips();
});

// ==========================================
// SCROLL ANIMATIONS
// ==========================================

function initializeScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all cards and sections
    document.querySelectorAll('.card, .stat-card, .feature-item').forEach(el => {
        observer.observe(el);
    });
}

// ==========================================
// MOBILE MENU HANDLER
// ==========================================

function handleMobileMenu() {
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');

    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Close navbar on mobile after clicking a link
            if (window.innerWidth < 992) {
                navbarToggler.click();
            }
        });
    });
}

// ==========================================
// SMOOTH SCROLL
// ==========================================

function handleSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// ==========================================
// PROJECT CARD EFFECTS
// ==========================================

function initializeProjectCards() {
    const projectCards = document.querySelectorAll('.project-card');
    
    projectCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
}

// ==========================================
// NAVBAR BACKGROUND ON SCROLL
// ==========================================

window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 5px 20px rgba(0,0,0,0.2)';
    } else {
        navbar.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
    }
});

// ==========================================
// FORM VALIDATION
// ==========================================

function validateForm() {
    const form = document.getElementById('contactForm');
    if (form) {
        form.addEventListener('submit', function(e) {
            const email = document.getElementById('email').value;
            const name = document.getElementById('name').value;
            const message = document.getElementById('message').value;
            
            // Basic validation
            if (!email || !name || !message) {
                e.preventDefault();
                alert('Sab fields fill karo!');
                return false;
            }
            
            // Email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                e.preventDefault();
                alert('Valid email address likho!');
                return false;
            }
        });
    }
}

// ==========================================
// COUNTER ANIMATION
// ==========================================

function animateCounters() {
    const counters = document.querySelectorAll('.stat-card h3');
    
    counters.forEach(counter => {
        const target = parseInt(counter.innerText);
        if (!isNaN(target)) {
            let current = 0;
            const increment = target / 30;
            
            const updateCounter = () => {
                current += increment;
                if (current < target) {
                    counter.innerText = Math.floor(current) + '+';
                    requestAnimationFrame(updateCounter);
                } else {
                    counter.innerText = target + '+';
                }
            };
            
            // Trigger animation when element is visible
            const observer = new IntersectionObserver((entries) => {
                if (entries[0].isIntersecting) {
                    updateCounter();
                    observer.unobserve(entries[0].target);
                }
            });
            
            observer.observe(counter);
        }
    });
}

// ==========================================
// IMAGE LAZY LOADING
// ==========================================

function initializeLazyLoading() {
    if ('IntersectionObserver' in window) {
        const images = document.querySelectorAll('img[data-src]');
        
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.getAttribute('data-src');
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    }
}

// ==========================================
// TOOLTIPS
// ==========================================

function initializeTooltips() {
    // Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// ==========================================
// ACTIVE LINK HIGHLIGHTER
// ==========================================

function highlightActiveLink() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === currentPath || 
            (currentPath === '/' && link.getAttribute('href') === '/')) {
            link.classList.add('active');
        }
    });
}

// ==========================================
// KEYBOARD SHORTCUTS
// ==========================================

function initializeKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        // Ctrl + K or Cmd + K to focus search (if implemented)
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            // Add search focus logic here
        }
    });
}

// ==========================================
// THEME TOGGLE (Optional Dark Mode)
// ==========================================

function initializeThemeToggle() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
}

// ==========================================
// PERFORMANCE MONITORING
// ==========================================

function logPerformanceMetrics() {
    if (window.performance) {
        const perfData = window.performance.timing;
        const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
        console.log('Page Load Time: ' + pageLoadTime + 'ms');
    }
}

// ==========================================
// CALL ALL INITIALIZATION FUNCTIONS
// ==========================================

// Execute on page load
window.addEventListener('load', function() {
    animateCounters();
    initializeLazyLoading();
    highlightActiveLink();
    validateForm();
    initializeKeyboardShortcuts();
    initializeThemeToggle();
    logPerformanceMetrics();
});

// ==========================================
// UTILITY FUNCTIONS
// ==========================================

// Smooth scroll to element
function scrollToElement(selector) {
    const element = document.querySelector(selector);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Add loading spinner
function showLoadingSpinner(element) {
    element.innerHTML = '<div class="spinner-border text-warning" role="status"><span class="visually-hidden">Loading...</span></div>';
}

// Hide loading spinner
function hideLoadingSpinner(element, content) {
    element.innerHTML = content;
}

// Debounce function
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Check if element is in viewport
function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

console.log('Portfolio App JavaScript Loaded Successfully!');
