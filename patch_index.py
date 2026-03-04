import re
import os

with open('/Users/hk/Desktop/hp_test/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. STYLE: Smooth Scroll
style_insert = """
        html {
            scroll-behavior: smooth;
        }

        body {
"""
content = content.replace("        body {", style_insert, 1)

# 2. HEADER INLINE & SCROLL PROGRESS
header_html = """
    <!-- ▼ 追加: A-1 ヘッダーナビ -->
    <header class="fixed top-0 left-0 w-full z-50 transition-all duration-300 bg-transparent py-4" id="main-header">
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 flex justify-between items-center">
            <!-- Logo -->
            <a href="./index.html" class="flex items-center space-x-2 no-underline text-text">
                <span class="font-h1 font-bold text-xl tracking-tighter">BUILDTECH<span class="text-accent">AI</span></span>
            </a>

            <!-- Desktop Navigation -->
            <nav class="hidden md:flex items-center space-x-8">
                <a href="#services" class="font-h2 text-sm text-text-sub hover:text-text transition-colors nav-link nav-item">サービス</a>
                <a href="#cases" class="font-h2 text-sm text-text-sub hover:text-text transition-colors nav-link nav-item">導入事例</a>
                <a href="#faq" class="font-h2 text-sm text-text-sub hover:text-text transition-colors nav-link nav-item">よくある質問</a>
                <a href="./column/index.html" class="font-h2 text-sm text-text-sub hover:text-text transition-colors nav-link">コラム</a>
                <a href="#company" class="font-h2 text-sm text-text-sub hover:text-text transition-colors nav-link nav-item">会社案内</a>
            </nav>

            <a href="./contact/index.html" class="hidden md:inline-block px-6 py-3 bg-primary text-surface font-h2 text-sm hover:opacity-90 transition-opacity">
                お問い合わせ
            </a>

            <!-- Mobile Menu Button -->
            <button type="button" class="md:hidden text-text p-2" onclick="toggleMobileMenu()" aria-label="Toggle Menu">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="square" stroke-linejoin="miter" stroke-width="1.5" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>
        </div>
    </header>

    <!-- ▼ 追加: A-1 モバイルメニュー -->
    <div id="mobile-menu-overlay" class="fixed inset-0 bg-surface/95 backdrop-blur-md z-40 hidden flex-col items-center justify-center space-y-8 h-screen overflow-y-auto w-full left-0 top-0">
        <button type="button" class="absolute top-6 right-6 text-text p-2" onclick="toggleMobileMenu()" aria-label="Close Menu">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="square" stroke-linejoin="miter" stroke-width="1.5" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
        </button>
        <a href="#services" class="font-h1 text-2xl text-text hover:text-accent" onclick="toggleMobileMenu()">サービス</a>
        <a href="#cases" class="font-h1 text-2xl text-text hover:text-accent" onclick="toggleMobileMenu()">導入事例</a>
        <a href="#faq" class="font-h1 text-2xl text-text hover:text-accent" onclick="toggleMobileMenu()">よくある質問</a>
        <a href="./column/index.html" class="font-h1 text-2xl text-text hover:text-accent" onclick="toggleMobileMenu()">コラム</a>
        <a href="#company" class="font-h1 text-2xl text-text hover:text-accent" onclick="toggleMobileMenu()">会社案内</a>
        <a href="./contact/index.html" class="mt-8 px-8 py-4 bg-primary text-surface font-h2 text-sm tracking-widest hover:opacity-90 transition-opacity" onclick="toggleMobileMenu()">お問い合わせ</a>
    </div>
    
    <!-- ▼ 追加: A-2 スクロール進捗バー -->
    <div class="fixed top-0 left-0 h-[2px] bg-accent z-[60] transition-all duration-100" id="scroll-progress" style="width: 0%;"></div>
"""
content = content.replace('<div id="header"></div>', header_html, 1)

# 3. HERO: Typewriter
hero_text = """                    <h1
                        class="font-h1 text-5xl md:text-7xl lg:text-[5.5rem] tracking-tighter leading-[1.1] mb-12 text-primary">
                        建設現場の経験値を、<br>データに変える。
                    </h1>"""

hero_replacement = """                    <h1
                        class="font-h1 text-5xl md:text-7xl lg:text-[5.5rem] tracking-tighter leading-[1.1] mb-6 text-primary">
                        建設現場の経験値を、<br>データに変える。
                    </h1>
                    <!-- ▼ 追加: B-1 サブテキストタイプライター -->
                    <div class="h-8 mb-8 md:mb-12">
                        <p id="typewriter-text" class="font-h2 text-xl text-accent transition-opacity duration-500 opacity-0"></p>
                    </div>"""
content = content.replace(hero_text, hero_replacement, 1)

# 4. HERO: CTA
hero_buttons_before = """                        <a href="./contact/index.html"
                            class="inline-flex justify-center items-center px-10 py-4 bg-primary text-surface font-h2 text-sm tracking-widest hover:bg-text transition-colors">
                            無料相談はこちら
                        </a>"""
hero_buttons_after = """                        <a href="./contact/index.html"
                            class="inline-flex justify-center items-center px-10 py-4 bg-primary text-surface font-h2 text-sm tracking-widest hover:bg-text transition-colors">
                            無料相談はこちら
                        </a>
                        <!-- ▼ 追加: B-2 AIレベル無料診断ボタン -->
                        <a href="#diagnosis"
                            class="inline-flex justify-center items-center px-10 py-4 border border-accent text-accent font-h2 text-sm tracking-widest hover:bg-accent hover:text-surface transition-colors">
                            AIレベル無料診断 →
                        </a>"""
content = content.replace(hero_buttons_before, hero_buttons_after, 1)

# 5. HERO: KPI Banner
kpi_marker = """            <div class="absolute bottom-10 right-12 hidden md:block opacity-10">
                <span class="font-h1 text-[12rem] leading-none select-none text-text">00</span>
            </div>
        </section>"""
kpi_replacement = """            <div class="absolute bottom-10 right-12 hidden md:block opacity-10">
                <span class="font-h1 text-[12rem] leading-none select-none text-text">00</span>
            </div>

            <!-- ▼ 追加: B-3 KPIバナー -->
            <div class="absolute bottom-0 left-0 w-full border-t border-primary/10 bg-surface/80 backdrop-blur-sm z-20">
                <div class="max-w-[1400px] mx-auto px-6 md:px-12 flex flex-col md:flex-row justify-between py-4 md:py-4 gap-4 md:gap-0">
                    <div class="flex items-center justify-center space-x-4">
                        <span class="font-body text-xs text-text-sub">導入実績</span>
                        <span class="font-num text-xl text-accent"><span class="count-up" data-target="120">0</span>社+</span>
                    </div>
                    <div class="hidden md:block w-px bg-primary/10"></div>
                    <div class="flex items-center justify-center space-x-4">
                        <span class="font-body text-xs text-text-sub">平均工期削減</span>
                        <span class="font-num text-xl text-accent"><span class="count-up" data-target="18">0</span>%</span>
                    </div>
                    <div class="hidden md:block w-px bg-primary/10"></div>
                    <div class="flex items-center justify-center space-x-4">
                        <span class="font-body text-xs text-text-sub">継続率</span>
                        <span class="font-num text-xl text-accent"><span class="count-up" data-target="98">0</span>%</span>
                    </div>
                </div>
            </div>
        </section>"""
content = content.replace(kpi_marker, kpi_replacement, 1)

# 6. D-2 Micro CTA 1
solution_end = "                            </div>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </section>"
solution_end_rep = """                            </div>
                        </div>
                    </div>

                    <!-- ▼ 追加: D-2 マイクロCTA -->
                    <div class="mt-12 md:mt-16 text-right md:text-left border-t border-text/10 pt-6 animate-on-scroll">
                        <a href="./services/index.html" class="inline-flex items-center font-h2 text-xs text-text hover:text-accent transition-colors nav-link">
                            サービス詳細を見る <span class="ml-2">→</span>
                        </a>
                    </div>

                </div>
            </div>
        </section>"""
content = content.replace(solution_end, solution_end_rep, 1)

# 7. ADD NEW SECTIONS (06, 07, 08, 09) BEFORE COMPANY (05->10)
cases_end = """                </div>
            </div>
        </section>

        <!-- COMPANY (05) -->"""

new_sections = """                </div>
            </div>
        </section>

        <!-- ▼ 追加: 06 / SERVICES -->
        <section id="services" aria-label="サービス一覧" class="py-24 md:py-32 w-full">
            <div class="max-w-[1400px] mx-auto px-6 md:px-12 grid grid-cols-12 md:gap-x-8">
                <div class="col-span-12 md:col-span-2 mb-12 md:mb-0 section-num-col">
                    <span class="font-num text-sm text-accent section-num">06 / SERVICES</span>
                </div>
                <div class="col-span-12 md:col-span-10">
                    <h2 class="font-h1 text-4xl mb-16 text-text animate-on-scroll">SERVICES</h2>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                        <div class="bg-bg border-l-2 border-accent p-8 hover:border-l-4 hover:shadow-sm transition-all duration-300 animate-on-scroll flex flex-col h-full">
                            <span class="font-num text-accent mb-4">06.1</span>
                            <h3 class="font-h2 text-lg mb-4 text-text">現場データ構造化パッケージ</h3>
                            <p class="font-body text-sm text-text-sub mb-8 flex-grow">日報・図面・写真をAI解析可能な形に変換。既存業務フローに負担をかけず導入できます。</p>
                            <a href="./services/data.html" class="font-h2 text-xs text-accent mt-auto hover:opacity-70 transition-opacity">詳細を見る →</a>
                        </div>
                        <div class="bg-bg border-l-2 border-accent p-8 hover:border-l-4 hover:shadow-sm transition-all duration-300 animate-on-scroll flex flex-col h-full" style="transition-delay: 100ms;">
                            <span class="font-num text-accent mb-4">06.2</span>
                            <h3 class="font-h2 text-lg mb-4 text-text">AI工程管理プラン</h3>
                            <p class="font-body text-sm text-text-sub mb-8 flex-grow">天候・資材リスクを加味した工程予測で、遅延を事前に検知しリカバリープランを自動提示。</p>
                            <a href="./services/schedule.html" class="font-h2 text-xs text-accent mt-auto hover:opacity-70 transition-opacity">詳細を見る →</a>
                        </div>
                        <div class="bg-bg border-l-2 border-accent p-8 hover:border-l-4 hover:shadow-sm transition-all duration-300 animate-on-scroll flex flex-col h-full" style="transition-delay: 200ms;">
                            <span class="font-num text-accent mb-4">06.3</span>
                            <h3 class="font-h2 text-lg mb-4 text-text">安全管理デジタル化プラン</h3>
                            <p class="font-body text-sm text-text-sub mb-8 flex-grow">ヒヤリハットデータと現場状況をリアルタイム照合。事故リスクの高い工程を可視化。</p>
                            <a href="./services/safety.html" class="font-h2 text-xs text-accent mt-auto hover:opacity-70 transition-opacity">詳細を見る →</a>
                        </div>
                        <div class="bg-bg border-l-2 border-accent p-8 hover:border-l-4 hover:shadow-sm transition-all duration-300 animate-on-scroll flex flex-col h-full" style="transition-delay: 300ms;">
                            <span class="font-num text-accent mb-4">06.4</span>
                            <h3 class="font-h2 text-lg mb-4 text-text">見積もりAI自動化プラン</h3>
                            <p class="font-body text-sm text-text-sub mb-8 flex-grow">類似案件の積み上げデータを活用し、見積もり作成工数を平均50%削減。</p>
                            <a href="./services/estimate.html" class="font-h2 text-xs text-accent mt-auto hover:opacity-70 transition-opacity">詳細を見る →</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ▼ 追加: 07 / FLOW -->
        <section id="flow" aria-label="導入の流れ" class="py-24 md:py-32 w-full bg-surface border-t border-primary/10">
            <div class="max-w-[1400px] mx-auto px-6 md:px-12 grid grid-cols-12 md:gap-x-8">
                <div class="col-span-12 md:col-span-2 mb-12 md:mb-0 section-num-col">
                    <span class="font-num text-sm text-accent section-num">07 / FLOW</span>
                </div>
                <div class="col-span-12 md:col-span-10">
                    <h2 class="font-h1 text-4xl mb-16 text-text animate-on-scroll">FLOW</h2>
                    
                    <div class="flex flex-col md:flex-row items-center justify-between gap-6 md:gap-4">
                        <!-- Step 1 -->
                        <div class="flex flex-col items-center text-center animate-on-scroll w-full md:w-auto">
                            <span class="font-num text-4xl text-primary mb-2">01</span>
                            <span class="font-h2 text-sm text-text font-bold mb-1">無料相談</span>
                            <span class="font-body text-xs text-text-sub">（30分）</span>
                        </div>
                        <div class="text-accent animate-on-scroll hidden md:block" style="transition-delay: 100ms;">→</div>
                        <div class="text-accent animate-on-scroll md:hidden" style="transition-delay: 100ms;">↓</div>
                        
                        <!-- Step 2 -->
                        <div class="flex flex-col items-center text-center animate-on-scroll w-full md:w-auto" style="transition-delay: 200ms;">
                            <span class="font-num text-4xl text-primary mb-2">02</span>
                            <span class="font-h2 text-sm text-text font-bold mb-1">現場診断</span>
                            <span class="font-body text-xs text-text-sub">（1〜2週間）</span>
                        </div>
                        <div class="text-accent animate-on-scroll hidden md:block" style="transition-delay: 300ms;">→</div>
                        <div class="text-accent animate-on-scroll md:hidden" style="transition-delay: 300ms;">↓</div>

                        <!-- Step 3 -->
                        <div class="flex flex-col items-center text-center animate-on-scroll w-full md:w-auto" style="transition-delay: 400ms;">
                            <span class="font-num text-4xl text-primary mb-2">03</span>
                            <span class="font-h2 text-sm text-text font-bold mb-1">開発・設定</span>
                            <span class="font-body text-xs text-text-sub">（4〜8週間）</span>
                        </div>
                        <div class="text-accent animate-on-scroll hidden md:block" style="transition-delay: 500ms;">→</div>
                        <div class="text-accent animate-on-scroll md:hidden" style="transition-delay: 500ms;">↓</div>

                        <!-- Step 4 -->
                        <div class="flex flex-col items-center text-center animate-on-scroll w-full md:w-auto" style="transition-delay: 600ms;">
                            <span class="font-num text-4xl text-primary mb-2">04</span>
                            <span class="font-h2 text-sm text-text font-bold mb-1">研修・導入</span>
                            <span class="font-body text-xs text-text-sub">（1〜2週間）</span>
                        </div>
                        <div class="text-accent animate-on-scroll hidden md:block" style="transition-delay: 700ms;">→</div>
                        <div class="text-accent animate-on-scroll md:hidden" style="transition-delay: 700ms;">↓</div>

                        <!-- Step 5 -->
                        <div class="flex flex-col items-center text-center animate-on-scroll w-full md:w-auto" style="transition-delay: 800ms;">
                            <span class="font-num text-4xl text-primary mb-2">05</span>
                            <span class="font-h2 text-sm text-text font-bold mb-1">運用サポート</span>
                            <span class="font-body text-xs text-text-sub">（継続）</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ▼ 追加: 08 / FAQ -->
        <section id="faq" aria-label="よくある質問" class="py-24 md:py-32 w-full">
            <div class="max-w-[1400px] mx-auto px-6 md:px-12 grid grid-cols-12 md:gap-x-8">
                <div class="col-span-12 md:col-span-2 mb-12 md:mb-0 section-num-col">
                    <span class="font-num text-sm text-accent section-num">08 / FAQ</span>
                </div>
                <div class="col-span-12 md:col-span-10">
                    <h2 class="font-h1 text-4xl mb-16 text-text animate-on-scroll">FAQ</h2>
                    
                    <div class="flex flex-col animate-on-scroll">
                        <!-- FAQ 1 -->
                        <div class="border-b border-text/10 overflow-hidden">
                            <button class="faq-btn w-full text-left py-6 flex justify-between items-center focus:outline-none" aria-expanded="false" aria-controls="faq-content-1">
                                <span class="font-h2 text-base text-text">Q1: ITが苦手でも使いこなせますか？</span>
                                <span class="text-text font-h2 text-xl transform transition-transform duration-300 faq-icon">+</span>
                            </button>
                            <div id="faq-content-1" class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out" role="region">
                                <p class="font-body text-sm text-text-sub pb-6">A1: はい。UIは現場スタッフが直感的に使えるよう設計されており、導入後の研修サポートも含まれています。PCやスマートフォンの基本操作ができれば問題ありません。</p>
                            </div>
                        </div>
                        
                        <!-- FAQ 2 -->
                        <div class="border-b border-text/10 overflow-hidden">
                            <button class="faq-btn w-full text-left py-6 flex justify-between items-center focus:outline-none" aria-expanded="false" aria-controls="faq-content-2">
                                <span class="font-h2 text-base text-text">Q2: 費用の目安を教えてください。</span>
                                <span class="text-text font-h2 text-xl transform transition-transform duration-300 faq-icon">+</span>
                            </button>
                            <div id="faq-content-2" class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out" role="region">
                                <p class="font-body text-sm text-text-sub pb-6">A2: 企業規模や導入範囲によって異なりますが、初期費用50万円〜、月額サポート5万円〜を目安にご提案しています。まずは無料相談でお気軽にご確認ください。</p>
                            </div>
                        </div>

                        <!-- FAQ 3 -->
                        <div class="border-b border-text/10 overflow-hidden">
                            <button class="faq-btn w-full text-left py-6 flex justify-between items-center focus:outline-none" aria-expanded="false" aria-controls="faq-content-3">
                                <span class="font-h2 text-base text-text">Q3: 既存のシステムや帳票と連携できますか？</span>
                                <span class="text-text font-h2 text-xl transform transition-transform duration-300 faq-icon">+</span>
                            </button>
                            <div id="faq-content-3" class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out" role="region">
                                <p class="font-body text-sm text-text-sub pb-6">A3: kintone・Excel・PDF帳票など主要フォーマットに対応しています。既存のデータフローをそのまま活用し、新たな入力作業を最小限に抑えます。</p>
                            </div>
                        </div>

                        <!-- FAQ 4 -->
                        <div class="border-b border-text/10 overflow-hidden">
                            <button class="faq-btn w-full text-left py-6 flex justify-between items-center focus:outline-none" aria-expanded="false" aria-controls="faq-content-4">
                                <span class="font-h2 text-base text-text">Q4: 何人規模の会社から対応していただけますか？</span>
                                <span class="text-text font-h2 text-xl transform transition-transform duration-300 faq-icon">+</span>
                            </button>
                            <div id="faq-content-4" class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out" role="region">
                                <p class="font-body text-sm text-text-sub pb-6">A4: 従業員5名の小規模事業者から対応しています。中小建設会社の現場実態に即したプランをご用意していますので、規模を問わずご相談ください。</p>
                            </div>
                        </div>

                        <!-- FAQ 5 -->
                        <div class="border-b border-text/10 overflow-hidden">
                            <button class="faq-btn w-full text-left py-6 flex justify-between items-center focus:outline-none" aria-expanded="false" aria-controls="faq-content-5">
                                <span class="font-h2 text-base text-text">Q5: 導入から稼働まで何ヶ月かかりますか？</span>
                                <span class="text-text font-h2 text-xl transform transition-transform duration-300 faq-icon">+</span>
                            </button>
                            <div id="faq-content-5" class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out" role="region">
                                <p class="font-body text-sm text-text-sub pb-6">A5: 標準的なプランで2〜3ヶ月が目安です。現場の繁忙期を避けた柔軟なスケジュール調整も可能です。</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ▼ 追加: 09 / DIAGNOSIS -->
        <section id="diagnosis" aria-label="AI導入レベル診断" class="py-24 md:py-32 w-full bg-primary text-surface">
            <div class="max-w-[1400px] mx-auto px-6 md:px-12 grid grid-cols-12 md:gap-x-8">
                <div class="col-span-12 md:col-span-2 mb-12 md:mb-0 section-num-col">
                    <span class="font-num text-sm text-accent section-num">09 / DIAGNOSIS</span>
                </div>
                <div class="col-span-12 md:col-span-10">
                    <h2 class="font-h1 text-4xl mb-6 text-surface animate-on-scroll">AI LEVEL DIAGNOSIS</h2>
                    <p class="font-body text-surface/80 mb-12 animate-on-scroll">5つの質問で、貴社に最適なAI導入ロードマップを診断します。（無料）</p>

                    <div id="quiz-container" class="bg-surface text-text p-8 md:p-12 animate-on-scroll relative min-h-[300px] md:min-h-[400px]">
                        <!-- Progress Bar -->
                        <div id="quiz-progress-bar" class="absolute top-0 left-0 h-2 bg-accent transition-all duration-300" style="width: 20%;"></div>
                        <div class="text-right font-num text-accent text-sm mb-6" id="quiz-progress-text">1/5</div>
                        
                        <!-- Question Area -->
                        <div id="quiz-question-area">
                            <h3 id="quiz-question" class="font-h2 text-xl mb-8 leading-relaxed"></h3>
                            <div id="quiz-options" class="flex flex-col gap-4">
                                <!-- Options injected via JS -->
                            </div>
                            <div class="mt-8 text-right hidden" id="quiz-next-container">
                                <button id="quiz-next-btn" class="inline-flex justify-center items-center px-8 py-3 bg-text text-surface font-h2 text-sm tracking-widest hover:bg-accent transition-colors">次へ →</button>
                            </div>
                        </div>

                        <!-- Result Area -->
                        <div id="quiz-result-area" class="hidden text-center py-8">
                            <div class="font-num text-accent text-2xl mb-2">SCORE <span id="quiz-score"></span>/10</div>
                            <h3 id="quiz-result-title" class="font-h2 text-2xl md:text-3xl mb-6 text-primary"></h3>
                            <p id="quiz-result-desc" class="font-body text-text-sub mb-10 max-w-2xl mx-auto leading-relaxed"></p>
                            <a href="./contact/index.html" class="inline-flex justify-center items-center px-10 py-4 bg-accent text-surface font-h2 text-sm tracking-widest hover:bg-primary transition-colors">
                                無料相談を予約する
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- COMPANY (10) -->"""

content = content.replace(cases_end, new_sections, 1)

# Renumber COMPANY 05 -> 10
content = content.replace("05 / COMPANY", "10 / COMPANY", 1)
content = content.replace("<!-- COMPANY (05) -->", "<!-- COMPANY (10) -->", 1)

# 8. Footer CTA inline + Footer inline
footer_placeholder = """    <div id="cta-component"></div>
    <div id="footer"></div>"""

footer_full = """    <!-- ▼ 追加: E CTAセクション -->
    <section class="w-full bg-primary text-surface py-32 text-center" aria-label="お問い合わせ">
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 animate-on-scroll">
            <h2 class="font-h1 text-3xl md:text-5xl mb-6 tracking-tight">建設現場のAI化、まず話を聞かせてください。</h2>
            <p class="font-body text-surface/80 max-w-2xl mx-auto mb-12">初回相談は無料。現場の課題をお聞きし、御社に合ったロードマップをご提案します。</p>
            <div class="flex flex-col sm:flex-row justify-center gap-6">
                <a href="./contact/index.html" class="inline-flex justify-center items-center px-10 py-4 bg-accent text-surface font-h2 text-sm tracking-widest hover:bg-surface hover:text-primary transition-colors">
                    無料相談を予約する
                </a>
                <a href="./download/index.html" class="inline-flex justify-center items-center px-10 py-4 border border-surface/30 text-surface font-h2 text-sm tracking-widest hover:bg-surface hover:text-primary transition-colors">
                    資料をダウンロード
                </a>
            </div>
        </div>
    </section>

    <!-- ▼ 追加: F フッター（インライン化） -->
    <footer class="bg-primary pt-24 pb-12 w-full text-surface z-10 relative">
        <div class="max-w-[1400px] mx-auto px-6 md:px-12">
            <div class="grid grid-cols-12 gap-y-12 md:gap-x-8">
                <!-- Left Info -->
                <div class="col-span-12 md:col-span-6 lg:col-span-5">
                    <a href="./index.html" class="flex items-center space-x-2 no-underline text-surface mb-8">
                        <span class="font-h1 font-bold text-2xl tracking-tighter">BUILDTECH<span
                                class="text-accent">AI</span></span>
                    </a>
                    <p class="font-body text-sm text-surface/80 leading-loose max-w-sm mb-8">
                        建設現場の経験値を、データに変える。<br>
                        中小建設会社に特化したAI導入コンサルティング。
                    </p>
                    <div class="font-h2 text-sm text-surface/60">
                        <p>TOKYO, JAPAN</p>
                    </div>
                </div>

                <!-- Empty Spacer or additional col -->
                <div class="col-span-12 md:col-span-1 lg:col-span-3"></div>

                <!-- Links -->
                <div class="col-span-12 md:col-span-5 lg:col-span-4 grid grid-cols-2 gap-8 font-h2 text-sm">
                    <ul class="space-y-4">
                        <li><a href="./index.html" class="text-surface/80 hover:text-accent transition-colors">00_HOME</a>
                        </li>
                        <li><a href="./about/index.html"
                                class="text-surface/80 hover:text-accent transition-colors">01_ABOUT</a></li>
                        <li><a href="./cases/index.html"
                                class="text-surface/80 hover:text-accent transition-colors">02_CASES</a></li>
                    </ul>
                    <ul class="space-y-4">
                        <li><a href="./contact/index.html"
                                class="text-surface/80 hover:text-accent transition-colors">CONTACT</a></li>
                        <li><a href="#" class="text-surface/80 hover:text-accent transition-colors">PRIVACY POLICY</a></li>
                    </ul>
                </div>
            </div>

            <div
                class="mt-24 pt-8 border-t border-surface/20 flex flex-col md:flex-row justify-between items-center font-h2 text-xs text-surface/50">
                <p>&copy; 2026 BuildTech AI. ALL RIGHTS RESERVED.</p>
                <p class="mt-4 md:mt-0">DESIGNED FOR CONSTRUCTION</p>
            </div>
        </div>
    </footer>

    <!-- ▼ 追加: D-1 フローティングCTA -->
    <a href="./contact/index.html" id="float-cta" 
       class="bg-accent text-surface px-6 py-3 font-h2 text-sm tracking-widest shadow-lg hover:bg-primary transition-colors"
       style="position:fixed; bottom:2rem; right:2rem; z-index:50; display:none; opacity:0; transition: opacity 0.3s ease;">
      無料相談
    </a>
"""

content = content.replace(footer_placeholder, footer_full, 1)

# 9. JS Script logic replacement
script_marker_start = """    <script>
        // Load global components
        async function loadComponent"""
script_marker_end = """        window.toggleMenu = function () {
            const menu = document.getElementById('mobile-menu');
            if (menu) {
                menu.classList.toggle('hidden');
            }
        }
    </script>"""

# Using regex to replace the entire old script block
import re

new_script = """    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Intersection Observer Setup
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

            // Count Up logic
            const countObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const target = entry.target;
                        const endValue = parseInt(target.getAttribute('data-target'), 10);
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
            
            // Active Navigation Link
            const sections = document.querySelectorAll('section[id]');
            const navItems = document.querySelectorAll('.nav-item');
            
            const navObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if(entry.isIntersecting) {
                        const id = entry.target.getAttribute('id');
                        navItems.forEach(item => {
                            if(item.getAttribute('href') === '#' + id) {
                                item.classList.add('text-accent');
                                item.classList.remove('text-text-sub', 'text-text');
                            } else {
                                item.classList.remove('text-accent');
                                item.classList.add('text-text-sub');
                            }
                        });
                    }
                });
            }, { threshold: 0.3, rootMargin: "-10% 0px -80% 0px" });
            
            sections.forEach(sec => navObserver.observe(sec));
        });

        // Header scroll behavior
        window.addEventListener('scroll', () => {
            const header = document.getElementById('main-header');
            if (header && window.scrollY > 50) {
                header.style.backgroundColor = 'rgba(245,247,250,0.95)';
                header.style.backdropFilter = 'blur(8px)';
                header.classList.add('shadow-sm');
                header.classList.remove('py-4');
                header.classList.add('py-2');
            } else if (header) {
                header.style.backgroundColor = 'transparent';
                header.style.backdropFilter = 'none';
                header.classList.remove('shadow-sm');
                header.classList.add('py-4');
                header.classList.remove('py-2');
            }
        });

        // Scroll progress bar
        window.addEventListener('scroll', () => {
            const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (winScroll / height) * 100;
            const progressBar = document.getElementById('scroll-progress');
            if(progressBar) progressBar.style.width = scrolled + '%';
        });

        // Floating CTA
        window.addEventListener('scroll', () => {
            const floatCta = document.getElementById('float-cta');
            if (floatCta) {
                if (window.scrollY > 200) {
                    floatCta.style.display = 'block';
                    setTimeout(() => { floatCta.style.opacity = '1'; }, 10);
                } else {
                    floatCta.style.opacity = '0';
                    setTimeout(() => { 
                        if (window.scrollY <= 200) floatCta.style.display = 'none'; 
                    }, 300);
                }
            }
        });

        // Typewriter animation
        const typewriterWords = ["工程管理をAIが最適化", "安全管理をデータで可視化", "見積もり作業を50%削減", "暗黙知を会社の資産に変える"];
        const typewriterEl = document.getElementById('typewriter-text');
        let currentWordIndex = 0;

        function updateTypewriter() {
            if(!typewriterEl) return;
            typewriterEl.style.opacity = 0;
            setTimeout(() => {
                typewriterEl.textContent = typewriterWords[currentWordIndex];
                typewriterEl.style.opacity = 1;
                currentWordIndex = (currentWordIndex + 1) % typewriterWords.length;
            }, 500);
        }
        
        if (typewriterEl) {
            updateTypewriter();
            setInterval(updateTypewriter, 2500);
        }

        // Mobile Menu toggle
        function toggleMobileMenu() {
            const menu = document.getElementById('mobile-menu-overlay');
            if (menu.classList.contains('hidden')) {
                menu.classList.remove('hidden');
                menu.classList.add('flex');
            } else {
                menu.classList.add('hidden');
                menu.classList.remove('flex');
            }
        }

        // FAQ Accordion
        document.querySelectorAll('.faq-btn').forEach(button => {
            button.addEventListener('click', () => {
                const expanded = button.getAttribute('aria-expanded') === 'true';
                const contentId = button.getAttribute('aria-controls');
                const content = document.getElementById(contentId);
                const icon = button.querySelector('.faq-icon');

                // Close all other FAQs
                document.querySelectorAll('.faq-btn').forEach(otherBtn => {
                    if (otherBtn !== button) {
                        otherBtn.setAttribute('aria-expanded', 'false');
                        otherBtn.querySelector('.faq-icon').textContent = '+';
                        const otherContent = document.getElementById(otherBtn.getAttribute('aria-controls'));
                        if(otherContent) otherContent.style.maxHeight = '0px';
                    }
                });

                // Toggle current FAQ
                if (expanded) {
                    button.setAttribute('aria-expanded', 'false');
                    icon.textContent = '+';
                    content.style.maxHeight = '0px';
                } else {
                    button.setAttribute('aria-expanded', 'true');
                    icon.textContent = '-';
                    content.style.maxHeight = content.scrollHeight + 'px';
                }
            });
        });
    </script>
    <script defer>
        // Diagnosis Quiz
        const quizData = [
            {
                q: "Q1: 日報や工程表はデジタル（Excel・アプリ等）で管理していますか？",
                opts: [
                    { t: "A: はい", score: 2 },
                    { t: "B: 一部だけ", score: 1 },
                    { t: "C: すべて紙", score: 0 }
                ]
            },
            {
                q: "Q2: 過去の工事データを見積もりや計画に活用していますか？",
                opts: [
                    { t: "A: 積極的に活用", score: 2 },
                    { t: "B: たまに参照", score: 1 },
                    { t: "C: ほぼ活用していない", score: 0 }
                ]
            },
            {
                q: "Q3: 工期の遅れが発生した場合、原因を後から分析できますか？",
                opts: [
                    { t: "A: データで分析できる", score: 2 },
                    { t: "B: 記憶や経験で大まかに", score: 1 },
                    { t: "C: 難しい", score: 0 }
                ]
            },
            {
                q: "Q4: 若手への技術継承の仕組みはありますか？",
                opts: [
                    { t: "A: マニュアル・システムがある", score: 2 },
                    { t: "B: 口頭・OJTのみ", score: 1 },
                    { t: "C: ほぼ個人任せ", score: 0 }
                ]
            },
            {
                q: "Q5: AIやDXに取り組みたいが、何から始めるかわからない状態ですか？",
                opts: [
                    { t: "A: 既に取り組んでいる", score: 2 },
                    { t: "B: 検討中", score: 1 },
                    { t: "C: 全くわからない", score: 0 }
                ]
            }
        ];

        let currentQIndex = 0;
        let totalScore = 0;
        let selectedScore = null;

        function renderQuiz() {
            if (currentQIndex >= quizData.length) {
                showQuizResult();
                return;
            }
            
            const qData = quizData[currentQIndex];
            const qEl = document.getElementById('quiz-question');
            if(!qEl) return;
            qEl.innerText = qData.q;
            document.getElementById('quiz-progress-text').innerText = `${currentQIndex + 1}/${quizData.length}`;
            document.getElementById('quiz-progress-bar').style.width = `${((currentQIndex + 1) / quizData.length) * 100}%`;
            
            const optionsContainer = document.getElementById('quiz-options');
            optionsContainer.innerHTML = '';
            selectedScore = null;
            document.getElementById('quiz-next-container').classList.add('hidden');

            qData.opts.forEach((opt, idx) => {
                const btn = document.createElement('button');
                btn.className = 'quiz-opt-btn w-full text-left p-4 border border-text/20 font-body text-sm hover:border-accent transition-colors';
                btn.innerText = opt.t;
                btn.onclick = () => {
                    document.querySelectorAll('.quiz-opt-btn').forEach(b => {
                        b.classList.remove('bg-accent', 'text-surface', 'border-accent');
                    });
                    btn.classList.add('bg-accent', 'text-surface', 'border-accent');
                    selectedScore = opt.score;
                    document.getElementById('quiz-next-container').classList.remove('hidden');
                };
                optionsContainer.appendChild(btn);
            });
        }

        document.getElementById('quiz-next-btn')?.addEventListener('click', () => {
            if(selectedScore !== null) {
                totalScore += selectedScore;
                currentQIndex++;
                renderQuiz();
            }
        });

        function showQuizResult() {
            document.getElementById('quiz-question-area').classList.add('hidden');
            document.getElementById('quiz-result-area').classList.remove('hidden');
            document.getElementById('quiz-score').innerText = totalScore;
            
            let title = '';
            let desc = '';
            
            if (totalScore <= 3) {
                title = 'AI導入スタート段階';
                desc = '現場データの整理から始めましょう。無料相談でロードマップを作成します。';
            } else if (totalScore <= 7) {
                title = 'AI活用準備段階';
                desc = 'データ基盤が整いつつあります。工程管理AIの導入で大きな成果が出やすい段階です。';
            } else {
                title = 'AI最適化段階';
                desc = '貴社のデータ資産を最大活用できます。カスタム開発のご提案が可能です。';
            }
            
            document.getElementById('quiz-result-title').innerText = title;
            document.getElementById('quiz-result-desc').innerText = desc;
        }

        renderQuiz();
    </script>"""

content = re.sub(r'    <script>.*?    </script>', new_script, content, flags=re.DOTALL)

with open('/Users/hk/Desktop/hp_test/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
