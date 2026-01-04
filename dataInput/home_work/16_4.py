import matplotlib
matplotlib.use('TkAgg')
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename_sitka = '../data/sitka_weather_2018_simple.csv'
filename_death = '../data/death_valley_2018_simple.csv'

def f2c (F):
    return ((F - 32) * 5 / 9)
def vals2compare (link, col_name):

    with open(link) as f:
        reader = csv.reader(f)
        header = next(reader)
        date_indx = header.index("DATE")
        value_indx = header.index(col_name)

