document.addEventListener('DOMContentLoaded', () => {

    // --- 0. Image Right-Click Protection (site-wide) ---
    document.querySelectorAll('img').forEach(img => {
        img.addEventListener('contextmenu', e => e.preventDefault());
        img.addEventListener('dragstart', e => e.preventDefault());
    });
    // Also block future dynamically-added images
    document.addEventListener('contextmenu', e => {
        if (e.target.tagName === 'IMG') e.preventDefault();
    });

    // --- 1. Dark/Light Mode Management ---
    // Enforce dark mode permanently as requested
    const htmlElement = document.documentElement;
    htmlElement.classList.add('dark');
    localStorage.setItem('color-theme', 'dark');

    // --- 2. Navbar Scroll Effect & Blur ---
    const navbar = document.getElementById('navbar');
    const navBg = document.getElementById('nav-bg');
    if(navbar && navBg) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('shadow-2xl');
                navBg.classList.add('bg-kim-darker/90', 'backdrop-blur-xl', 'border-b', 'border-gray-800');
                navBg.classList.remove('bg-transparent');
            } else {
                navbar.classList.remove('shadow-2xl');
                navBg.classList.remove('bg-kim-darker/90', 'backdrop-blur-xl', 'border-b', 'border-gray-800');
                navBg.classList.add('bg-transparent');
            }
        });
    }

    // --- 3. Mega Menu Logic ---
    const modelesLink = document.getElementById('nav-modeles');
    const megaMenu = document.getElementById('mega-menu');
    
    if (modelesLink && megaMenu) {
        let timeout;
        
        const openMenu = () => {
            clearTimeout(timeout);
            megaMenu.classList.add('active');
            modelesLink.classList.add('text-kim-red');
        };
        
        const closeMenu = () => {
            timeout = setTimeout(() => {
                megaMenu.classList.remove('active');
                modelesLink.classList.remove('text-kim-red');
            }, 300);
        };

        modelesLink.addEventListener('mouseenter', openMenu);
        megaMenu.addEventListener('mouseenter', openMenu);
        
        modelesLink.addEventListener('mouseleave', closeMenu);
        megaMenu.addEventListener('mouseleave', closeMenu);
    }

    // --- 4. Magnetic Buttons (Dynamism 2026) ---
    const magneticBtns = document.querySelectorAll('.magnetic-wrap');
    
    magneticBtns.forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            
            // Move the button slightly towards the cursor
            gsap.to(btn, {
                x: x * 0.3,
                y: y * 0.3,
                duration: 0.5,
                ease: "power2.out"
            });
        });
        
        btn.addEventListener('mouseleave', () => {
            gsap.to(btn, {
                x: 0,
                y: 0,
                duration: 0.7,
                ease: "elastic.out(1, 0.3)"
            });
        });
    });

    // --- 5. Mobile Menu ---
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const closeMobileMenuBtn = document.getElementById('close-mobile-menu');
    const mobileMenu = document.getElementById('mobile-menu');

    if(mobileMenuBtn && closeMobileMenuBtn && mobileMenu) {
        const toggleMobileMenu = () => {
            mobileMenu.classList.toggle('translate-x-full');
            document.body.classList.toggle('overflow-hidden');
            
            const header = document.getElementById('navbar');
            if (header) {
                if (mobileMenu.classList.contains('translate-x-full')) {
                    header.classList.remove('opacity-0', 'pointer-events-none');
                } else {
                    header.classList.add('opacity-0', 'pointer-events-none');
                }
            }
        };
        mobileMenuBtn.addEventListener('click', toggleMobileMenu);
        closeMobileMenuBtn.addEventListener('click', toggleMobileMenu);
    }

    // --- 6. Hero Carousel Logic ---
    const heroCarousel = document.getElementById('hero-carousel');
    const indicatorContainer = document.getElementById('carousel-indicators');

    if (heroCarousel && typeof heroData !== 'undefined') {
        let currentSlide = 0;
        
        // Render Slides
        heroData.forEach((data, index) => {
            const slide = document.createElement('div');
            slide.className = `hero-slide ${index === 0 ? 'active' : ''}`;
            slide.innerHTML = `
                <div class="hero-slide-bg">
                    <picture>
                        <source media="(max-width: 768px)" srcset="${data.imageMobile || data.imageDesktop}">
                        <img src="${data.imageDesktop}" alt="${data.title}" class="w-full h-full object-cover opacity-90">
                    </picture>
                    <div class="absolute inset-0 bg-gradient-to-t from-kim-darker/80 via-transparent to-transparent"></div>
                </div>
                <div class="container mx-auto px-4 lg:px-8 relative z-20 h-full flex items-end pb-20 md:pb-24 lg:pb-32">
                    <div class="max-w-4xl w-full">
                        <div class="flex flex-wrap gap-6 hero-elem">
                            <div class="magnetic-wrap">
                                <a href="${data.buttonLink}" class="magnetic-btn px-5 py-3 md:px-10 md:py-5 bg-kim-red text-white font-bold uppercase tracking-widest text-[10px] md:text-sm">
                                    <span class="relative z-10 flex items-center gap-2 md:gap-3 whitespace-nowrap">${data.buttonText} <i class="fa-solid fa-arrow-right"></i></span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            `;
            heroCarousel.appendChild(slide);

            // Indicators
            const indicator = document.createElement('div');
            indicator.className = `carousel-indicator ${index === 0 ? 'active' : ''}`;
            indicator.addEventListener('click', () => goToSlide(index));
            indicatorContainer.appendChild(indicator);
        });

        const slides = document.querySelectorAll('.hero-slide');
        const indicators = document.querySelectorAll('.carousel-indicator');

        const progressBar = document.createElement('div');
        progressBar.className = 'absolute bottom-0 left-0 h-1 bg-gradient-to-r from-kim-red via-red-500 to-kim-red w-full origin-left carousel-progress z-30';
        heroCarousel.appendChild(progressBar);

        const goToSlide = (index) => {
            slides[currentSlide].classList.remove('active');
            indicators[currentSlide].classList.remove('active');
            currentSlide = index;
            slides[currentSlide].classList.add('active');
            indicators[currentSlide].classList.add('active');
            
            // Reset Progress Bar Animation
            progressBar.style.animation = 'none';
            progressBar.offsetHeight; // Trigger reflow
            progressBar.style.animation = 'progressAnim 4s linear infinite';
        };

        const nextSlide = () => {
            goToSlide((currentSlide + 1) % heroData.length);
        };

        // Auto play
        let slideInterval = setInterval(nextSlide, 4000);
    }

    // --- 7. Scroll to Top Lazy Button ---
    const scrollTopBtn = document.createElement('button');
    scrollTopBtn.innerHTML = '<i class="fa-solid fa-arrow-up text-xl"></i>';
    scrollTopBtn.className = 'fixed bottom-8 right-8 bg-kim-red text-white w-12 h-12 rounded-full flex items-center justify-center shadow-2xl opacity-0 pointer-events-none transition-all duration-300 z-50 hover:bg-kim-dark hover:scale-110';
    document.body.appendChild(scrollTopBtn);

    window.addEventListener('scroll', () => {
        if (window.scrollY > 400) {
            scrollTopBtn.classList.remove('opacity-0', 'pointer-events-none');
            scrollTopBtn.classList.add('opacity-100', 'pointer-events-auto');
        } else {
            scrollTopBtn.classList.remove('opacity-100', 'pointer-events-auto');
            scrollTopBtn.classList.add('opacity-0', 'pointer-events-none');
        }
    });

    scrollTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // --- GSAP Init ---
    if(typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);
    }
});

