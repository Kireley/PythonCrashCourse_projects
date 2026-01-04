import matplotlib
matplotlib.use('TkAgg')
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'

def f2c (F):
    return ((F - 32) * 5 / 9)

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = f2c(int(row[4]))
            low = f2c(int(row[5]))
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)



    plt.style.use('seaborn-v0_8-colorblind')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    ax.plot(dates, lows, c='blue')
    title = 'Daily High And Low Temperature, 2018\nDeath Valley, Ca'
    plt.title(title, fontweight='bold')

    plt.xlabel('', fontsize=4)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (C)', fontsize=16)

    plt.show()