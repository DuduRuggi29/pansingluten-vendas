import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove the mobile overrides block completely
html = re.sub(r'<style id="mobile-responsive-overrides">.*?</style>', '', html, flags=re.DOTALL)

# 2. Fix scripts blocked by wp-rocket
html = html.replace('type="rocketlazyloadscript"', 'type="text/javascript"')

# 3. Fix images blocked by wp-rocket
# Remove the fake src
html = re.sub(r'src="data:image/svg\+xml;charset=utf-8,[^"]*"', '', html)
html = re.sub(r'src="data:image/svg\+xml,[^"]*"', '', html)
# Rename data-lazy-src to src
html = html.replace('data-lazy-src=', 'src=')
html = html.replace('data-lazy-srcset=', 'srcset=')
html = html.replace('data-lazy-sizes=', 'sizes=')

# Also remove the noscript wrappers for images to avoid duplicates if JS fails
html = re.sub(r'<noscript><img[^>]*></noscript>', '', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done")
