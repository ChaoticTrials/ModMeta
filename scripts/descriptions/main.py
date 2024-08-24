import os
import subprocess

import util
from modrinth import update_modrinth_desc, update_modrinth_logo

BASE_URL = 'https://raw.githubusercontent.com/ChaoticTrials/ModMeta/HEAD/'
DIR = 'assets/mods/'


def update_logo(path, mod):
    logo = os.path.join(path, 'logo.png')
    if not os.path.exists(logo):
        logo = os.path.join(path, 'logo.gif')
        if not os.path.exists(logo):
            print('❌ Logo')
            return

    if not logo_changed(logo):
        print('❌ Logo didn\'t change. Skipping.')
        return

    update_modrinth_logo(logo, mod)
    # update_curseforge_logo(logo, mod) todo
    print('✔️ Logo')


def update_desc(path, mod):
    desc = os.path.join(path, 'desc.md')
    if not os.path.exists(desc):
        print('❌ Description')
        return

    with open(desc, 'r') as f:
        content = f.read()

    content = important_information(content)

    print('🧾 Description')
    content += '\nYou are allowed to put this mod in any modpack you like.\n'
    for image in os.listdir(path):
        if is_image(image):
            if image == 'promo.png':
                content += f'![[Werbung](https://www.bisecthosting.com/melanx)]({image_url(path, image)})\n#Werbung #Ad'
                print('✔️ Promo')
                continue

            title = image.rsplit(".", 1)[0].replace("_", " ").title()
            old = content
            content = content.replace('{' + image + '}', f'![{title}]' +
                                      f'({image_url(path, image)})')
            if old is not content:
                print(f'✔️ {title}')
    recipes = os.path.join(path, 'recipes')
    if os.path.exists(recipes):
        images_str = '<details>\n<summary>Click to expand</summary>\n\n'
        for recipe in sorted(os.listdir(recipes)):
            images_str += f'**{recipe.split(".")[0].replace("_", " ").title()}**\n\n'
            images_str += f'![{recipe.rsplit(".", 1)[0].replace("_", " ").title()} Recipe]({image_url(recipes, recipe)})\n\n'
        images_str += '</details>\n\n'
        content = content.replace('{recipe_images}', images_str)
        print('✔️ Example Recipes')

    print('✔️ Full Desc')
    update_modrinth_desc(mod, content)
    # update_curseforge_desc(mod, content) todo


def something_changed(path):
    with open('latest.txt', 'r') as f:
        hash = f.readline().rstrip("\n")
        cmd = (f'git diff --name-only {hash} -- '
               f'{path} ' # if some information in the mod itself changed, update
               f'assets/important_notes.md ' # if the header information changed, update everything
               f'data/projects.json') # if something changed in the metadata, update everything
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
        changed_files = result.stdout.decode().splitlines()

    return len(changed_files) > 0


def logo_changed(path):
    with open('latest.txt', 'r') as f:
        hash = f.readline().rstrip("\n")
        cmd = f'git diff --name-only {hash} -- {path}'
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
        changed_files = result.stdout.decode().splitlines()

    return len(changed_files) > 0


def main():
    for mod in util.get_data()['projects']:
        slug = util.get_default_slug(mod)
        print(f'🔄️ Updating project pages for {mod["name"]}.')
        path = os.path.join(DIR, slug)
        if not os.path.exists(path):
            print(f'❌❌❌ No assets found. Skipping. ❌❌❌')
            print()
            continue

        if not something_changed(path):
            print('❌❌❌ No changes detected. Skipping. ❌❌❌')
            print()
            continue

        update_logo(path, mod)
        update_desc(path, mod)

        print(f'✔️ Finished {mod["name"]}')
        print()


def important_information(content: str):
    with open('assets/important_notes.md', 'r') as f:
        data = f.read()

    if data.strip() != '':
        content = data + content

    return content


def is_image(file: str):
    return file.lower().endswith('.png') or file.lower().endswith('.gif')


def image_url(path, file):
    full_path = os.path.join(path, file).replace('\\', '/')
    if os.path.exists(full_path):
        return BASE_URL + str(full_path)

    if full_path.endswith('.png'):
        full_path = full_path[:len(full_path) - 3] + 'gif'
        if os.path.exists(full_path):
            return BASE_URL + full_path

    return None


if __name__ == '__main__':
    main()
