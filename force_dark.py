import os

ROOT = os.path.dirname(os.path.abspath(__file__))

replacements = {
    'bg-gray-50 dark:bg-kim-darker': 'bg-kim-darker',
    'bg-gray-50 dark:bg-kim-dark': 'bg-kim-dark',
    'bg-gray-50 dark:bg-black': 'bg-black',
    'bg-white dark:bg-kim-dark': 'bg-kim-dark',
    'bg-white dark:bg-kim-darker': 'bg-kim-darker',
    'text-gray-900 dark:text-gray-100': 'text-gray-100',
    'text-gray-800 dark:text-gray-200': 'text-gray-200',
    'text-gray-600 dark:text-gray-400': 'text-gray-400',
    'border-gray-200 dark:border-gray-800': 'border-gray-800',
    'border-gray-100 dark:border-gray-800': 'border-gray-800',
    'bg-white/95 dark:bg-kim-darker/95': 'bg-kim-darker/95',
    'bg-white/70 dark:bg-kim-darker/70': 'bg-kim-darker/70',
    'dark:hidden': 'hidden',
    'hidden dark:block': 'block'
}

for dirpath, _, filenames in os.walk(ROOT):
    if 'node_modules' in dirpath or '.git' in dirpath:
        continue
    for fname in filenames:
        if not fname.endswith('.html'):
            continue
        path = os.path.join(dirpath, fname)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        for old, new in replacements.items():
            content = content.replace(old, new)
            
        if content != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {fname}")
