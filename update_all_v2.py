import os
import glob
import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Header
header_start = index_html.find('<!-- NOUVEAU MENU NAV (Plus épuré et moderne) -->')
header_end = index_html.find('</header>') + len('</header>')
header_content = index_html[header_start:header_end]

# Mobile Menu
mobile_menu_start = index_html.find('<!-- Mobile Menu -->')
main_start = index_html.find('<main')
mobile_menu_content = index_html[mobile_menu_start:main_start].strip()

# Footer
footer_start = index_html.find('<!-- Footer -->')
footer_end = index_html.find('</footer>') + len('</footer>')
footer_content = index_html[footer_start:footer_end]

def adjust_paths_for_subfolder(content):
    c = content.replace('href="index.html"', 'href="../index.html"')
    c = c.replace('href="a-propos.html"', 'href="../a-propos.html"')
    c = c.replace('href="atelier.html"', 'href="../atelier.html"')
    c = c.replace('href="contact.html"', 'href="../contact.html"')
    c = c.replace('href="catalogue.html"', 'href="../catalogue.html"')
    c = c.replace('href="devis.html"', 'href="../devis.html"')
    c = c.replace('href="modeles/', 'href="')
    c = c.replace('src="media/', 'src="../media/')
    c = c.replace('src="assets/', 'src="../assets/')
    return c

html_files = glob.glob('*.html') + glob.glob('modeles/*.html')

for filepath in html_files:
    if filepath == 'index.html' or filepath == 'index 2.html':
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace header
    h_start = content.find('<!-- NOUVEAU MENU NAV')
    if h_start == -1:
        h_start = content.find('<header')
    h_end = content.find('</header>') + len('</header>')
    
    # Replace mobile menu using regex
    m_match = re.search(r'<!-- Mobile Menu -->.*?id="close-mobile-menu".*?</button>\s*</div>\s*(</div>)?', content, re.DOTALL)
    if m_match:
        m_start = m_match.start()
        m_end = m_match.end()
    else:
        print(f"Could not find mobile menu in {filepath}")
        continue
    
    # Replace footer
    f_start = content.find('<!-- Footer -->')
    if f_start == -1:
        f_start = content.find('<footer')
    f_end = content.find('</footer>') + len('</footer>')

    if h_start != -1 and h_end != -1 and f_start != -1 and f_end != -1:
        new_header = header_content
        new_mobile = mobile_menu_content
        new_footer = footer_content
        
        if filepath.startswith('modeles/'):
            new_header = adjust_paths_for_subfolder(new_header)
            new_mobile = adjust_paths_for_subfolder(new_mobile)
            new_footer = adjust_paths_for_subfolder(new_footer)
            
        content = content[:f_start] + new_footer + "\n" + content[f_end:]
        content = content[:m_start] + new_mobile + "\n" + content[m_end:]
        content = content[:h_start] + new_header + "\n" + content[h_end:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Could not find all sections in {filepath}. h:{h_start}, f:{f_start}")

