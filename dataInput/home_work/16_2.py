import matplotlib
matplotlib.use('TkAgg')
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename_sitka = '../data/sitka_weather_2018_simple.csv'
filename_death = '../data/death_valley_2018_simple.csv'
filename_sf = '../data/4187591.csv'

def f2c (F):
    return ((F - 32) * 5 / 9)
def vals2compare (link, col_name):

    with open(link) as f:
        reader = csv.reader(f)
        header = next(reader)
        date_index = header.index("DATE")
        vals_index = header.index(col_name)
        for i, r in enumerate(header):
            print(i, r)

        dates, temps = [], []

        for row in reader:
            date = datetime.strptime(row[date_index], '%Y-%m-%d')

            try:
                temp = f2c(int(row[vals_index]))
                print(temp)
            except ValueError:
                print(f'Shiet data in {date} is invalid')
            else:
                dates.append(date)
                temps.append(temp)
        paired = list(zip(dates, temps))
        paired.sort(key=lambda x: x[0])

        dates, temps = zip(*paired)
    return dates, temps
sitka_data = vals2compare(filename_death, 'TMAX')
death_data = vals2compare(filename_sitka, 'TMAX')
sf_data = vals2compare(filename_sf, 'TMAX')


plt.style.use('seaborn-v0_8-colorblind')
fig, ax = plt.subplots()
numbr = 2
print(len(death_data[0]))
print(len(sf_data[0]))
ax.plot(sitka_data[0][::numbr], sitka_data[1][::numbr], c='red')
ax.plot(death_data[0][::numbr], death_data[1][::numbr], c='blue')
ax.plot(sf_data[0][::numbr], sf_data[1][::numbr], c='green')
title = 'Daily High And Low Temperature, 2018\nDeath Valley, Ca'
plt.title(title, fontweight='bold')

plt.xlabel('', fontsize=4)
fig.autofmt_xdate()
plt.ylabel('Temperature (C)', fontsize=16)

plt.show()