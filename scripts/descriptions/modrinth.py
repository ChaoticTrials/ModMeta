import os.path
import sys

import requests

import util

MOD_PAGE = 'https://modrinth.com/mod/'
PROJECT_API = 'https://api.modrinth.com/v2/project/'
MODRINTH_TOKEN = sys.argv[1]


def exists_on_modrinth(mod):
    exists = 'mr_id' in mod

    if not exists:
        print('❌ Mod not available on Modrinth')

    return exists


def update_modrinth_desc(mod, content):
    if not exists_on_modrinth(mod):
        return

    content = content.replace('{mod_hoster}', MOD_PAGE, -1)
    url = PROJECT_API + mod['mr_id']
    headers = {'Authorization': MODRINTH_TOKEN, 'User-Agent': 'GitHub@ChaoticTrials/ModMeta', 'Content-Type': 'application/json'}
    projects_data = util.get_data()
    github_base_url = projects_data.get('github', {}).get('base_url', '')
    source_url = f'{github_base_url}{mod.get('github', '')}'
    issues_url = f'{source_url}/issues'

    response = requests.patch(url, json={
        'body': content,
        'wiki_url': (projects_data['wiki_url'] + 'swl/' + util.get_default_slug(mod)) if not 'wiki_url' in mod else mod['wiki_url'],
        'source_url': source_url if github_base_url else '',
        'issues_url': issues_url if github_base_url else '',
        'discord_url': projects_data['discord_invite'] if not 'discord_invite' in mod else mod['discord_invite']
    }, headers=headers)
    if response.status_code == 204:
        print('✔️ Successfully updated Modrinth description')
    else:
        print('❌ Error updating Modrinth description: ' + response.text)


def update_modrinth_logo(logo, mod):
    if not exists_on_modrinth(mod):
        return

    data = open(logo, 'rb').read()
    if len(data) >= 262_144:
        print('❌ Logo too big, please compress')
        return

    file_type = os.path.splitext(logo)[1].lstrip('.')

    url = PROJECT_API + mod['mr_id'] + '/icon'
    params = {'ext': file_type}
    headers = {'Authorization': MODRINTH_TOKEN, 'User-Agent': 'GitHub@ChaoticTrials/ModMeta', 'Content-Type': 'image/' + file_type}

    response = requests.patch(url, params=params, data=data, headers=headers)

    if response.status_code == 204:
        print('✔️ Successfully updated Modrinth logo')
    else:
        print('❌ Error updating Modrinth logo: ' + response.text)
