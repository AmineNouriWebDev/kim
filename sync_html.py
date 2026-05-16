import os
import re

# 1. Extract exact blocks from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract Navbar
header_match = re.search(r'(<header class=".*? w-full z-50 top-0.*? id="navbar">.*?</header>)', index_html, re.DOTALL)
if header_match:
    navbar_content = header_match.group(1)
    # Change fixed to absolute to make it scroll naturally
    navbar_content = navbar_content.replace('class="fixed ', 'class="absolute ')

# Extract Mobile Menu
mobile_menu_match = re.search(r'(<!-- Mobile Menu -->\s*<div id="mobile-menu".*?</div>)', index_html, re.DOTALL)
mobile_menu_content = mobile_menu_match.group(1) if mobile_menu_match else ""

# Extract Footer
footer_match = re.search(r'(<!-- Footer -->\s*<footer class="bg-black text-white pt-24 pb-10">.*?</footer>)', index_html, re.DOTALL)
footer_content = footer_match.group(1) if footer_match else ""

# 2. Files to process
root_files = ['atelier.html', 'contact.html', 'devis.html', 'a-propos.html', 'index.html']
model_files = [
    'modeles/pista-hr.html', 'modeles/pista-hr-plus.html', 'modeles/pista-vcx.html',
    'modeles/ghost-v7.html', 'modeles/black-street.html', 'modeles/power-spring-st.html',
    'modeles/power-125.html', 'modeles/power-110.html', 'modeles/blaster.html'
]

def replace_block(content, start_tag_regex, end_tag, new_block, fallback_insert_after=None):
    pattern = re.compile(f'({start_tag_regex}.*?{end_tag})', re.DOTALL)
    if pattern.search(content):
        return pattern.sub(new_block.replace('\\', '\\\\'), content, count=1)
    elif fallback_insert_after:
        return content.replace(fallback_insert_after, f"{fallback_insert_after}\n{new_block}")
    return content

# 3. Process each file
for file_path in root_files + model_files:
    if not os.path.exists(file_path): continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine relative prefix
    is_model = file_path.startswith('modeles/')
    
    # Adjust paths for modeles
    custom_navbar = navbar_content
    custom_mobile = mobile_menu_content
    custom_footer = footer_content
    
    if is_model:
        # Add ../ to root assets
        custom_navbar = custom_navbar.replace('href="index.html"', 'href="../index.html"')
        custom_navbar = custom_navbar.replace('href="a-propos.html"', 'href="../a-propos.html"')
        custom_navbar = custom_navbar.replace('href="atelier.html"', 'href="../atelier.html"')
        custom_navbar = custom_navbar.replace('href="contact.html"', 'href="../contact.html"')
        custom_navbar = custom_navbar.replace('href="devis.html"', 'href="../devis.html"')
        custom_navbar = custom_navbar.replace('src="media/', 'src="../media/')
        custom_navbar = custom_navbar.replace('href="modeles/', 'href="')
        
        custom_mobile = custom_mobile.replace('href="index.html"', 'href="../index.html"')
        custom_mobile = custom_mobile.replace('href="a-propos.html"', 'href="../a-propos.html"')
        custom_mobile = custom_mobile.replace('href="atelier.html"', 'href="../atelier.html"')
        custom_mobile = custom_mobile.replace('href="contact.html"', 'href="../contact.html"')
        custom_mobile = custom_mobile.replace('href="modeles/', 'href="')
        
        custom_footer = custom_footer.replace('href="index.html"', 'href="../index.html"')
        custom_footer = custom_footer.replace('href="a-propos.html"', 'href="../a-propos.html"')
        custom_footer = custom_footer.replace('href="atelier.html"', 'href="../atelier.html"')
        custom_footer = custom_footer.replace('href="contact.html"', 'href="../contact.html"')
        custom_footer = custom_footer.replace('src="media/', 'src="../media/')

    # Replace Navbar
    content = replace_block(content, r'<header class=".*? w-full z-50 top-0.*?" id="navbar">', r'</header>', custom_navbar, '<body...>')
    
    # Replace Mobile Menu
    content = replace_block(content, r'<!-- Mobile Menu -->\s*<div id="mobile-menu"', r'</div>\s*</div>', custom_mobile)
    if 'id="mobile-menu"' not in content: # Fallback if replace failed due to mismatched tags
         content = replace_block(content, r'<!-- Mobile Menu -->\s*<div id="mobile-menu"', r'</button>\s*</div>', custom_mobile)
         
    if 'id="mobile-menu"' not in content:
        content = content.replace('</header>', f'</header>\n\n    {custom_mobile}')

    # Replace Footer
    content = replace_block(content, r'<!-- Footer -->\s*<footer', r'</footer>', custom_footer)
    if '<footer' not in content:
        content = content.replace('</main>', f'</main>\n\n    {custom_footer}')
        
    # Specific fixes
    if file_path == 'a-propos.html':
        content = content.replace('media/logo-groupe-kaddeche.png', 'media/kim-group/logo-groupe-kaddeche.png')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Sync completed.")
