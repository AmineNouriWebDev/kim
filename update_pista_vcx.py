import re

with open('modeles/pista-vcx.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix horizontal overflow
content = content.replace(
    '<section class="bg-black py-0 border-y border-gray-900">',
    '<section class="bg-black py-0 border-y border-gray-900 overflow-hidden">'
)

# Remove py-6 from marquee-track
content = content.replace(
    '<div class="marquee-track py-6">',
    '<div class="marquee-track">'
)

# Remove .marquee-item from the slash separator so it doesn't get massive paddings
content = content.replace(
    '<div class="marquee-item"><span class="text-gray-800 text-2xl">/</span></div>',
    '<span class="text-gray-800 text-2xl px-4 md:px-6 flex items-center shrink-0">/</span>'
)

with open('modeles/pista-vcx.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done pista-vcx.html fixes")
