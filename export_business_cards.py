import os
import re
import subprocess
from PIL import Image

SCRATCH_DIR = "/Users/nguyenngocphuc/.gemini/antigravity/scratch/business-card"
DOWNLOADS_DIR = "/Users/nguyenngocphuc/Downloads"
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# 1. Read index.html
with open(os.path.join(SCRATCH_DIR, "index.html"), "r", encoding="utf-8") as f:
    full_html = f.read()

# Extract head content (Tailwind, Fonts, Styles)
head_match = re.search(r'<head>([\s\S]*?)</head>', full_html)
head_content = head_match.group(1) if head_match else ""

# Extract Front Card
front_match = re.search(r'(<article id="card-front-view"[\s\S]*?</article>)', full_html)
front_html_base = front_match.group(1) if front_match else ""

# Extract Back Card
back_match = re.search(r'(<article id="card-back-view"[\s\S]*?</article>)', full_html)
back_html_base = back_match.group(1) if back_match else ""

# Prepare variants
front_oliver = front_html_base.replace("Nguyễn Ngọc Phúc", "Oliver Nguyen")
front_phuc = front_html_base.replace("Oliver Nguyen", "Nguyễn Ngọc Phúc")

# Thanh Thu variant
front_thu = (front_html_base
    .replace("Oliver Nguyen", "Nguyễn Thị Thanh Thư")
    .replace("+84 947 282 357", "+84 369 693 240")
    .replace("phuc.nn@yspace.vn", "thu.ntt@yspace.vn")
    .replace("avatar_oliver.jpg", "avatar_thu.jpg")
    .replace("qr_oliver.png", "qr_thu.png")
)

if os.path.exists(os.path.join(SCRATCH_DIR, "avatar_3x4_b64.txt")) and os.path.exists(os.path.join(SCRATCH_DIR, "avatar_thu_b64.txt")):
    with open(os.path.join(SCRATCH_DIR, "avatar_3x4_b64.txt")) as f1, open(os.path.join(SCRATCH_DIR, "avatar_thu_b64.txt")) as f2:
        b64_oliver = f1.read().strip()
        b64_thu = f2.read().strip()
        front_thu = front_thu.replace(b64_oliver, b64_thu)

if os.path.exists(os.path.join(SCRATCH_DIR, "qr_oliver_b64.txt")) and os.path.exists(os.path.join(SCRATCH_DIR, "qr_thu_b64.txt")):
    with open(os.path.join(SCRATCH_DIR, "qr_oliver_b64.txt")) as f1, open(os.path.join(SCRATCH_DIR, "qr_thu_b64.txt")) as f2:
        b64_qr_oliver = f1.read().strip()
        b64_qr_thu = f2.read().strip()
        front_thu = front_thu.replace(b64_qr_oliver, b64_qr_thu)

front_helimer = front_thu.replace("Nguyễn Thị Thanh Thư", "Helimer Haluy")

# 2. Template for single isolated card
def make_single_card_html(card_article_html, title="YSPACE Business Card"):
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
{head_content}
<style>
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
</style>
</head>
<body class="bg-[#080C16]">
{card_article_html}
</body>
</html>"""

# 3. Template for 2-in-1 Mockup Showcase
def make_both_cards_html(front_article, back_article, emp_name="Oliver Nguyen"):
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
{head_content}
<style>
  html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100vh;
    background: #050811;
    font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
    color: #F8FAFC;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }}
  .card-container {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 130px;
  }}
  .card-box {{
    display: flex;
    flex-direction: column;
    align-items: center;
  }}
  .business-card {{
    width: 90mm !important;
    height: 54mm !important;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7), 0 0 30px rgba(230, 27, 95, 0.15) !important;
    border-radius: 14px !important;
  }}
</style>
</head>
<body class="p-8">
  <div class="mb-6 text-center">
    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#E61B5F]/15 border border-[#E61B5F]/30 text-[#FF2A75] text-xs font-bold uppercase tracking-wider mb-2">
      YSPACE Digital Transformation Specialist &bull; Standard 90mm &times; 54mm
    </div>
    <h1 class="text-2xl font-black text-white tracking-tight">
      Business Card &bull; <span class="text-[#E61B5F]">{emp_name}</span>
    </h1>
    <p class="text-xs text-slate-400 mt-1">Chuẩn in ấn cao cấp Executive Dark Tech &bull; Màu sắc nhận diện thương hiệu #E61B5F</p>
  </div>

  <div class="card-container">
    <div class="card-box">
      <div class="transform scale-125 origin-center my-6">
        {front_article}
      </div>
      <div class="mt-6 flex items-center gap-2 text-xs font-bold tracking-widest text-[#FF2A75] uppercase bg-slate-900/80 px-4 py-1.5 rounded-full border border-slate-800">
        <span class="w-2 h-2 rounded-full bg-[#E61B5F]"></span>
        Mặt Trước (Front Side)
      </div>
    </div>

    <div class="card-box">
      <div class="transform scale-125 origin-center my-6">
        {back_article}
      </div>
      <div class="mt-6 flex items-center gap-2 text-xs font-bold tracking-widest text-slate-300 uppercase bg-slate-900/80 px-4 py-1.5 rounded-full border border-slate-800">
        <span class="w-2 h-2 rounded-full bg-slate-400"></span>
        Mặt Sau (Back Side)
      </div>
    </div>
  </div>
</body>
</html>"""

