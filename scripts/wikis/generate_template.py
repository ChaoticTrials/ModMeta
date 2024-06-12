import os

from util import get_default_slug, get_data


def add_mod(new_mod):
    with open("mkdocs.yml", "r") as file:
        content = file.readlines()

    start_index = content.index("  - Mods:\n")
    end_index = content.index("\n", start_index + 1)

    mods = []
    for line in content[start_index + 1 : end_index]:
        if line.strip().startswith("- "):
            mods.append(line)

    mods.append(f"    - {new_mod}\n")
    mods.sort()
    content[start_index + 1: end_index] = mods

    with open("mkdocs.yml", "w") as file:
        file.writelines(content)


def main(data):
    i = 1
    mods = list(filter(lambda mod: (not os.path.exists("docs/" + mod['slug'] if type(mod['slug']) == str else mod['slug']['cf']) and 'wiki_url' not in mod), data['projects']))
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
            mr_url = f"[![]({mr_badge.format(slug)})]({mr_link + slug})"
        else:
            cf_url = f"[![]({cf_badge.format(mod['cf_id'])})]({cf_link + slug['cf']})"
            mr_url = f"[![]({mr_badge.format(slug['mr'])})]({mr_link + slug['mr']})"
    else:
        cf_url = f"[![]({cf_badge.format(mod['cf_id'])})]({cf_link + slug})"
        mr_url = ""

    github = f"[![]({github_badge.format(mod['github'])})]({github_url + mod['github']})" if "github" in mod else ""

    path = "docs/" + get_default_slug(mod)
    os.mkdir(path)
    with open(path + "/index.md", "w") as f:
        f.writelines([
            f"# {mod['name']}\n",
            f"{cf_url}\n{mr_url}\n{github}\n"
        ])

    add_mod(f"{mod['name']}: {get_default_slug(mod)}/index.md")
    print("Added to mkdocs.yml")


if __name__ == "__main__":
    main(get_data())
