from random import choice


class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, number_points=5000):
        """Initilize attributes of walk"""
        self.number_points = number_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculates the points of the walk"""

        # Take steps until the walk reaches the desired length
        while len(self.x_values) < self.number_points:
            # Decide which direction to go
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate the next x and y values
            next_x = self.x_values[-1] + x_step  # Last stored value plus the step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    @staticmethod
    def get_step():
        """Method to decide which direction to go"""
        direction = choice([1, -1])  # pick one of going to the right or left || up or down
        distance = choice([0, 1, 2, 3, 4])  # pick one of how far to go
        step = direction * distance
        return step

