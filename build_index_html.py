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

with open("qr_thu_b64.txt", "r") as f:
    qr_thu_b64 = clean_b64(f.read())

with open("logo_yspace_b64.txt", "r") as f:
    yspace_logo_b64 = clean_b64(f.read())

with open("logo_lark_b64.txt", "r") as f:
    lark_logo_b64 = clean_b64(f.read())

# FRONT CARD ARTICLE
front_article = f"""<article id="card-front-view" class="business-card relative w-[90mm] h-[54mm] bg-[#080C16] text-white rounded-xl shadow-2xl overflow-hidden flex items-center p-3.5 select-none cyber-border print-page-break shrink-0">
  
  <!-- Họa tiết mạch chuyển đổi số & vi mạch dữ liệu -->
  <div class="absolute inset-0 pointer-events-none overflow-hidden z-0">
    <div class="absolute inset-0 bg-[radial-gradient(#E61B5F_0.8px,transparent_0.8px)] [background-size:5.5mm_5.5mm] opacity-15"></div>
    <svg class="absolute inset-0 w-full h-full opacity-15" viewBox="0 0 340 200" fill="none" stroke="#E61B5F">
      <path d="M0,35 L50,35 L80,65 L260,65 L290,35 L340,35" stroke-width="1.2" />
      <path d="M0,165 L70,165 L100,135 L240,135 L270,165 L340,165" stroke-width="1.2" />
      <circle cx="80" cy="65" r="3" fill="#E61B5F" />
      <circle cx="260" cy="65" r="3" fill="#E61B5F" />
    </svg>
    <div class="absolute -top-10 -left-10 w-36 h-36 rounded-full bg-[#E61B5F]/20 blur-2xl"></div>
  </div>

  <!-- NỘI DUNG MẶT TRƯỚC (2 CỘT CÂN ĐỐI, THÔNG THOÁNG) -->
  <div class="relative z-10 w-full h-full flex items-center gap-3.5">
    
    <!-- CỘT TRÁI: Ảnh chân dung 3:4 -->
    <div class="shrink-0 flex flex-col items-center justify-center">
      <div class="w-[25.5mm] h-[34mm] rounded-xl overflow-hidden p-[1.5px] bg-gradient-to-b from-[#E61B5F] via-[#FF2A75]/50 to-slate-800 shadow-xl shadow-[#E61B5F]/25 ring-1 ring-[#E61B5F]/40 relative group">
        <img id="card-avatar" src="avatar_oliver.jpg" onerror="this.onerror=null; this.src='data:image/jpeg;base64,{avatar_oliver_b64}'" alt="Oliver Nguyen" class="w-full h-full object-cover rounded-[10px]" />
        
        <!-- Tag trạng thái PRO -->
        <div class="absolute bottom-1 right-1 px-1 py-0.2 bg-black/80 backdrop-blur-xs rounded-full border border-[#E61B5F]/60 flex items-center gap-1 shadow-xs">
          <span class="w-1 h-1 rounded-full bg-emerald-400 animate-pulse"></span>
          <span class="text-[5.2px] font-bold text-slate-200 uppercase tracking-tighter">PRO</span>
        </div>
      </div>
    </div>

    <!-- CỘT PHẢI: Thông tin chuyên gia -->
    <div class="flex-1 h-full flex flex-col justify-between py-0.5 min-w-0">
      
      <!-- Hàng 1: Brand Logo & Badge Lark Partner -->
      <div class="flex items-center justify-between gap-1">
        <div class="flex items-center gap-1.5">
          <img src="logo_yspace.png" onerror="this.onerror=null; this.src='data:image/png;base64,{yspace_logo_b64}'" alt="YSPACE" class="h-3.5 object-contain shrink-0 drop-shadow-[0_0_6px_rgba(230,27,95,0.4)]" />
          <span class="text-[6px] font-extrabold tracking-wider text-[#FF2A75] uppercase px-1 py-0.5 rounded bg-[#E61B5F]/15 border border-[#E61B5F]/30 leading-none">SOLUTIONS</span>
        </div>
        <div class="flex items-center gap-1.5 px-2 py-0.8 rounded-full bg-slate-900/90 border border-slate-700/70 shadow-sm shrink-0">
          <img src="logo_lark_bird.png" onerror="this.onerror=null; this.src='data:image/png;base64,{lark_logo_b64}'" alt="Lark" class="w-3.5 h-3.5 object-contain shrink-0" />
          <span class="text-[7.5px] font-black text-white tracking-tight leading-none">Lark</span>
          <span class="text-[5.5px] font-extrabold px-1.5 py-0.2 rounded-full bg-[#3370FF]/25 text-[#4E88FF] border border-[#3370FF]/50 uppercase tracking-tight leading-none">Partner</span>
        </div>
      </div>

      <!-- Hàng 2: Tên & Chức danh (Khoảng cách thoáng, chữ nổi bật) -->
      <div class="my-auto">
        <h2 id="display-name" class="text-[14.5px] font-black tracking-tight text-white leading-tight">Oliver Nguyen</h2>
        <div class="text-[7.2px] font-bold tracking-wider text-[#FF2A75] uppercase mt-0.5 leading-tight flex items-center gap-1">
          <span>Digital Transformation Specialist</span>
        </div>
        <div class="text-[6.4px] font-medium text-slate-400 tracking-wide mt-0.5">
          Company OS Solution Architect &bull; Lark Expert
        </div>
      </div>

      <!-- Hàng 3: Kênh kết nối số & Smart QR -->
      <div class="pt-1.5 border-t border-slate-800/80 flex items-center justify-between gap-2">
        
        <!-- Danh bạ (Giãn dòng thoáng đãng, icon viền hồng tinh tế) -->
        <div class="space-y-1.2 flex-1 min-w-0">
          <!-- Mobile / Zalo -->
          <div class="flex items-center gap-1.5 text-[6.8px] text-slate-300 leading-tight">
            <div class="w-3 h-3 rounded-full bg-[#E61B5F]/20 text-[#FF2A75] border border-[#E61B5F]/40 flex items-center justify-center shrink-0">
              <svg class="w-1.5 h-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
            </div>
            <span id="display-phone" class="font-medium truncate">+84 947 282 357 <span class="text-slate-500 text-[5.8px]">(Zalo/Phone)</span></span>
          </div>

          <!-- Email -->
          <div class="flex items-center gap-1.5 text-[6.8px] text-slate-300 leading-tight">
            <div class="w-3 h-3 rounded-full bg-[#E61B5F]/20 text-[#FF2A75] border border-[#E61B5F]/40 flex items-center justify-center shrink-0">
              <svg class="w-1.5 h-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
            </div>
            <span id="display-email" class="font-medium truncate">phuc.nn@yspace.vn</span>
          </div>

          <!-- Website & Location -->
          <div class="flex items-center gap-1.5 text-[6.8px] text-slate-300 leading-tight">
            <div class="w-3 h-3 rounded-full bg-[#E61B5F]/20 text-[#FF2A75] border border-[#E61B5F]/40 flex items-center justify-center shrink-0">
              <svg class="w-1.5 h-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"/></svg>
            </div>
            <span class="font-medium truncate">www.yspace.vn &bull; Da Nang Office</span>
          </div>
        </div>

        <!-- Khung QR Code vCard / Lark Contact -->
        <div class="shrink-0 flex flex-col items-center justify-center p-1 rounded-lg bg-white/5 border border-[#E61B5F]/30 backdrop-blur-xs">
          <div id="card-qr-box" class="w-[8.5mm] h-[8.5mm] bg-white rounded p-0.5 shadow-sm flex items-center justify-center relative overflow-hidden">
            <img src="qr_oliver.png" onerror="this.onerror=null; this.src='data:image/png;base64,{qr_oliver_b64}'" alt="Lark QR" class="w-full h-full object-contain rounded" />
          </div>
          <span id="card-qr-label" class="text-[4.8px] font-bold text-[#FF2A75] mt-0.5 tracking-tighter uppercase">Lark Contact</span>
        </div>

      </div>

    </div>

  </div>

</article>"""

