import os
import re
import glob

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine context based on the directory
    is_root = '/' not in filepath.replace('./', '') and 'modeles/' not in filepath

    # --- 1. Mega Menu Update ---
    # Find the block starting with power-125 and ending after power-110
    pattern_mega = re.compile(r'<a href="[^"]*power-125\.html".*?</a\s*>\s*<a href="[^"]*power-110\.html".*?</a\s*>', re.DOTALL)
    
    if is_root:
        mega_replacement = """<a href="#" class="mega-menu-item block group opacity-50 cursor-not-allowed" title="Bientôt disponible">
                        <div class="aspect-video bg-gray-100 dark:bg-kim-gray mb-4 overflow-hidden rounded-lg flex items-center justify-center p-4 relative">
                            <div class="w-full h-full bg-gray-700"></div>
                            <div class="absolute inset-0 flex items-center justify-center bg-black/40"><span class="text-white font-sport text-xl tracking-widest">BIENTÔT</span></div>
                        </div>
                        <h4 class="font-sport font-bold text-2xl tracking-wide group-hover:text-kim-red transition-colors">POWER</h4>
                    </a>"""
    else:
        mega_replacement = """<a href="#" class="mega-menu-item block group opacity-50 cursor-not-allowed" title="Bientôt disponible">
                        <div class="aspect-video bg-kim-gray mb-4 overflow-hidden rounded-lg flex items-center justify-center p-4 relative">
                            <div class="w-full h-full bg-gray-700"></div>
                            <div class="absolute inset-0 flex items-center justify-center bg-black/40"><span class="text-white font-sport text-xl tracking-widest">BIENTÔT</span></div>
                        </div>
                        <h4 class="font-sport font-bold text-2xl tracking-wide text-white group-hover:text-kim-red transition-colors">POWER</h4>
                    </a>"""

    content = pattern_mega.sub(mega_replacement, content)

    # --- 2. Mobile Menu Update ---
    # In the mobile menu, we might have power-125 and power-110 links, or maybe just nothing, or maybe some are missing.
    # First, let's remove any existing power-125 or power-110 links
    pattern_mob_125 = re.compile(r'<a href="[^"]*power-125\.html".*?</a\s*>\n?', re.DOTALL)
    pattern_mob_110 = re.compile(r'<a href="[^"]*power-110\.html".*?</a\s*>\n?', re.DOTALL)
    
    content = pattern_mob_125.sub('', content)
    content = pattern_mob_110.sub('', content)
    
    # Now we need to append the disabled POWER link.
    # Let's find the closing div of the grid containing the models in the mobile menu.
    # It usually looks like this: <a href="blaster.html" class="font-bold text-lg text-white">BLASTER</a>\n            </div>
    # We will inject the POWER link right before </div>
    # Wait, some pages highlight the active link (e.g. text-kim-red), let's just insert it after SPRING ST or BLASTER
    
    mob_replacement = '\n                <a href="#" class="font-bold text-lg text-gray-500 cursor-not-allowed">POWER (Bientôt)</a>\n            </div>'
    content = re.sub(r'\n\s*</div>\s*(?:</div>\s*)?<a href="[^"]*a-propos\.html"', mob_replacement + r'\n        </div>\n        <a href="' + ('../' if not is_root else '') + r'a-propos.html"', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

# Find all HTML files
html_files = glob.glob('*.html') + glob.glob('modeles/*.html')
for f in html_files:
    process_file(f)