# 4. Template for Exact 2-Page Print PDF (90mm x 54mm per page)
def make_print_pdf_html(front_article, back_article):
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
{head_content}
<style>
  @page {{
    size: 90mm 54mm;
    margin: 0;
  }}
  * {{
    box-sizing: border-box;
    -webkit-font-smoothing: antialiased;
    margin: 0;
    padding: 0;
  }}
  html, body {{
    margin: 0 !important;
    padding: 0 !important;
    width: 90mm !important;
    height: 54mm !important;
    background: #080C16 !important;
  }}
  .print-page {{
    width: 90mm !important;
    height: 54mm !important;
    margin: 0 !important;
    padding: 0 !important;
    page-break-after: always !important;
    page-break-inside: avoid !important;
    overflow: hidden !important;
    position: relative !important;
  }}
  .business-card {{
    width: 90mm !important;
    height: 54mm !important;
    margin: 0 !important;
    box-shadow: none !important;
    border-radius: 0 !important;
    border: none !important;
    page-break-inside: avoid !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }}
</style>
</head>
<body>
  <div class="print-page">
    {front_article}
  </div>
  <div class="print-page" style="page-break-after: avoid !important;">
    {back_article}
  </div>
</body>
</html>"""

# Write HTML files
files_to_write = {
    "export_front_oliver.html": make_single_card_html(front_oliver, "YSPACE Card Front - Oliver Nguyen"),
    "export_front_phuc.html": make_single_card_html(front_phuc, "YSPACE Card Front - Nguyen Ngoc Phuc"),
    "export_front_thu.html": make_single_card_html(front_thu, "YSPACE Card Front - Nguyen Thi Thanh Thu"),
    "export_front_thu_en.html": make_single_card_html(front_helimer, "YSPACE Card Front - Helimer Haluy"),
    "export_back.html": make_single_card_html(back_html_base, "YSPACE Card Back"),
    "export_both_oliver.html": make_both_cards_html(front_oliver, back_html_base, "Oliver Nguyen"),
    "export_both_phuc.html": make_both_cards_html(front_phuc, back_html_base, "Nguyễn Ngọc Phúc"),
    "export_both_thu.html": make_both_cards_html(front_thu, back_html_base, "Nguyễn Thị Thanh Thư"),
    "export_both_thu_en.html": make_both_cards_html(front_helimer, back_html_base, "Helimer Haluy"),
    "export_print_oliver.html": make_print_pdf_html(front_oliver, back_html_base),
    "export_print_phuc.html": make_print_pdf_html(front_phuc, back_html_base),
    "export_print_thu.html": make_print_pdf_html(front_thu, back_html_base),
    "export_print_thu_en.html": make_print_pdf_html(front_helimer, back_html_base)
}

for fname, content in files_to_write.items():
    with open(os.path.join(SCRATCH_DIR, fname), "w", encoding="utf-8") as f:
        f.write(content)
print("HTML templates written.")

# Render High-Resolution PNGs and PDFs
def render_png(html_name, output_png, scale=4, width=340, height=204):
    html_path = os.path.join(SCRATCH_DIR, html_name)
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        f"--force-device-scale-factor={scale}",
        f"--window-size={width},{height}",
        f"--screenshot={output_png}",
        html_path
    ]
    subprocess.run(cmd, check=True)

def render_pdf(html_name, output_pdf):
    html_path = os.path.join(SCRATCH_DIR, html_name)
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        f"--print-to-pdf={output_pdf}",
        html_path
    ]
    subprocess.run(cmd, check=True)

# 1. Front Oliver (1360 x 816)
front_oliver_png = os.path.join(DOWNLOADS_DIR, "YSPACE_Card_Mat_Truoc_Oliver_Nguyen.png")
render_png("export_front_oliver.html", front_oliver_png, scale=4, width=340, height=204)
# Default copy
render_png("export_front_oliver.html", os.path.join(DOWNLOADS_DIR, "YSPACE_Card_Mat_Truoc.png"), scale=4, width=340, height=204)

# 2. Front Nguyen Ngoc Phuc
front_phuc_png = os.path.join(DOWNLOADS_DIR, "YSPACE_Card_Mat_Truoc_Nguyen_Ngoc_Phuc.png")
render_png("export_front_phuc.html", front_phuc_png, scale=4, width=340, height=204)

# 3. Front Nguyen Thi Thanh Thu & Helimer Haluy
front_thu_png = os.path.join(DOWNLOADS_DIR, "YSPACE_Card_Mat_Truoc_Thanh_Thu.png")
render_png("export_front_thu.html", front_thu_png, scale=4, width=340, height=204)
front_helimer_png = os.path.join(DOWNLOADS_DIR, "YSPACE_Card_Mat_Truoc_Helimer_Haluy.png")
render_png("export_front_thu_en.html", front_helimer_png, scale=4, width=340, height=204)

# 4. Back Side
back_png = os.path.join(DOWNLOADS_DIR, "YSPACE_Card_Mat_Sau.png")
render_png("export_back.html", back_png, scale=4, width=340, height=204)

# 5. Both Cards Mockup (1440 x 820)
both_oliver_png = os.path.join(DOWNLOADS_DIR, "YSPACE_Card_2Mat_Oliver_Nguyen.png")
render_png("export_both_oliver.html", both_oliver_png, scale=2, width=1440, height=820)
# Default copy
render_png("export_both_oliver.html", os.path.join(DOWNLOADS_DIR, "YSPACE_Card_2Mat.png"), scale=2, width=1440, height=820)

both_phuc_png = os.path.join(DOWNLOADS_DIR, "YSPACE_Card_2Mat_Nguyen_Ngoc_Phuc.png")
render_png("export_both_phuc.html", both_phuc_png, scale=2, width=1440, height=820)

both_thu_png = os.path.join(DOWNLOADS_DIR, "YSPACE_Card_2Mat_Thanh_Thu.png")
render_png("export_both_thu.html", both_thu_png, scale=2, width=1440, height=820)

both_helimer_png = os.path.join(DOWNLOADS_DIR, "YSPACE_Card_2Mat_Helimer_Haluy.png")
render_png("export_both_thu_en.html", both_helimer_png, scale=2, width=1440, height=820)

# 6. Print PDF (2 pages 90mm x 54mm)
pdf_oliver = os.path.join(DOWNLOADS_DIR, "YSPACE_Business_Card_Oliver_Nguyen_InAn_90x54mm.pdf")
render_pdf("export_print_oliver.html", pdf_oliver)
# Default copy
render_pdf("export_print_oliver.html", os.path.join(DOWNLOADS_DIR, "YSPACE_Business_Card_90x54mm.pdf"))

pdf_phuc = os.path.join(DOWNLOADS_DIR, "YSPACE_Business_Card_Nguyen_Ngoc_Phuc_InAn_90x54mm.pdf")
render_pdf("export_print_phuc.html", pdf_phuc)

pdf_thu = os.path.join(DOWNLOADS_DIR, "YSPACE_Business_Card_Thanh_Thu_InAn_90x54mm.pdf")
render_pdf("export_print_thu.html", pdf_thu)

pdf_helimer = os.path.join(DOWNLOADS_DIR, "YSPACE_Business_Card_Helimer_Haluy_InAn_90x54mm.pdf")
render_pdf("export_print_thu_en.html", pdf_helimer)

print("All business card assets exported successfully into ~/Downloads!")

