import re

def clean_b64(val):
    val = val.strip()
    if "," in val and val.startswith("data:image"):
        return val.split(",", 1)[1]
    return val

with open("avatar_thu_b64.txt", "r") as f:
    avatar_thu_b64 = clean_b64(f.read())

with open("avatar_3x4_b64.txt", "r") as f:
    avatar_oliver_b64 = clean_b64(f.read())

with open("qr_oliver_b64.txt", "r") as f:
    qr_oliver_b64 = clean_b64(f.read())

with open("yspace_logo_b64.txt", "r") as f:
    yspace_logo_b64 = clean_b64(f.read())

with open("export_back.html", "r", encoding="utf-8") as f:
    back_html_content = f.read()

# Extract back card article
back_match = re.search(r'(<article id="card-back-view"[\s\S]*?</article>)', back_html_content)
back_article = back_match.group(1)

with open("export_front_thu_vi.html", "r", encoding="utf-8") as f:
    thu_front_content = f.read()

# Extract front card article
front_match = re.search(r'(<article id="card-front-view"[\s\S]*?</article>)', thu_front_content)
front_article = front_match.group(1)

# Ensure ID hooks and default to Oliver Nguyen with Lark QR
# 1. Avatar img hook
front_article = re.sub(
    r'<img id="card-avatar"\s+src="data:image/jpeg;base64,[^"]+"\s+alt="[^"]*"\s+class="([^"]*)"\s*/>',
    f'<img id="card-avatar" src="data:image/jpeg;base64,{avatar_oliver_b64}" alt="Oliver Nguyen" class="\\1" />',
    front_article,
    count=1
)

# 2. Name hook
front_article = re.sub(
    r'<h2 id="display-name"[^>]*>[\s\S]*?</h2>',
    '<h2 id="display-name" class="text-[13.5px] font-black tracking-tight text-white leading-none">Oliver Nguyen</h2>',
    front_article
)

# 3. Phone hook
front_article = re.sub(
    r'<span id="display-phone"[^>]*>[\s\S]*?</span>',
    '<span id="display-phone" class="font-medium truncate">+84 947 282 357 <span class="text-slate-500 text-[5.8px]">(Zalo/Phone)</span></span>',
    front_article
)

# 4. Email hook
front_article = re.sub(
    r'<span id="display-email"[^>]*>[\s\S]*?</span>',
    '<span id="display-email" class="font-medium truncate">phuc.nn@yspace.vn</span>',
    front_article
)

# 5. QR Code hook
qr_replacement = f"""<div id="card-qr-box" class="w-[8mm] h-[8mm] bg-white rounded p-0.5 shadow-sm flex items-center justify-center relative overflow-hidden">
                    <img src="data:image/png;base64,{qr_oliver_b64}" alt="Lark QR" class="w-full h-full object-contain rounded" />
                  </div>
                  <span id="card-qr-label" class="text-[4.8px] font-bold text-[#FF2A75] mt-0.5 tracking-tighter uppercase">Lark Contact</span>"""

front_article = re.sub(
    r'<div class="w-\[8mm\] h-\[8mm\] bg-white rounded p-0\.5 shadow-sm flex items-center justify-center relative">[\s\S]*?</div>\s*<span class="text-\[4\.8px\] font-bold text-\[#FF2A75\] mt-0\.5 tracking-tighter uppercase">Scan vCard</span>',
    qr_replacement,
    front_article
)

