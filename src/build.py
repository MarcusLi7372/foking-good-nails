"""Builds ../index.html from site.html: inlines the logo and photos as data URIs
and wraps the page in a full HTML document so it can be hosted anywhere (Vercel, GitHub Pages)."""
import base64, re, os
here = os.path.dirname(os.path.abspath(__file__))
p = lambda *a: os.path.join(here, *a)
s = open(p('site.html')).read()
b64 = lambda f: 'data:image/webp;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
s = s.replace('LOGO_DATA', b64(p('logo.webp')))
for m in set(re.findall(r"PH_([a-z\-]+)", s)):
    s = s.replace("'PH_" + m + "'", "'" + b64(p('photos', m + '.webp')) + "'")
assert 'PH_' not in s
title = re.search(r'<title>.*?</title>', s).group(0)
s = s.replace(title, '', 1)
html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
{title}
<meta name="description" content="Custom hand-painted press-on nails from Vaughan, ON. Design your set in 3D and order with your inspo.">
<link rel="icon" href="{b64(p('logo.webp'))}">
</head>
<body style="margin:0">
{s}
</body>
</html>
'''
open(p('..', 'index.html'), 'w').write(html)
print(len(html) // 1024, 'KB')
