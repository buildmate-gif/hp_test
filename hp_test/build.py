import os

HEAD_INJECT = """
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="株式会社BuildTech AI - 中小建設会社向けAI導入コンサルティング。現場の経験値をデータに変え、工期削減と安全管理を支援します。">
    <meta property="og:title" content="株式会社BuildTech AI | 建設現場の経験値をデータに変える">
    <meta property="og:description" content="中小建設会社向けAI導入コンサルティング。現場の経験値をデータに変え、工期削減と安全管理を支援します。">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="ja_JP">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&family=Noto+Sans+JP:wght@400;500;700&family=Space+Grotesk:wght@300..700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#1B3A6B',
                        accent: '#C45C1A',
                        surface: '#EDEAE4',
                        bg: '#F5F7FA',
                        text: '#1C1B18',
                        'text-sub': '#5C5C5C',
                    },
                    fontFamily: {
                        'h1': ['"Space Grotesk"', 'sans-serif'],
                        'h2': ['"Space Grotesk"', 'sans-serif'],
                        'body': ['"Noto Sans JP"', 'sans-serif'],
                        'num': ['"DM Mono"', 'monospace'],
                    }
                }
            }
        }
    </script>
    <style>
        body {
            background-color: #F5F7FA;
            color: #1C1B18;
            font-family: 'Noto Sans JP', sans-serif;
            line-height: 2.0;
        }
        h1 {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: -0.04em;
        }
        h2 {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: -0.02em;
        }
        .num-font {
            font-family: 'DM Mono', monospace;
            color: #C45C1A;
        }
        .num-xl {
            font-size: clamp(3rem, 8vw, 6rem);
            line-height: 1.1;
        }
        .animate-on-scroll {
            opacity: 0;
            transform: translateY(2rem);
            transition: opacity 0.7s ease-out, transform 0.7s ease-out;
        }
        .animate-on-scroll.is-visible {
            opacity: 1;
            transform: translateY(0);
        }
        .nav-link {
            position: relative;
            display: inline-block;
        }
        .nav-link::after {
            content: '';
            position: absolute;
            width: 100%;
            transform: scaleX(0);
            height: 1px;
            bottom: 0;
            left: 0;
            background-color: #C45C1A;
            transform-origin: bottom left;
            transition: transform 0.25s ease-out;
        }
        .nav-link:hover::after {
            transform: scaleX(1);
        }
        .section-number-col {
            position: relative;
        }
        .section-number-col::after {
            content: '';
            position: absolute;
            width: 100%;
            transform: scaleX(0);
            height: 1px;
            bottom: -5px;
            left: 0;
            background-color: #C45C1A;
            transform-origin: bottom left;
            transition: transform 0.3s ease-out;
        }
        .section-number-col:hover::after {
            transform: scaleX(1);
        }
    </style>
"""

COMMON_JS = """
    <script>
        async function loadComponent(id, path) {
            try {
                const res = await fetch(path);
                if (res.ok) {
                    const html = await res.text();
                    document.getElementById(id).innerHTML = html;
                }
            } catch (e) {
                console.error("Failed to load component", path, e);
            }
        }
        
        document.addEventListener('DOMContentLoaded', () => {
            // intersection observer for animations
            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                    }
                });
            }, { threshold: 0.1 });

            document.querySelectorAll('.animate-on-scroll').forEach((el) => {
                observer.observe(el);
            });
            
            // Number count up
            const countObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if(entry.isIntersecting) {
                        const target = entry.target;
                        const endValue = parseInt(target.getAttribute('data-target'), 10);
                        let startValue = 0;
                        const duration = 1500;
                        let startTimestamp = null;
                        
                        const step = (timestamp) => {
                            if (!startTimestamp) startTimestamp = timestamp;
                            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
                            target.innerText = Math.floor(progress * endValue);
                            if (progress < 1) {
                                window.requestAnimationFrame(step);
                            } else {
                                target.innerText = endValue;
                            }
                        };
                        window.requestAnimationFrame(step);
                        countObserver.unobserve(target);
                    }
                });
            }, { threshold: 0.1 });
            
            document.querySelectorAll('.count-up').forEach((el) => {
                countObserver.observe(el);
            });
        });
        
        window.addEventListener('scroll', () => {
            const header = document.querySelector('header');
            if (header && window.scrollY > 50) {
                header.classList.add('shadow-md');
                header.classList.add('bg-bg/95');
                header.classList.remove('bg-transparent');
            } else if (header) {
                header.classList.remove('shadow-md');
                header.classList.remove('bg-bg/95');
                header.classList.add('bg-transparent');
            }
        });
        
        function toggleMenu() {
            const menu = document.getElementById('mobile-menu');
            if(menu) {
                menu.classList.toggle('hidden');
            }
        }
    </script>
"""

with open('/Users/hk/Desktop/hp_test/template_script.py', 'w') as f:
    pass # Wait, I don't need this script just to open files, I can just use string concatenation and output directly.
