import json

filename = './data/eq_1_day_m1.json'
with open(filename) as f:
    data = json.load(f)

all_eq_dicts = data['features']
print(len(all_eq_dicts))
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(lons[:10])
print(lats[:10])