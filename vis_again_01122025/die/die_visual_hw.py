from plotly.graph_objs import Bar, Layout
from plotly import offline
from vis_again_01122025.die.die import Die

dies = 2

die_1 = Die()
die_2 = Die()

results = [(die_1.roll() + die_2.roll()) for i in range(1000)]
max_result = die_1.num_sides + die_2.num_sides

frequencies = [(results.count(i)) for i in range(2, max_result+1)]



x_value = list(range(2, max_result + 1))
print(x_value)
data = [Bar(x=x_value, y=frequencies)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6 100,000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename='15-9_d6+d6.html')