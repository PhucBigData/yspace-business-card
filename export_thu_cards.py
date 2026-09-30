import os
import re
import subprocess

SCRATCH_DIR = "/Users/nguyenngocphuc/.gemini/antigravity/scratch/business-card"
DOWNLOADS_DIR = "/Users/nguyenngocphuc/Downloads"
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

with open(os.path.join(SCRATCH_DIR, "index.html"), "r", encoding="utf-8") as f:
    full_html = f.read()

head_match = re.search(r'<head>([\s\S]*?)</head>', full_html)
head_content = head_match.group(1)

front_match = re.search(r'(<article id="card-front-view"[\s\S]*?</article>)', full_html)
front_html_thu_vi = front_match.group(1)

back_match = re.search(r'(<article id="card-back-view"[\s\S]*?</article>)', full_html)
back_html = back_match.group(1)

# English name version
front_html_thu_en = front_html_thu_vi.replace("Nguyễn Thị Thanh Thư", "Helimer Haluy")

def make_single_card(card_article):
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
{card_article}
</body>
</html>"""

def make_both_cards(front_article, back_article, name_display="Nguyễn Thị Thanh Thư"):
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
    gap: 90px;
    width: 100%;
    max-width: 1600px;
    margin: 0 auto;
  }}
  .card-box {{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0 20px;
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
      Business Card &bull; <span class="text-[#E61B5F]">{name_display}</span>
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

def make_print_pdf(front_article, back_article):
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

files_to_render = {
    "export_front_thu_vi.html": make_single_card(front_html_thu_vi),
    "export_front_thu_en.html": make_single_card(front_html_thu_en),
    "export_both_thu_vi.html": make_both_cards(front_html_thu_vi, back_html, "Nguyễn Thị Thanh Thư"),
    "export_both_thu_en.html": make_both_cards(front_html_thu_en, back_html, "Helimer Haluy"),
    "export_print_thu_vi.html": make_print_pdf(front_html_thu_vi, back_html),
    "export_print_thu_en.html": make_print_pdf(front_html_thu_en, back_html)
}

for fname, content in files_to_render.items():
    with open(os.path.join(SCRATCH_DIR, fname), "w", encoding="utf-8") as f:
        f.write(content)

print("Export templates prepared.")

def render_png(html_name, output_png, scale=4, width=340, height=204):
    html_path = os.path.join(SCRATCH_DIR, html_name)
    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
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
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={output_pdf}",
        html_path
    ]
    subprocess.run(cmd, check=True)

# 1. Front Side PNGs
render_png("export_front_thu_vi.html", os.path.join(DOWNLOADS_DIR, "YSPACE_Card_Mat_Truoc_Thanh_Thu.png"), scale=4, width=340, height=204)
render_png("export_front_thu_en.html", os.path.join(DOWNLOADS_DIR, "YSPACE_Card_Mat_Truoc_Helimer_Haluy.png"), scale=4, width=340, height=204)

# 2. Both Sides 2-in-1 Mockup PNGs
render_png("export_both_thu_vi.html", os.path.join(DOWNLOADS_DIR, "YSPACE_Card_2Mat_Thanh_Thu.png"), scale=2, width=1600, height=850)
render_png("export_both_thu_en.html", os.path.join(DOWNLOADS_DIR, "YSPACE_Card_2Mat_Helimer_Haluy.png"), scale=2, width=1600, height=850)

# 3. Print Ready PDFs
render_pdf("export_print_thu_vi.html", os.path.join(DOWNLOADS_DIR, "YSPACE_Business_Card_Thanh_Thu_InAn_90x54mm.pdf"))
render_pdf("export_print_thu_en.html", os.path.join(DOWNLOADS_DIR, "YSPACE_Business_Card_Helimer_Haluy_InAn_90x54mm.pdf"))

print("All Thanh Thu card exports completed successfully!")
