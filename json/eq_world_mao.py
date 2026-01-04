import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
#filename = './data/all_day.geojson.json'
filename = './data/all_month.geojson.json'
with open(filename, 'r', encoding='utf-8') as f:
    data = json.load(f)

headtitle = data["metadata"]['title']
print(headtitle)

all_eq_dicts = data['features']
print(len(all_eq_dicts))

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    if eq_dict['properties']['mag'] is not None:
        mags.append(eq_dict['properties']['mag'])
        lons.append(eq_dict['geometry']['coordinates'][0])
        lats.append(eq_dict['geometry']['coordinates'][1])
        eq_titles.append(eq_dict['properties']['title'])
    else:
        print(eq_dict['properties']['title'])


plotdata = [{
            'type': 'scattergeo',
            'lon': lons,
            'lat': lats,
            'text': eq_titles,
            'marker': {
                      'size': [5*mag for mag in mags],
                      'color': mags,
                        'colorscale': 'Blackbody',
                'reversescale': True,
                'colorbar': {'title':'Magnitude'},
            },
            }]
my_layout = Layout(title=headtitle)

fig = {'data': plotdata, 'layout': my_layout}
offline.plot(fig, filename='eq_world_mao.html')