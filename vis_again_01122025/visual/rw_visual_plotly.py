import plotly.graph_objs as go
from plotly import offline
import plotly.express as px

from random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()
point_numbers = range(rw.num_points)


df = (0,0)
fig = px.scatter(x=rw.x_value, y=rw.y_value)
fig.show()

