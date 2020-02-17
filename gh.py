"""
HW04A
@Author: David Tsu
for fetching github data
"""

import requests
import json

def get_data():
    ''' fetches user repos '''
    g = input("Enter GitHub ID:").lower()

    repo_url = f'https://api.github.com/users/{g}/repos'
    github_data = requests.get(repo_url).json()

    if not isinstance(github_data, list):
        raise ValueError(f"{github_data['message']}")

    d = dict()
    for i in github_data:
        commit_url = f'https://api.github.com/repos/{g}/{i}/commits'
        r = requests.get(commit_url).json()
        d[i['name']] = len(r)

    print(d)
    return d