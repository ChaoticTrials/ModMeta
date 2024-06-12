import os

from util import get_data

data = get_data()

mods = data['projects']

for mod in mods:
    slug = mod['slug'] if type(mod['slug']) == str else mod['slug']['cf']
    if "wiki_url" not in mod and not os.path.exists("docs/" + slug):
        os.mkdir("docs/" + slug)
        with open("docs/" + slug + "/index.md", "w") as f:
            f.writelines([
                f"# {mod['name']}\n",
                "\n",
                "This mod was not even started to be worked on, sorry!\n"
            ])
