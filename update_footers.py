import os
files = ['biography.html', 'albums.html', 'news/12345.html']
old_str = """      <div class="f-logo-n">Иван Квитка</div>"""

def process_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Adjust path to SVG based on relative folder depth
    svg_path = "Логотип_партии__Единая_Россия_.svg"
    if "news/" in filepath:
        svg_path = "../Логотип_партии__Единая_Россия_.svg"
        
    new_str = f"""      <div class="f-logo-n" style="display: flex; align-items: center; gap: 12px;">
        Иван Квитка
        <img src="{svg_path}" alt="Единая Россия" style="height: 24px; opacity: 0.8; filter: brightness(0) invert(1);">
      </div>"""
      
    content = content.replace(old_str, new_str)
    with open(filepath, 'w') as f:
        f.write(content)

for f in files:
    process_file(f)
