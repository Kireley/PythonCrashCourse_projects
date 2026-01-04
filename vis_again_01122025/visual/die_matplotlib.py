import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from die import Die

dies = 2

die_1 = Die()
die_2 = Die()

results = [(die_1.roll() + die_2.roll()) for i in range(10000)]
max_result = die_1.num_sides + die_2.num_sides

frequencies = [(results.count(i)) for i in range(2, max_result+1)]

x_value = list(range(2, max_result + 1))

plt.style.use('classic')

fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
ax.bar(x_value, frequencies, label='Frequencies')

plt.show()

