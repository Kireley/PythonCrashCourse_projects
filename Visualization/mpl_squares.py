import random

import matplotlib

matplotlib.use('TkAgg')  # You can also try 'Agg', 'Qt5Agg', or 'WebAgg' if 'TkAgg' doesn't work.
import matplotlib.pyplot as plt
x_values = [i for i in range(100)]
y_values = [i**3 for i in x_values]
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, color="black", s=5)


#ax.plot(input_values, squares, linewidth=3)
# Set chart tutle and label axes.
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Values",fontsize=13)
ax.set_ylabel("Square of Value",fontsize=13)

# Set size of tick labels.
ax.tick_params(labelsize=6)
ax.axis([0, 100, 0, 1_000_000])
ax.ticklabel_format(style="plain")
##ax.plot(squares)
plt.show()