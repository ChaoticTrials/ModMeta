import json
import os

with open("data/projects.json", "r", encoding="utf-8") as f:
    data = json.loads(f.read())

mods = data['projects']

for mod in mods:
    slug = mod['slug'] if type(mod['slug']) == str else mod['slug']['cf']
    if "wiki_url" not in mod and not os.path.exists("docs/" + slug):
        os.mkdir("docs/" + slug)
        with open("docs/" + slug + "/index.md", "w", encoding="utf-8") as f:
            f.writelines([
                "# " + mod['name'] + "\n",
                "\n",
                "This mod was not even started to be worked on, sorry!\n"
            ])
