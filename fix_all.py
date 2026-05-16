import os
import re
import glob

BASE = "/Users/mac/Library/Mobile Documents/com~apple~CloudDocs/Desktop/projects/kim"

# ============================================================
# 1. RENAME FILES WITH SPACES → hyphens
# ============================================================
rename_map = {}  # old_relative → new_relative

for root, dirs, files in os.walk(os.path.join(BASE, "media")):
    for fname in files:
        if ' ' not in fname:
            continue
        ext = os.path.splitext(fname)[1].lower()
        if ext not in ['.jpg','.jpeg','.png','.webp','.mp4','.mov']:
            continue
        new_name = fname.replace(' ', '-').replace('+', 'plus').replace('(', '').replace(')', '').replace('..', '.').replace('é', 'e').replace('è', 'e').replace('ê', 'e').replace('î', 'i').replace('ô', 'o').replace('ù', 'u').replace('û', 'u').replace('à', 'a').replace('â', 'a').replace('ç', 'c')
        old_path = os.path.join(root, fname)
        new_path = os.path.join(root, new_name)
        if old_path != new_path and not os.path.exists(new_path):
            os.rename(old_path, new_path)
            # Compute relative paths from BASE
            old_rel = os.path.relpath(old_path, BASE)
            new_rel = os.path.relpath(new_path, BASE)
            rename_map[old_rel] = new_rel
            print(f"RENAMED: {old_rel} → {new_rel}")

print(f"\nTotal renamed: {len(rename_map)} files")

# ============================================================
# 2. UPDATE ALL REFERENCES IN HTML / JS files
# ============================================================
html_js_files = glob.glob(os.path.join(BASE, "**/*.html"), recursive=True) + \
                glob.glob(os.path.join(BASE, "assets/js/*.js"))

updated_files = 0
for fpath in html_js_files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content
        for old_rel, new_rel in rename_map.items():
            # Just replace filename portions (keep media/ prefix safe)
            old_name = os.path.basename(old_rel)
            new_name = os.path.basename(new_rel)
            if old_name in content:
                content = content.replace(old_name, new_name)
        if content != original:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_files += 1
            print(f"UPDATED refs: {os.path.relpath(fpath, BASE)}")
    except Exception as e:
        print(f"ERROR {fpath}: {e}")

print(f"\nTotal HTML/JS files updated: {updated_files}")

# ============================================================
# 3. ADD LOADER TO ALL HTML PAGES (except index.html)
# ============================================================
LOADER_SUBDIR = '''    <!-- Loader -->
    <div id="loader" class="fixed inset-0 z-[100] flex items-center justify-center bg-white dark:bg-kim-darker transition-opacity duration-700">
        <div class="relative w-3/4 md:w-1/2 max-w-4xl h-auto">
            <img src="{ROOT}media/logo.png" alt="KIM Motors Loading" class="w-full h-auto opacity-10 grayscale">
            <div class="absolute inset-0 overflow-hidden loader-fill">
                <img src="{ROOT}media/logo.png" alt="KIM Motors Loading" class="w-full h-auto max-w-none">
            </div>
        </div>
    </div>

'''

pages_root  = ['a-propos.html','atelier.html','contact.html','devis.html']
pages_model = ['modeles/pista-hr.html','modeles/pista-hr-plus.html','modeles/pista-vcx.html',
               'modeles/ghost-v7.html','modeles/black-street.html','modeles/power-spring-st.html',
               'modeles/power-125.html','modeles/power-110.html','modeles/blaster.html']

loader_added = 0
for rel_path in pages_root + pages_model:
    fpath = os.path.join(BASE, rel_path)
    if not os.path.exists(fpath):
        print(f"SKIP (not found): {rel_path}")
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'id="loader"' in content:
        print(f"SKIP (loader exists): {rel_path}")
        continue
    root_prefix = '../' if rel_path.startswith('modeles/') else ''
    loader_html = LOADER_SUBDIR.replace('{ROOT}', root_prefix)
    # Insert right after <body ...>
    new_content = re.sub(r'(<body[^>]*>)', r'\1\n' + loader_html, content, count=1)
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        loader_added += 1
        print(f"LOADER ADDED: {rel_path}")

print(f"\nLoader added to {loader_added} pages.")

# ============================================================
# 4. FIX HORIZONTAL STRIP SCROLLBAR — hide it in CSS
# ============================================================
css_file = os.path.join(BASE, "assets/css/style.css")
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

strip_css = """
/* --- Hide scrollbar on horizontal feature strips --- */
.features-strip { overflow-x: auto; scrollbar-width: none; -ms-overflow-style: none; }
.features-strip::-webkit-scrollbar { display: none; }
"""
if 'features-strip' not in css:
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write(strip_css)
    print("CSS: features-strip scrollbar hidden added.")

print("\nAll done.")
