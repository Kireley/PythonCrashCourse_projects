import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]
#print(plt.style.available)
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots()

ax.plot(input_values,squares, linewidth=3)
#ax.plot(squares)

#Устанавливаю заголовок и титул
ax.set_title("Квадратные числа", fontsize=14)
ax.set_xlabel('Значение', fontsize=14)
ax.set_ylabel('Значение в кв', fontsize=14)

#Устанавливаю размер лэйблов
ax.tick_params(labelsize=14)

plt.show()
