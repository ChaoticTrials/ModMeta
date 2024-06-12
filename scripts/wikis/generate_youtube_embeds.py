import os

from util import get_data, get_default_slug

data = get_data()

mods = data['projects']

for mod in mods:
    if 'yt_video' in mod:
        slug = get_default_slug(mod)
        if os.path.exists('docs/' + slug):
            file = f'docs/{slug}/index.md'
            if os.path.exists(file):
                with open(file, 'r') as f:
                    content = f.read()
                    is_short = mod['yt_video']['type'] == 'short'
                    width = '451' if is_short else '801'
                    height = '801' if is_short else '451'
                    content = content.replace('{yt_video}',
                                              f'<div class="video-wrapper"><iframe width="{width}" height="{height}" '
                                              f'src="https://www.youtube.com/embed/{mod["yt_video"]["id"]}" '
                                              f'title="Excavar" frameborder="0" allow="accelerometer; autoplay; '
                                              f'clipboard-write; encrypted-media; gyroscope; picture-in-picture; '
                                              f'web-share" allowfullscreen></iframe></div>')

                with open(file, 'w') as f:
                    f.write(content)
