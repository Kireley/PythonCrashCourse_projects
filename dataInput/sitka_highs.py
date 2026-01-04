import matplotlib
matplotlib.use('TkAgg')
import csv
from matplotlib import pyplot as plt
from datetime import datetime
#first_date = datetime.strptime('2017-01-01', '%Y-%m-%d')
#print(first_date)
filename = 'data/sitka_weather_2018_simple.csv'
#filename = 'data/death_valley_2018_simple.csv'
def f2c (F):
    return ((F - 32) * 5 / 9)
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = f2c(int(row[5]))
        low = f2c(int(row[6]))
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    print(highs)

    print(plt.style.available)
    plt.style.use('seaborn-v0_8-colorblind')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    ax.plot(dates, lows, c='blue')

    plt.title('Daily High And Low Temperature, 2018', fontweight='bold')
    plt.xlabel('', fontsize=4)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (C)', fontsize=16)

    plt.show()