full_index_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Digital Transformation Specialist Business Card - YSPACE</title>
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            yspace: {{
              pink: '#E61B5F',       /* Màu hồng đỏ đặc trưng thương hiệu YSPACE */
              pinkDark: '#C9104F',
              pinkGlow: '#FF2A75',
              dark: '#080C16',       /* Deep Space Obsidian */
              card: '#0D1322',
              cardLight: '#141D33',
              border: '#1E293B',
            }}
          }}
        }}
      }}
    }}
  </script>
  
  <!-- Google Fonts: Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
  
  <style>
    * {{
      box-sizing: border-box;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    }}

    @page {{
      size: 90mm 54mm;
      margin: 0;
    }}

    @media print {{
      html, body {{
        width: 90mm !important;
        height: 54mm !important;
        margin: 0 !important;
        padding: 0 !important;
        background: transparent !important;
        display: block !important;
      }}
      .no-print {{
        display: none !important;
      }}
      .stage-wrapper {{
        padding: 0 !important;
        margin: 0 !important;
        background: transparent !important;
        min-height: auto !important;
        display: block !important;
      }}
      .scale-wrapper {{
        transform: none !important;
        margin: 0 !important;
      }}
      .print-page-break {{
        page-break-after: always !important;
      }}
      .business-card {{
        width: 90mm !important;
        height: 54mm !important;
        margin: 0 !important;
        box-shadow: none !important;
        border: none !important;
        border-radius: 0 !important;
        page-break-inside: avoid !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }}
    }}

    /* Thu phóng màn hình */
    .zoom-100 {{ transform: scale(1); }}
    .zoom-150 {{ transform: scale(1.5); }}
    .zoom-200 {{ transform: scale(2); }}

    /* Hiệu ứng viền phát sáng thẻ công nghệ */
    .cyber-border {{
      position: relative;
    }}
    .cyber-border::after {{
      content: '';
      position: absolute;
      inset: -1px;
      border-radius: inherit;
      padding: 1px;
      background: linear-gradient(135deg, rgba(230,27,95,0.7) 0%, rgba(255,42,117,0.2) 40%, rgba(30,41,59,0.3) 100%);
      -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      pointer-events: none;
    }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col selection:bg-[#E61B5F] selection:text-white">

  <!-- THANH CÔNG CỤ XEM TRƯỚC VÀ IN -->
  <header class="no-print sticky top-0 z-50 bg-slate-900/95 backdrop-blur border-b border-slate-800 px-5 py-3 shadow-xl">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-4">
      
      <!-- Brand Logo YSPACE -->
      <div class="flex items-center gap-3">
        <img src="data:image/png;base64,{yspace_logo_b64}" alt="YSPACE Logo" class="w-8 h-8 object-contain drop-shadow-[0_0_10px_rgba(230,27,95,0.5)]" />
        <div>
          <h1 class="text-sm font-bold text-white tracking-tight flex items-center gap-2">
            Digital Transformation Specialist Card
            <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-[#E61B5F]/20 text-[#FF2A75] border border-[#E61B5F]/40">Executive Dark Tech</span>
          </h1>
          <p class="text-xs text-slate-400">Chuyên gia Chuyển đổi số &bull; Company OS Architect &bull; Chuẩn in 90mm &times; 54mm</p>
        </div>
      </div>

      <!-- Controls: Switch Profile, Switch View, Zoom & Print Action -->
      <div class="flex items-center gap-3 flex-wrap">
        
        <!-- Chọn nhân sự (Profile) -->
        <div class="flex items-center bg-slate-800/80 rounded-lg p-1 border border-slate-700/80 text-xs text-slate-300">
          <span class="px-2 text-slate-400 text-[11px] font-medium">Nhân sự:</span>
          <button onclick="setProfile('oliver')" id="btn-prof-oliver" class="prof-btn px-2.5 py-1 rounded font-medium transition bg-[#E61B5F] text-white font-bold">Oliver Nguyen (Phúc)</button>
          <button onclick="setProfile('thu')" id="btn-prof-thu" class="prof-btn px-2.5 py-1 rounded font-medium hover:text-white transition">Thanh Thư (Helimer)</button>
        </div>

        <!-- Chọn kiểu tên (VI / EN) -->
        <div class="flex items-center bg-slate-800/80 rounded-lg p-1 border border-slate-700/80 text-xs text-slate-300">
          <span class="px-2 text-slate-400 text-[11px] font-medium">Tên:</span>
          <button onclick="setLang('en')" id="btn-lang-en" class="lang-btn px-2.5 py-1 rounded font-medium transition bg-[#E61B5F] text-white font-bold">English</button>
          <button onclick="setLang('vi')" id="btn-lang-vi" class="lang-btn px-2.5 py-1 rounded font-medium hover:text-white transition">Tiếng Việt</button>
        </div>

        <!-- Tab chuyển Mặt trước / Mặt sau -->
        <div class="flex items-center bg-slate-800/80 rounded-lg p-1 border border-slate-700/80 text-xs text-slate-300">
          <button onclick="switchCard('front')" id="tab-front" class="card-tab px-3 py-1 rounded font-medium hover:text-white transition bg-[#E61B5F] text-white font-bold">Mặt Trước</button>
          <button onclick="switchCard('back')" id="tab-back" class="card-tab px-3 py-1 rounded font-medium hover:text-white transition">Mặt Sau</button>
          <button onclick="switchCard('both')" id="tab-both" class="card-tab px-3 py-1 rounded font-medium hover:text-white transition">Cả 2 Mặt</button>
        </div>

        <!-- Zoom controls -->
        <div class="hidden md:flex items-center bg-slate-800/80 rounded-lg p-1 border border-slate-700/80 text-xs text-slate-300">
          <span class="px-2 text-slate-400 text-[11px] font-medium">Thu phóng:</span>
          <button onclick="setZoom('zoom-100')" id="btn-zoom-100" class="zoom-btn px-2.5 py-1 rounded font-medium hover:text-white transition">100%</button>
          <button onclick="setZoom('zoom-150')" id="btn-zoom-150" class="zoom-btn px-2.5 py-1 rounded font-medium hover:text-white transition">150%</button>
          <button onclick="setZoom('zoom-200')" id="btn-zoom-200" class="zoom-btn px-2.5 py-1 rounded font-medium hover:text-white transition bg-[#E61B5F] text-white font-bold">200%</button>
        </div>

        <!-- Print Button -->
        <button onclick="window.print()" class="bg-gradient-to-r from-[#E61B5F] via-[#FF2A75] to-[#E11D48] hover:opacity-95 text-white font-bold px-4 py-2 rounded-lg shadow-lg shadow-[#E61B5F]/35 transition duration-150 flex items-center gap-2 text-xs">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/>
          </svg>
          In Thẻ (Print)
        </button>
      </div>

    </div>
  </header>

  <!-- VÙNG HIỂN THỊ THẺ -->
  <main class="stage-wrapper flex-1 flex flex-col items-center justify-center p-8 sm:p-14 overflow-auto gap-12">
    
    <div id="cardWrapper" class="scale-wrapper zoom-200 transition-transform duration-200 ease-out origin-center my-8 flex flex-col sm:flex-row items-center justify-center gap-8">
      {front_article}
      {back_article}
    </div>

  </main>

  <!-- Script điều khiển Thu phóng, Chuyển Mặt thẻ, Đổi Profile & Đổi Tên -->
  <script>
    const profiles = {{
      oliver: {{
        name_vi: 'Nguyễn Ngọc Phúc',
        name_en: 'Oliver Nguyen',
        phone: '+84 947 282 357',
        email: 'phuc.nn@yspace.vn',
        avatar: 'data:image/jpeg;base64,{avatar_oliver_b64}',
        qr_inner: `<img src="data:image/png;base64,{qr_oliver_b64}" alt="Lark QR" class="w-full h-full object-contain rounded" />`,
        qr_label: 'Lark Contact'
      }},
      thu: {{
        name_vi: 'Nguyễn Thị Thanh Thư',
        name_en: 'Helimer Haluy',
        phone: '+84 369 693 240',
        email: 'thu.ntt@yspace.vn',
        avatar: 'data:image/jpeg;base64,{avatar_thu_b64}',
        qr_inner: `<svg class="w-full h-full text-slate-950" viewBox="0 0 24 24" fill="currentColor"><path d="M2 2h8v8H2V2zm2 2v4h4V4H4zm10-2h8v8h-8V2zm2 2v4h4V4h-4zM2 14h8v8H2v-8zm2 2v4h4v-4H4zm14 0h4v4h-4v-4zm-4 4h4v4h-4v-4zm4-4h4v-4h-4v4zm-4-4h4v4h-4v-4z" /></svg><div class="absolute inset-0 m-auto w-2 h-2 rounded-[2px] bg-[#E61B5F] flex items-center justify-center text-white text-[4px] font-black">Y</div>`,
        qr_label: 'Scan vCard'
      }}
    }};

    let currentProfile = 'oliver';
    let currentLang = 'en';

    function updateCardDisplay() {{
      const p = profiles[currentProfile];
      const nameEl = document.getElementById('display-name');
      const phoneEl = document.getElementById('display-phone');
      const emailEl = document.getElementById('display-email');
      const avatarEl = document.getElementById('card-avatar');
      const qrBox = document.getElementById('card-qr-box');
      const qrLabel = document.getElementById('card-qr-label');

      if (nameEl) nameEl.innerText = currentLang === 'vi' ? p.name_vi : p.name_en;
      if (phoneEl) phoneEl.innerHTML = `${{p.phone}} <span class="text-slate-500 text-[5.8px]">(Zalo/Phone)</span>`;
      if (emailEl) emailEl.innerText = p.email;
      if (avatarEl) avatarEl.src = p.avatar;
      if (qrBox && p.qr_inner) qrBox.innerHTML = p.qr_inner;
      if (qrLabel && p.qr_label) qrLabel.innerText = p.qr_label;
    }}

    function setProfile(profKey) {{
      currentProfile = profKey;
      document.querySelectorAll('.prof-btn').forEach(btn => {{
        btn.classList.remove('bg-[#E61B5F]', 'text-white', 'font-bold');
        btn.classList.add('hover:text-white');
      }});
      const activeBtn = document.getElementById('btn-prof-' + profKey);
      if (activeBtn) {{
        activeBtn.classList.add('bg-[#E61B5F]', 'text-white', 'font-bold');
        activeBtn.classList.remove('hover:text-white');
      }}
      updateCardDisplay();
    }}

    function setLang(langKey) {{
      currentLang = langKey;
      document.querySelectorAll('.lang-btn').forEach(btn => {{
        btn.classList.remove('bg-[#E61B5F]', 'text-white', 'font-bold');
        btn.classList.add('hover:text-white');
      }});
      const activeBtn = document.getElementById('btn-lang-' + langKey);
      if (activeBtn) {{
        activeBtn.classList.add('bg-[#E61B5F]', 'text-white', 'font-bold');
        activeBtn.classList.remove('hover:text-white');
      }}
      updateCardDisplay();
    }}

    function setZoom(zoomClass) {{
      const wrapper = document.getElementById('cardWrapper');
      const currentClasses = wrapper.className.split(' ').filter(c => !c.startsWith('zoom-'));
      wrapper.className = currentClasses.join(' ') + ' ' + zoomClass;
      
      document.querySelectorAll('.zoom-btn').forEach(btn => {{
        btn.classList.remove('bg-[#E61B5F]', 'text-white', 'font-bold');
      }});
      const activeBtn = document.getElementById('btn-' + zoomClass);
      if (activeBtn) {{
        activeBtn.classList.add('bg-[#E61B5F]', 'text-white', 'font-bold');
      }}
    }}

    function switchCard(mode) {{
      const frontCard = document.getElementById('card-front-view');
      const backCard = document.getElementById('card-back-view');
      
      document.querySelectorAll('.card-tab').forEach(tab => {{
        tab.classList.remove('bg-[#E61B5F]', 'text-white', 'font-bold');
      }});
      document.getElementById('tab-' + mode).classList.add('bg-[#E61B5F]', 'text-white', 'font-bold');

      if (mode === 'front') {{
        frontCard.style.display = 'flex';
        backCard.style.display = 'none';
      }} else if (mode === 'back') {{
        frontCard.style.display = 'none';
        backCard.style.display = 'flex';
      }} else if (mode === 'both') {{
        frontCard.style.display = 'flex';
        backCard.style.display = 'flex';
      }}
    }}
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_index_html)

print("Generated clean and complete index.html with Lark QR code for Oliver Nguyen!")