# BACK CARD ARTICLE
back_article = f"""<article id="card-back-view" class="business-card relative w-[90mm] h-[54mm] bg-[#080C16] text-white rounded-xl shadow-2xl overflow-hidden flex flex-col justify-between select-none cyber-border print-page-break shrink-0">
  
  <!-- Họa tiết mạch chuyển đổi số & vi mạch dữ liệu -->
  <div class="absolute inset-0 pointer-events-none overflow-hidden z-0">
    <div class="absolute inset-0 bg-[radial-gradient(#E61B5F_0.8px,transparent_0.8px)] [background-size:5.5mm_5.5mm] opacity-15"></div>
    <svg class="absolute inset-0 w-full h-full opacity-20" viewBox="0 0 340 200" fill="none" stroke="#E61B5F">
      <path d="M0,35 L50,35 L80,65 L260,65 L290,35 L340,35" stroke-width="1.2" />
      <path d="M0,165 L70,165 L100,135 L240,135 L270,165 L340,165" stroke-width="1.2" />
      <circle cx="80" cy="65" r="3" fill="#E61B5F" />
      <circle cx="260" cy="65" r="3" fill="#E61B5F" />
      <circle cx="100" cy="135" r="3" fill="#FF2A75" />
      <circle cx="240" cy="135" r="3" fill="#FF2A75" />
    </svg>
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-48 h-48 rounded-full bg-[#E61B5F]/15 blur-2xl"></div>
  </div>

  <!-- Nội dung chính Mặt sau: Tuyên ngôn & Năng lực Tư vấn CĐS -->
  <div class="relative z-10 flex-1 px-5 pt-3 pb-2 flex flex-col justify-between items-center text-center">
    
    <!-- Logo lớn & Định vị thương hiệu -->
    <div>
      <div class="flex flex-col items-center justify-center mb-0.5">
        <img src="logo_yspace.png" onerror="this.onerror=null; this.src='data:image/png;base64,{yspace_logo_b64}'" alt="YSPACE" class="h-5 object-contain drop-shadow-[0_0_12px_rgba(230,27,95,0.5)]" />
        <div class="w-14 h-[1.5px] bg-gradient-to-r from-transparent via-[#E61B5F] to-transparent mt-1 rounded-full"></div>
      </div>
      <p class="text-[6.8px] font-bold tracking-widest text-[#FF2A75] uppercase mt-0.5">
        ARCHITECTING YOUR ENTERPRISE OPERATING SYSTEM
      </p>
    </div>

    <!-- 4 Khối Giải Pháp Chuyển Đổi Số Doanh Nghiệp -->
    <div class="grid grid-cols-2 gap-x-3 gap-y-1.5 text-left w-full max-w-[78mm] my-auto py-1.5 px-3 rounded-lg bg-slate-900/60 border border-[#E61B5F]/30 backdrop-blur-xs shadow-inner">
      <div class="flex items-center gap-1.5">
        <img src="logo_lark_bird.png" onerror="this.onerror=null; this.src='data:image/png;base64,{lark_logo_b64}'" alt="Lark" class="w-3.5 h-3.5 object-contain shrink-0" />
        <div>
          <div class="text-[6.6px] font-bold text-slate-100">Lark Pro Deployment</div>
          <div class="text-[5.4px] text-slate-400">Tối ưu không gian làm việc số all-in-one</div>
        </div>
      </div>
      
      <div class="flex items-center gap-1.5">
        <div class="w-3.5 h-3.5 rounded-full bg-[#E61B5F]/20 border border-[#E61B5F]/40 flex items-center justify-center shrink-0">
          <span class="w-1.5 h-1.5 rounded-full bg-[#E61B5F]"></span>
        </div>
        <div>
          <div class="text-[6.6px] font-bold text-slate-100">Company OS Design</div>
          <div class="text-[5.4px] text-slate-400">Kiến trúc vận hành liên phòng ban</div>
        </div>
      </div>
      
      <div class="flex items-center gap-1.5">
        <div class="w-3.5 h-3.5 rounded-full bg-[#FF2A75]/20 border border-[#FF2A75]/40 flex items-center justify-center shrink-0">
          <span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
        </div>
        <div>
          <div class="text-[6.6px] font-bold text-slate-100">BPM & Automation</div>
          <div class="text-[5.4px] text-slate-400">Tự động hóa luồng quy trình & phê duyệt</div>
        </div>
      </div>
      
      <div class="flex items-center gap-1.5">
        <img src="logo_lark_bird.png" onerror="this.onerror=null; this.src='data:image/png;base64,{lark_logo_b64}'" alt="Lark" class="w-3.5 h-3.5 object-contain shrink-0" />
        <div>
          <div class="text-[6.6px] font-bold text-slate-100">Lark Base & AnyCross</div>
          <div class="text-[5.4px] text-slate-400">Cơ sở dữ liệu quan hệ & Tích hợp API</div>
        </div>
      </div>
    </div>

    <!-- Bottom Footer Bar Mặt sau: Hotline & Kênh Tư Vấn -->
    <div class="flex items-center justify-between w-full max-w-[78mm] pt-1 border-t border-slate-800 text-[6.5px]">
      <div class="flex items-center gap-1.5 text-slate-300">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
        <span>Hotline Chuyển đổi số: <strong class="text-white font-bold">0973 000 002</strong></span>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-[#FF2A75] font-extrabold tracking-wider">www.yspace.vn</span>
        <span class="text-slate-500">&bull;</span>
        <span class="text-slate-400">Da Nang Office</span>
      </div>
    </div>

  </div>

  <!-- Đường chỉ viền đáy thẻ mặt sau -->
  <div class="h-[2px] w-full bg-gradient-to-r from-transparent via-[#E61B5F] to-transparent z-20"></div>

</article>"""

