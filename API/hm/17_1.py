import requests


headers = {'Accept': 'application/vnd.github.v3+json'}


lng_list = ['js', 'ruby', 'c', 'java', 'perl', 'haskell', 'go']
url_list = [f"https://api.github.com/search/repositories?q=language:{i}&sort=stars" for i in lng_list]
for url in url_list:
    r = requests.get(url, headers=headers)
    response_dict = r.json()
    print(f'Status code: {r.status_code}')
    repo_dicts = response_dict['items']
    print(f"Total repositories: {response_dict['total_count']}")
    print(f"{url}")
    print(f"Total repositories: {len(repo_dicts)}")

    print("\nSelected information about first repository:")
    for repo_dict in repo_dicts:
        print(f"======== {repo_dict['name']} ========")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Link: {repo_dict['html_url']}")
        print(f"Created: {repo_dict['created_at']}")
        print(f"Updated: {repo_dict['updated_at']}")
        print(f"Description: {repo_dict['description']}")






