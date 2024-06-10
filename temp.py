from scripts.wikis.util import get_data, get_default_slug

projects_data = get_data()
for mod in projects_data['projects']:
    url = f"https://legacy.curseforge.com/minecraft/mc-mods/{get_default_slug(mod)}/settings/issues"
    # webbrowser.open(url)
    if not 'cf_id' in mod or not 'github' in mod:
        continue
    print(f"{mod['name']}: {projects_data['github']['base_url'] + mod['github'] + '/issues'}")