// --- Loader Management ---
// Uses window 'load' so it fires only after ALL resources (images, videos, scripts) are ready.
// A minimum display duration ensures the fill animation is always visible.
(function() {
    const loader = document.getElementById('loader');
    if (!loader) return;

    const isHomePage = !!document.getElementById('hero-carousel');
    const MIN_DISPLAY = isHomePage ? 5200 : 1400; // minimum ms loader stays visible
    const startTime = Date.now();

    // Adjust fill animation speed for sub-pages
    if (!isHomePage) {
        const fillEl = loader.querySelector('.loader-fill');
        if (fillEl) fillEl.style.animation = 'fillUp 1.2s cubic-bezier(0.85, 0, 0.15, 1) forwards';
    }

    function hideLoader() {
        const elapsed = Date.now() - startTime;
        const remaining = Math.max(0, MIN_DISPLAY - elapsed);

        setTimeout(() => {
            loader.style.transition = 'opacity 0.7s ease';
            loader.style.opacity = '0';
            loader.style.pointerEvents = 'none';

            setTimeout(() => {
                loader.style.display = 'none';

                // Animate hero on home page if GSAP is available
                if (isHomePage && typeof gsap !== 'undefined') {
                    gsap.fromTo('.hero-slide.active .hero-elem',
                        { y: 50, opacity: 0 },
                        { y: 0, opacity: 1, duration: 1.2, stagger: 0.15, ease: 'power3.out' }
                    );
                }
            }, 700);
        }, remaining);
    }

    if (document.readyState === 'complete') {
        // Page already loaded (e.g. cached)
        hideLoader();
    } else {
        window.addEventListener('load', hideLoader, { once: true });
    }
})();
