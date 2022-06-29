from util import get_data

data = get_data()

wiki_url: str = data['wiki_url']

github_url: str = data['github']['base_url']
github_badge: str = data['github']['badge_url']

cf_link: str = data['curseforge']['base_url']
cf_badge: str = data['curseforge']['badge_url']

mr_link: str = data['modrinth']['base_url']
mr_badge: str = data['modrinth']['badge_url']

mods = data['projects']

table = "|Name|CurseForge|Modrinth|GitHub|\n|---|:---:|:---:|:---:|\n"

for mod in mods:
    name = mod['name']
    slug = mod['slug']
    if "mr_id" in mod:
        if type(slug) == str:
            cf_url = f"[![]({cf_badge.format(mod['cf_id'])})]({cf_link + slug})"
            mr_url = f"[![]({mr_badge.format(mod['mr_id'])})]({mr_link + slug})"
            wiki = wiki_url + slug
        else:
            cf_url = f"[![]({cf_badge.format(mod['cf_id'])})]({cf_link + slug['cf']})"
            mr_url = f"[![]({mr_badge.format(mod['mr_id'])})]({mr_link + slug['mr']})"
            wiki = wiki_url + slug['cf']
    else:
        cf_url = f"[![]({cf_badge.format(mod['cf_id'])})]({cf_link + slug})"
        mr_url = "Not available"
        wiki = wiki_url + slug

    if "wiki_url" in mod:
        wiki = mod['wiki_url']
    github = f"[![]({github_badge.format(mod['github'])})]({github_url + mod['github']})" if "github" in mod else "Not available"
    table += f"|[{name}]({wiki})|{cf_url}|{mr_url}|{github}|\n"

with open("docs/index.md", "r", encoding="utf-8") as f:
    content = f.read()

with open("docs/index.md", "w", encoding="utf-8") as f:
    f.write(content.format(table))
