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

def fetch_repo(r):
    ''' takes URL, fetches repo data and returns as JSON '''
    if not r:
        raise 'No input string'
    else:
        response = requests.get(r).json() # fetches and converts to JSON
        if isinstance(response, list):
            return response
        else:
            raise ValueError('Bad response')

def fetch_commit(r):
    ''' takes URL, fetches commit data and returns as JSON '''
    if not r:
        raise 'No input string'
    else:
        response = requests.get(r).json() # fetches and converts to JSON
        if isinstance(response, list):
            return len(response)
        else:
            raise ValueError('Bad response')

def get_data(g):
    ''' fetches user repos '''
    try:
        repo_url = f"https://api.github.com/users/{g}/repos"
        github_data = fetch_repo(repo_url)
        d = dict()
        for i in github_data:
            commit_url = f"https://api.github.com/repos/{g}/{i}/commits"
            r = fetch_commit(commit_url)
            d[i['name']] = r
        return d
    except ValueError:
        print('Bad data.')

def main():
    ''' running main '''
    try:
        x = get_data(get_user())
        for key in x:
            print(f"Repo: {key}     Number of commits: {x[key]}")
    except ValueError:
        print('Bad data, try again.')

if __name__ == '__main__':
    main()
