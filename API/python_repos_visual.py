import requests
from plotly.graph_objs import Bar
from plotly import offline
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars, labels, links = [], [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    url = repo_dict['html_url']
    link = f"<a href='{url}'>{repo_name}</a>"
    links.append(link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)



data = [{
    'type':'bar',
    'x': links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': {
        'text': 'Most-Starred Python Projects on GitHUb',
        'font': {'size': 24},
        'x': 0.5,
    },


    'xaxis': {
        'title': {
            'text': 'Repository',
            'font': {'size': 24},
        },
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': {
            'text': 'Stars',
            'font': {'size': 24},
        },
        'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')