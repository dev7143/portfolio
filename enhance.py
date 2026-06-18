import re

with open('D:\\steam\\桌面\\个人作品集\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ===== 1. ENHANCE HERO with industrial SVG decor =====
hero_add = '''    <div class="hero-enhance-svg">
        <svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" opacity="0.07">
            <path d="M40 300 L120 300 L140 280 L200 280 L220 300 L280 300" stroke="#6ab0ff" stroke-width="1.5" fill="none" opacity="0.6"/>
            <path d="M40 320 L100 320 L120 340 L200 340 L220 320 L280 320" stroke="#6ab0ff" stroke-width="1" fill="none" opacity="0.4"/>
            <path d="M40 340 L80 340 L100 360 L200 360" stroke="#6ab0ff" stroke-width="1" fill="none" opacity="0.3"/>
            <circle cx="280" cy="300" r="3" fill="#6ab0ff" opacity="0.5"/>
            <circle cx="280" cy="320" r="2" fill="#6ab0ff" opacity="0.5"/>
            <path d="M1160 200 L1240 200 L1260 220 L1320 220 L1340 200 L1400 200" stroke="#6ab0ff" stroke-width="1.5" fill="none" opacity="0.6"/>
            <path d="M1160 220 L1220 220 L1240 240 L1320 240 L1340 220 L1400 220" stroke="#6ab0ff" stroke-width="1" fill="none" opacity="0.4"/>
            <path d="M1160 240 L1200 240 L1220 260 L1320 260" stroke="#6ab0ff" stroke-width="1" fill="none" opacity="0.3"/>
            <circle cx="1160" cy="200" r="3" fill="#6ab0ff" opacity="0.5"/>
            <circle cx="1160" cy="220" r="2" fill="#6ab0ff" opacity="0.5"/>
            <path d="M80 580 Q120 520 160 580 Q200 640 240 580 Q280 520 320 580 Q360 640 400 580" stroke="#6ab0ff" stroke-width="1" fill="none" opacity="0.3"/>
            <path d="M1040 620 Q1080 560 1120 620 Q1160 680 1200 620 Q1240 560 1280 620 Q1320 680 1360 620" stroke="#6ab0ff" stroke-width="1" fill="none" opacity="0.25"/>
            <g transform="translate(100,680) scale(0.8)" opacity="0.4">
                <circle cx="0" cy="0" r="40" fill="none" stroke="#6ab0ff" stroke-width="1"/>
                <circle cx="0" cy="0" r="25" fill="none" stroke="#6ab0ff" stroke-width="0.8"/>
                <circle cx="0" cy="0" r="8" fill="none" stroke="#6ab0ff" stroke-width="0.8"/>
                <line x1="0" y1="-40" x2="0" y2="-48" stroke="#6ab0ff" stroke-width="1.5"/><line x1="0" y1="40" x2="0" y2="48" stroke="#6ab0ff" stroke-width="1.5"/>
                <line x1="-40" y1="0" x2="-48" y2="0" stroke="#6ab0ff" stroke-width="1.5"/><line x1="40" y1="0" x2="48" y2="0" stroke="#6ab0ff" stroke-width="1.5"/>
                <line x1="-28" y1="-28" x2="-34" y2="-34" stroke="#6ab0ff" stroke-width="1.5"/>
                <line x1="28" y1="28" x2="34" y2="34" stroke="#6ab0ff" stroke-width="1.5"/>
                <line x1="-28" y1="28" x2="-34" y2="34" stroke="#6ab0ff" stroke-width="1.5"/>
                <line x1="28" y1="-28" x2="34" y2="-34" stroke="#6ab0ff" stroke-width="1.5"/>
            </g>
            <g transform="translate(1340,100) scale(0.6)" opacity="0.3">
                <circle cx="0" cy="0" r="40" fill="none" stroke="#6ab0ff" stroke-width="1"/>
                <circle cx="0" cy="0" r="25" fill="none" stroke="#6ab0ff" stroke-width="0.8"/>
                <circle cx="0" cy="0" r="8" fill="none" stroke="#6ab0ff" stroke-width="0.8"/>
                <line x1="0" y1="-40" x2="0" y2="-48" stroke="#6ab0ff" stroke-width="1.5"/><line x1="0" y1="40" x2="0" y2="48" stroke="#6ab0ff" stroke-width="1.5"/>
                <line x1="-40" y1="0" x2="-48" y2="0" stroke="#6ab0ff" stroke-width="1.5"/><line x1="40" y1="0" x2="48" y2="0" stroke="#6ab0ff" stroke-width="1.5"/>
                <line x1="-28" y1="-28" x2="-34" y2="-34" stroke="#6ab0ff" stroke-width="1.5"/>
                <line x1="28" y1="28" x2="34" y2="34" stroke="#6ab0ff" stroke-width="1.5"/>
                <line x1="-28" y1="28" x2="-34" y2="34" stroke="#6ab0ff" stroke-width="1.5"/>
                <line x1="28" y1="-28" x2="34" y2="-34" stroke="#6ab0ff" stroke-width="1.5"/>
            </g>
            <g transform="translate(1250,480) scale(0.7)" opacity="0.4">
                <rect x="-30" y="-30" width="60" height="60" rx="4" fill="none" stroke="#6ab0ff" stroke-width="1"/>
                <rect x="-20" y="-20" width="40" height="40" rx="2" fill="none" stroke="#6ab0ff" stroke-width="0.8"/>
                <rect x="-10" y="-10" width="20" height="20" rx="1" fill="none" stroke="#6ab0ff" stroke-width="0.6"/>
                <line x1="-30" y1="-15" x2="-38" y2="-15" stroke="#6ab0ff" stroke-width="1"/>
                <line x1="-30" y1="0" x2="-38" y2="0" stroke="#6ab0ff" stroke-width="1"/>
                <line x1="-30" y1="15" x2="-38" y2="15" stroke="#6ab0ff" stroke-width="1"/>
                <line x1="30" y1="-15" x2="38" y2="-15" stroke="#6ab0ff" stroke-width="1"/>
                <line x1="30" y1="0" x2="38" y2="0" stroke="#6ab0ff" stroke-width="1"/>
                <line x1="30" y1="15" x2="38" y2="15" stroke="#6ab0ff" stroke-width="1"/>
                <line x1="-15" y1="-30" x2="-15" y2="-38" stroke="#6ab0ff" stroke-width="1"/>
                <line x1="0" y1="-30" x2="0" y2="-38" stroke="#6ab0ff" stroke-width="1"/>
                <line x1="15" y1="-30" x2="15" y2="-38" stroke="#6ab0ff" stroke-width="1"/>
                <line x1="-15" y1="30" x2="-15" y2="38" stroke="#6ab0ff" stroke-width="1"/>
                <line x1="0" y1="30" x2="0" y2="38" stroke="#6ab0ff" stroke-width="1"/>
                <line x1="15" y1="30" x2="15" y2="38" stroke="#6ab0ff" stroke-width="1"/>
            </g>
            <circle cx="200" cy="200" r="1.5" fill="#6ab0ff" opacity="0.4"/>
            <circle cx="350" cy="150" r="1" fill="#6ab0ff" opacity="0.3"/>
            <circle cx="1100" cy="300" r="1.5" fill="#6ab0ff" opacity="0.4"/>
            <circle cx="1300" cy="350" r="1" fill="#6ab0ff" opacity="0.3"/>
            <circle cx="150" cy="500" r="1.5" fill="#6ab0ff" opacity="0.3"/>
            <circle cx="1200" cy="550" r="1.5" fill="#6ab0ff" opacity="0.3"/>
            <circle cx="620" cy="200" r="4" fill="#6ab0ff" opacity="0.15"/>
            <circle cx="820" cy="180" r="3" fill="#6ab0ff" opacity="0.12"/>
            <circle cx="720" cy="700" r="3.5" fill="#6ab0ff" opacity="0.12"/>
        </svg>
    </div>
    <div class="hero-glow hero-glow-1"></div>
    <div class="hero-glow hero-glow-2"></div>'''

old = '<div class="hero-shapes"><div class="hero-shape"></div><div class="hero-shape"></div><div class="hero-shape"></div><div class="hero-shape"></div><div class="hero-shape"></div></div>'
content = content.replace(old, old + hero_add)

# ===== 2. ADD SKILLS SECTION =====
skills = '''<section class="section" id="skills" style="background:#fff;padding-top:60px;padding-bottom:40px">
    <div class="section-inner">
        <div class="section-header" style="margin-bottom:28px">
            <p class="section-label">Skills &amp; Tools</p>
            <h2 class="section-title"><span class="num">&#x2699;</span> 技术专长</h2>
        </div>
        <div class="reveal">
            <div class="about-section">
                <div class="about-text">
                    <p style="margin-bottom:16px">熟悉西门子 S7-1200 PLC 编程开发，掌握 <strong>SCL（结构化文本）</strong>与 <strong>LAD（梯形图）</strong>两种编程语言。具备从 IO 地址分配、硬件组态、程序编写到系统联调的全流程项目经验。</p>
                    <p style="margin-bottom:16px">熟练使用 <strong>Factory IO</strong> 3D 工业仿真平台进行虚拟调试，能够快速搭建产线场景并实现 PLC 实时联动控制。</p>
                    <p>对步进/伺服驱动控制、变频器通信（USS/Modbus）、模拟量采集与PID调节有深入理解。</p>
                </div>
                <div class="about-stats">
                    <div class="about-stat-card"><div class="about-stat-icon">&#x1F4E1;</div><div class="about-stat-num">SCL</div><div class="about-stat-label">结构化文本</div></div>
                    <div class="about-stat-card"><div class="about-stat-icon">&#x1F4C8;</div><div class="about-stat-num">LAD</div><div class="about-stat-label">梯形图</div></div>
                    <div class="about-stat-card"><div class="about-stat-icon">&#x1F3ED;</div><div class="about-stat-num">Factory IO</div><div class="about-stat-label">3D 仿真</div></div>
                    <div class="about-stat-card"><div class="about-stat-icon">&#x2699;&#xFE0F;</div><div class="about-stat-num">驱动控制</div><div class="about-stat-label">步进/伺服/变频</div></div>
                </div>
            </div>
            <div class="skills-grid" style="margin-top:28px">
                <div class="skill-card"><div class="skill-card-icon">&#x1F4F6;</div><div class="skill-card-label">S7-1200</div><div class="skill-card-desc">西门子 PLC</div></div>
                <div class="skill-card"><div class="skill-card-icon">&#x1F4DD;</div><div class="skill-card-label">SCL / LAD</div><div class="skill-card-desc">编程语言</div></div>
                <div class="skill-card"><div class="skill-card-icon">&#x1F3C6;</div><div class="skill-card-label">Factory IO</div><div class="skill-card-desc">3D 仿真平台</div></div>
                <div class="skill-card"><div class="skill-card-icon">&#x1F527;</div><div class="skill-card-label">步进/伺服</div><div class="skill-card-desc">驱动控制系统</div></div>
                <div class="skill-card"><div class="skill-card-icon">&#x1F4CA;</div><div class="skill-card-label">变频通信</div><div class="skill-card-desc">USS / Modbus</div></div>
                <div class="skill-card"><div class="skill-card-icon">&#x1F3C1;</div><div class="skill-card-label">模拟量 PID</div><div class="skill-card-desc">温度/压力控制</div></div>
            </div>
        </div>
    </div>
</section>'''

content = content.replace(
    '</section>\n<section class="section" id="project1">',
    '</section>\n' + skills + '\n<section class="section" id="project1">'
)

# ===== 3. SECTION DIVIDERS =====
div1 = '''\n<div class="section-divider">
    <div class="section-divider-inner">
        <svg viewBox="0 0 200 40" xmlns="http://www.w3.org/2000/svg">
            <line x1="0" y1="20" x2="60" y2="20" stroke="#2d7dd2" stroke-width="1" stroke-dasharray="4 4"/>
            <circle cx="80" cy="20" r="4" fill="#2d7dd2" opacity="0.3"/>
            <circle cx="100" cy="20" r="6" fill="#2d7dd2" opacity="0.15"/>
            <circle cx="100" cy="20" r="2" fill="#2d7dd2" opacity="0.5"/>
            <circle cx="120" cy="20" r="4" fill="#2d7dd2" opacity="0.3"/>
            <line x1="140" y1="20" x2="200" y2="20" stroke="#2d7dd2" stroke-width="1" stroke-dasharray="4 4"/>
        </svg>
    </div>
</div>\n'''

div2 = '''\n<div class="section-divider section-divider-alt">
    <div class="section-divider-inner">
        <svg viewBox="0 0 200 40" xmlns="http://www.w3.org/2000/svg">
            <line x1="0" y1="20" x2="60" y2="20" stroke="#2d7dd2" stroke-width="1" stroke-dasharray="4 4"/>
            <rect x="78" y="15" width="8" height="10" rx="1" fill="#2d7dd2" opacity="0.2"/>
            <rect x="92" y="12" width="16" height="16" rx="2" fill="#2d7dd2" opacity="0.1"/>
            <rect x="94" y="14" width="12" height="12" rx="1" fill="#2d7dd2" opacity="0.25"/>
            <rect x="114" y="15" width="8" height="10" rx="1" fill="#2d7dd2" opacity="0.2"/>
            <line x1="140" y1="20" x2="200" y2="20" stroke="#2d7dd2" stroke-width="1" stroke-dasharray="4 4"/>
        </svg>
    </div>
</div>\n'''

content = content.replace('</section>\n<section class="section section-alt" id="project2">', '</section>' + div1 + '<section class="section section-alt" id="project2">')
content = content.replace('</section>\n<section class="section" id="project3">', '</section>' + div2 + '<section class="section" id="project3">')
content = content.replace('</section>\n<section class="section section-alt" id="project4">', '</section>' + div1 + '<section class="section section-alt" id="project4">')
content = content.replace('</section>\n<section class="section" id="project5">', '</section>' + div2 + '<section class="section" id="project5">')

# ===== 4. FOOTER CIRCUIT =====
footer_svg = '''    <div class="footer-circuit">
        <svg viewBox="0 0 600 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
            <path d="M0 60 L50 60 L60 50 L90 50 L100 60 L140 60" stroke="#6ab0ff" stroke-width="1" fill="none"/>
            <path d="M0 70 L40 70 L50 80 L90 80 L100 70 L140 70" stroke="#6ab0ff" stroke-width="0.8" fill="none"/>
            <circle cx="140" cy="60" r="2" fill="#6ab0ff"/>
            <circle cx="140" cy="70" r="1.5" fill="#6ab0ff"/>
            <path d="M460 200 L500 200 L510 210 L550 210 L560 200 L600 200" stroke="#6ab0ff" stroke-width="1" fill="none"/>
            <path d="M460 210 L490 210 L500 220 L550 220 L560 210 L600 210" stroke="#6ab0ff" stroke-width="0.8" fill="none"/>
            <circle cx="460" cy="200" r="2" fill="#6ab0ff"/>
            <circle cx="460" cy="210" r="1.5" fill="#6ab0ff"/>
            <path d="M200 240 Q220 220 240 240 Q260 260 280 240" stroke="#6ab0ff" stroke-width="0.8" fill="none" opacity="0.5"/>
            <path d="M320 60 Q340 40 360 60 Q380 80 400 60" stroke="#6ab0ff" stroke-width="0.8" fill="none" opacity="0.5"/>
        </svg>
    </div>
'''

content = content.replace(
    '<footer class="footer" id="contact">\n    <div class="footer-inner">',
    '<footer class="footer" id="contact">\n' + footer_svg + '    <div class="footer-inner">'
)

with open('D:\\steam\\桌面\\个人作品集\\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('SUCCESS: All enhancements applied')
