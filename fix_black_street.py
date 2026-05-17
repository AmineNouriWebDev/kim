import re

with open('modeles/black-street.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix horizontal overflow in marquee section
content = content.replace(
    '<section class="bg-black py-0 border-y border-gray-900">',
    '<section class="bg-black py-0 border-y border-gray-900 overflow-hidden">'
)

# 2. Decrease marquee height
content = content.replace(
    '<div class="marquee-track py-6">',
    '<div class="marquee-track py-0 md:py-2">'
)

# 3. Decrease space between marquee and the next block on mobile
content = content.replace(
    '<section class="bg-kim-darker py-24 relative overflow-hidden">',
    '<section class="bg-kim-darker pt-8 pb-16 lg:py-24 relative overflow-hidden">'
)

content = content.replace(
    '<div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">',
    '<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-16 items-center">'
)

with open('modeles/black-street.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done black-street.html layout fixes")
