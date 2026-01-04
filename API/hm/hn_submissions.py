from operator import itemgetter
import requests
from plotly.graph_objs import Bar
from plotly import offline


url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()

comments, titles, links = [], [], []
for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)

    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
        comment = response_dict['descendants']
        title = response_dict['title']
        link = f"http://news.ycombinator.com/item?id={submission_id}"

    except: KeyError

    comments.append(comment)
    titles.append(title)
    links.append(link)
sorted_by_age = sorted(zip(names, ages), key=lambda x: x[1])
data = [{
    'type':'bar',
    'x': titles,
    'y': comments,
    'hovertext': links,
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
offline.plot(fig, filename='coms.html')
