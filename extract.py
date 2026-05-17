import os

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

header_start = index_html.find('<!-- NOUVEAU MENU NAV (Plus épuré et moderne) -->')
header_end = index_html.find('</header>') + len('</header>')
header_content = index_html[header_start:header_end]

mobile_menu_start = index_html.find('<!-- Mobile Menu -->')
main_start = index_html.find('<main class="min-h-screen">')
mobile_menu_content = index_html[mobile_menu_start:main_start].strip()

footer_start = index_html.find('<!-- Footer -->')
footer_end = index_html.find('</footer>') + len('</footer>')
footer_content = index_html[footer_start:footer_end]

print("Header length:", len(header_content))
print("Mobile Menu length:", len(mobile_menu_content))
print("Footer length:", len(footer_content))
