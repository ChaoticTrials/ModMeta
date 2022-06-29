import os

from util import get_data, get_default_slug

data = get_data()
mods = data['projects']
i = 1
mods = list(filter(lambda mod: (not os.path.exists("docs/" + mod['slug'] if type(mod['slug']) == str else mod['slug']['cf'])), mods))
for mod in mods:
    if not os.path.exists("docs/" + mod['slug'] if type(mod['slug']) == str else mod['slug']['cf']):
        print(f"({i}) {mod['name']}")
        i += 1

selection = int(input("Which mod you want to work on? "))
mod = mods[selection - 1]

github_url: str = data['github']['base_url']
github_badge: str = data['github']['badge_url']

cf_link: str = data['curseforge']['base_url']
cf_badge: str = data['curseforge']['badge_url']

mr_link: str = data['modrinth']['base_url']
mr_badge: str = data['modrinth']['badge_url']

slug = mod['slug']

if "mr_id" in mod:
    if type(slug) == str:
        cf_url = f"[![]({cf_badge.format(mod['cf_id'])})]({cf_link + slug})"
        mr_url = f"[![]({mr_badge.format(mod['mr_id'])})]({mr_link + slug})"
    else:
        cf_url = f"[![]({cf_badge.format(mod['cf_id'])})]({cf_link + slug['cf']})"
        mr_url = f"[![]({mr_badge.format(mod['mr_id'])})]({mr_link + slug['mr']})"
else:
    cf_url = f"[![]({cf_badge.format(mod['cf_id'])})]({cf_link + slug})"
    mr_url = ""

github = f"[![]({github_badge.format(mod['github'])})]({github_url + mod['github']})" if "github" in mod else "Not available"

path = "docs/" + get_default_slug(mod)
os.mkdir(path)
with open(path + "/index.md", "w", encoding="utf-8") as f:
    f.writelines([
        f"# {mod['name']}\n",
        f"{cf_url} {mr_url} {github}\n"
    ])

print("Add this to mkdocs.yml:")
print(f"  - {mod['name']}: {get_default_slug(mod)}/index.md")
