"""
HW04A
@Author: David Tsu
for fetching github data
"""

import requests

def get_user():
    ''' fetches username '''
    g = input("Enter GitHub ID:").lower()
    return g

def get_data(g):
    ''' fetches user repos '''
    try:
        repo_url = f"https://api.github.com/users/{g}/repos"
        github_data = requests.get(repo_url).json() # fetches and converts to JSON
        d = dict()
        for i in github_data:
            commit_url = f"https://api.github.com/repos/{g}/{i}/commits"
            r = requests.get(commit_url).json() # fetches and converts to JSON
            d[i['name']] = len(r)
        return d
    except ValueError:
        print('Bad data.')