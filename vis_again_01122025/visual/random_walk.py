from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_value = [0]
        self.y_value = [0]

    def get_step(self, distance_list):
        direction = choice([-1, 1])
        distance = choice(distance_list)
        return direction * distance
    def fill_walk(self):
        while len(self.x_value) < self.num_points:

            x_step = self.get_step([0, 1, 2, 3, 4])
            y_step = self.get_step([0, 1, 2, 3, 4])

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)


