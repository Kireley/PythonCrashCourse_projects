import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    ax.scatter(rw.x_value, rw.y_value, s=1)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.scatter(0,0, c='green', edgecolors='none', s=50)
    ax.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none', s=50)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("make another one? (y/n): ")
    if keep_running == "n":
        break