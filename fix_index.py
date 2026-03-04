import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# find first <script src="https://cdn.tailwindcss.com"></script>
start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if "cdn.tailwindcss.com" in line:
        start_idx = i + 1
        break

for i in range(start_idx, len(lines)):
    if "<style>" in line:
        pass
    if line.strip() == "<style>":
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    del lines[start_idx:end_idx]
    
    tailwind = """    <script>
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
"""
    lines.insert(start_idx, tailwind)

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
