import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/c1cef1c4f04afa96433a2d1bcd69b2e1"></script>
<script data-cfasync="false" src="https://bauval.org/14/66f2a5ea79ecb50dd314dd2ddeaeb93d"></script>
<script>
  atOptions = {
    'key' : 'd862eb632e3108d8f52472c17d5b967f',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/d862eb632e3108d8f52472c17d5b967f"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-c1cef1c4f04afa96433a2d1bcd69b2e1"></div>
</div>'''

files = ['index.html', 'walkthrough.html', 'bosses.html', 'characters.html', 'weapons.html', 'collectibles.html', 'tips.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if 'd862eb632e3108d8f52472c17d5b967f' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-c1cef1c4f04afa96433a2d1bcd69b2e1' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')
