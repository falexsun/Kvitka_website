import re

def fix_nav_links(filepath, is_main=False):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Prefix for nav links
    prefix = "" if is_main else "kvitka-light.html"
    
    nav_replacements = [
        ('href="#news"', f'href="{prefix}#news"'),
        ('href="#video"', f'href="{prefix}#video"'),
        ('href="#gallery"', f'href="{prefix}#gallery"'),
        ('href="#bio"', f'href="{prefix}#bio"'),
        ('href="#initiatives"', f'href="{prefix}#initiatives"'),
        ('href="#press"', f'href="{prefix}#press"')
    ]
    
    for old, new in nav_replacements:
        content = content.replace(old, new)
        
    with open(filepath, 'w') as f:
        f.write(content)

fix_nav_links('kvitka-light.html', True)
fix_nav_links('biography.html', False)
fix_nav_links('albums.html', False)