full_index_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
  <meta http-equiv="Pragma" content="no-cache" />
  <meta http-equiv="Expires" content="0" />
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
    .zoom-150 {{ transform: scale(1.35); }}
    .zoom-200 {{ transform: scale(1.6); }}

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
        <img src="logo_yspace.png" onerror="this.onerror=null; this.src='data:image/png;base64,{yspace_logo_b64}'" alt="YSPACE" class="h-7 object-contain drop-shadow-[0_0_10px_rgba(230,27,95,0.5)]" />
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
          <button onclick="setZoom('zoom-150')" id="btn-zoom-150" class="zoom-btn px-2.5 py-1 rounded font-medium hover:text-white transition bg-[#E61B5F] text-white font-bold">150%</button>
          <button onclick="setZoom('zoom-200')" id="btn-zoom-200" class="zoom-btn px-2.5 py-1 rounded font-medium hover:text-white transition">200%</button>
        </div>

        <!-- Print Button -->
        <button onclick="window.print()" class="bg-gradient-to-r from-[#E61B5F] via-[#FF2A75] to-[#E11D48] hover:opacity-95 text-white font-bold px-4 py-2 rounded-lg shadow-lg shadow-[#E61B5F]/35 transition duration-150 flex items-center gap-2 text-xs">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/>
          </svg>
          In Thẻ (Print)
        </button>
      </div>

    </div>
  </header>

  <!-- VÙNG HIỂN THỊ THẺ (KHOẢNG CÁCH RỘNG RÃI, KHÔNG DÍNH NHAU) -->
  <main class="stage-wrapper flex-1 flex flex-col items-center justify-center p-8 sm:p-14 overflow-auto">
    
    <div id="cardWrapper" class="scale-wrapper zoom-150 transition-transform duration-200 ease-out origin-center my-10 flex flex-col lg:flex-row items-center justify-center gap-12 lg:gap-20">
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
        avatar: 'avatar_oliver.jpg',
        avatar_fallback: 'data:image/jpeg;base64,{avatar_oliver_b64}',
        qr_inner: `<img src="qr_oliver.png" onerror="this.onerror=null; this.src='data:image/png;base64,{qr_oliver_b64}'" alt="Lark QR" class="w-full h-full object-contain rounded" />`,
        qr_label: 'Lark Contact'
      }},
      thu: {{
        name_vi: 'Nguyễn Thị Thanh Thư',
        name_en: 'Helimer Haluy',
        phone: '+84 369 693 240',
        email: 'thu.ntt@yspace.vn',
        avatar: 'avatar_thu.jpg',
        avatar_fallback: 'data:image/jpeg;base64,{avatar_thu_b64}',
        qr_inner: `<img src="qr_thu.png" onerror="this.onerror=null; this.src='data:image/png;base64,{qr_thu_b64}'" alt="Lark QR" class="w-full h-full object-contain rounded" />`,
        qr_label: 'Lark Contact'
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
      if (avatarEl) {{
        avatarEl.src = p.avatar;
        avatarEl.onerror = function() {{
          this.onerror = null;
          this.src = p.avatar_fallback;
        }};
      }}
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

# Also update export_back.html with stand-alone back card
export_back_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
  <title>YSPACE Business Card Back</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <style>
    * {{ box-sizing: border-box; -webkit-font-smoothing: antialiased; }}
    body {{ font-family: 'Plus Jakarta Sans', system-ui, sans-serif; }}
    @page {{ size: 90mm 54mm; margin: 0; }}
    html, body {{
      margin: 0 !important;
      padding: 0 !important;
      width: 90mm !important;
      height: 54mm !important;
      overflow: hidden !important;
      background: #080C16 !important;
    }}
    .business-card {{
      width: 90mm !important;
      height: 54mm !important;
      margin: 0 !important;
      box-shadow: none !important;
      border-radius: 0 !important;
      border: none !important;
    }}
    .cyber-border {{ position: relative; }}
    .cyber-border::after {{
      content: ''; position: absolute; inset: -1px; border-radius: inherit; padding: 1px;
      background: linear-gradient(135deg, rgba(230,27,95,0.7) 0%, rgba(255,42,117,0.2) 40%, rgba(30,41,59,0.3) 100%);
      -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      -webkit-mask-composite: xor; mask-composite: exclude; pointer-events: none;
    }}
  </style>
</head>
<body class="bg-[#080C16]">
{back_article}
</body>
</html>"""

with open("export_back.html", "w", encoding="utf-8") as f:
    f.write(export_back_html)

print("Generated clean, spacious, executive index.html and export_back.html!")
