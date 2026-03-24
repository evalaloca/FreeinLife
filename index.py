# -*- coding: utf-8 -*-
import os

def generate_github_index():
    # 1. Get all htm files in the current directory
    files = [f for f in os.listdir('.') if f.lower().endswith(('.htm', '.html')) and f != 'index.html']
    files.sort()

    # 2. HTML Template with Search/Filter Logic
    html_template = f"""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>佛教經典與講記索引</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f9f9f9; }}
        h1 {{ color: #333; text-align: center; }}
        #searchBar {{ width: 100%; padding: 12px; margin-bottom: 20px; border: 1px solid #ddd; border-radius: 8px; font-size: 16px; box-sizing: border-box; }}
        .file-list {{ list-style: none; padding: 0; }}
        .file-item {{ background: white; margin-bottom: 8px; padding: 12px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); display: flex; align-items: center; }}
        .file-item a {{ text-decoration: none; color: #0366d6; font-weight: 500; flex-grow: 1; }}
        .file-item a:hover {{ text-decoration: underline; }}
        .no-results {{ display: none; text-align: center; color: #888; margin-top: 20px; }}
    </style>
</head>
<body>

    <h1>經書文獻索引</h1>
    
    <input type="text" id="searchBar" onkeyup="filterFiles()" placeholder="請輸入關鍵字搜尋 (例如：地藏、印順)...">

    <ul class="file-list" id="fileList">
        {"".join([f'<li class="file-item"><a href="./{f}">{f}</a></li>' for f in files])}
    </ul>

    <div id="noResults" class="no-results">找不到相關檔案</div>

    <script>
        function filterFiles() {{
            let input = document.getElementById('searchBar').value.toLowerCase();
            let list = document.getElementById('fileList');
            let items = list.getElementsByTagName('li');
            let noResults = document.getElementById('noResults');
            let found = false;

            for (let i = 0; i < items.length; i++) {{
                let text = items[i].textContent || items[i].innerText;
                if (text.toLowerCase().indexOf(input) > -1) {{
                    items[i].style.display = "";
                    found = true;
                }} else {{
                    items[i].style.display = "none";
                }}
            }}
            
            noResults.style.display = found ? "none" : "block";
        }}
    </script>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    
    print(f"✅ index.html generated with {len(files)} files.")

if __name__ == "__main__":
    generate_github_index()
