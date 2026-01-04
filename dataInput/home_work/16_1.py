import matplotlib
matplotlib.use('TkAgg')
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = '../data/sitka_weather_2018_simple.csv'


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:

            high = row[3]

        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
    print(highs)



    plt.style.use('seaborn-v0_8-colorblind')
    fig, ax = plt.subplots()
    ax.plot(dates[::15], highs[::15], c='red')

    title = 'Daily High And Low Temperature, 2018\nDeath Valley, Ca'
    plt.title(title, fontweight='bold')

    plt.xlabel('', fontsize=4)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (C)', fontsize=16)

    plt.show()