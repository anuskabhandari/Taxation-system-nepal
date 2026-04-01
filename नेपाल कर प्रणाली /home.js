        // Language toggle functionality
        document.querySelectorAll('.lang-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                
                // Store language preference
                const lang = this.textContent.trim();
                localStorage.setItem('preferredLanguage', lang);
                
                console.log('Language switched to:', lang);
            });
        });

        // Restore language preference
        const savedLang = localStorage.getItem('preferredLanguage');
        if (savedLang) {
            document.querySelectorAll('.lang-btn').forEach(btn => {
                if (btn.textContent.trim() === savedLang) {
                    btn.click();
                }
            });
        }

        // Card hover effect
        document.querySelectorAll('.card').forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.style.transition = 'all 0.3s ease';
            });
        });

        // Smooth scroll for navigation
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });
