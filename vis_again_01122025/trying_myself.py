import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots()

x_values = range(1,100)
y_values = [i**3 for i in x_values]

ax.scatter(x_values,y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# устанавливаю титулы и ярлыки
ax.set_title('Chisla d kv', fontsize=24)
ax.set_xlabel('Chisla', fontsize=14)
ax.set_ylabel('Chisla v kv', fontsize=14)

#устанавливаю тики
ax.tick_params(labelsize=14)

ax.axis([0,100,0,1_100_000])
ax.ticklabel_format(style='plain')

#если хочу сохранить плот
if input("Сохранить? y/n") == 'y':
    plt.savefig('squares_plot.png', bbox_inches='tight')
else:
    plt.show()
