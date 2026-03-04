import os

base_dir = '/Users/hk/Desktop/hp_test'
html_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Determine depth
    rel_path = os.path.relpath(filepath, base_dir)
    depth = len(rel_path.split(os.sep)) - 1
    prefix = '../' * depth if depth > 0 else './'

    # Fix component loading paths in JS
    if 'loadComponent' in content:
        # Instead of modifying the HTML files' inline JS, let's modify the components themselves?
        # No, components are loaded as strings. 
        # A better way: Modify header/footer to use `href="#" data-href="/index.html"` and let JS resolve?
        pass

    # Actually, let's just do a simple replacement on the JS loader in all files
    # to rewrite the `href="/` inside the loaded HTML.
    
    # Let's find the loadComponent function and inject the path replacement.
    old_func = """document.getElementById(id).innerHTML = html;"""
    if "const pathString = window.location.pathname;" in content:
        # Breadcrumb handling logic exists
        new_func = f"""document.getElementById(id).innerHTML = html;
                    document.getElementById(id).querySelectorAll('a').forEach(a => {{
                        let href = a.getAttribute('href');
                        if (href && href.startsWith('/')) {{
                            a.setAttribute('href', '{prefix}' + href.substring(1));
                        }}
                    }});"""
    else:
        new_func = f"""document.getElementById(id).innerHTML = html;
                    // Fix relative paths
                    document.getElementById(id).querySelectorAll('a').forEach(a => {{
                        let href = a.getAttribute('href');
                        if (href && href.startsWith('/')) {{
                            a.setAttribute('href', '{prefix}' + href.substring(1));
                        }}
                    }});"""
                    
    if old_func in content and "Fix relative paths" not in content:
        content = content.replace(old_func, new_func)
    
    # Also fix static links in the HTML files themselves
    content = content.replace('href="/', f'href="{prefix}')
    
    with open(filepath, 'w') as f:
        f.write(content)
        
print("Paths fixed.")
