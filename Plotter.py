import matplotlib.pyplot as plt


class Plotter:
    def __init__(self):
        self.plotNbr = 0
        self.figure = plt.figure(constrained_layout=True)
        gs = self.figure.add_gridspec(2, 3)
        self.occupancy = self.figure.add_subplot(gs[0, :])
        self.ax0 = self.figure.add_subplot(gs[1, 0])
        self.ax1 = self.figure.add_subplot(gs[1, 1])
        self.ax2 = self.figure.add_subplot(gs[1, 2])
        self.occupancy.set_title('Occupancy Map')
        self.occupancy.grid()

    def add_to_robot_subplot(self, data, color='r', title='untitled'):
        if self.plotNbr == 0:
            axis = self.ax0
        elif self.plotNbr == 1:
            axis = self.ax1
        elif self.plotNbr == 2:
            axis = self.ax2
        else:
            raise Exception('Too many plots allowed = 3')

        axis.set_title(title)
        axis.grid()
        axis.plot(0, 0, 'x', markersize=6)
        axis.plot(data[0], data[1], color + 'o', markersize=1)
        self.plotNbr += 1

    def plot(self):
        plt.show()

    def plot_to_room(self, world_data_points, color):
        self.occupancy.plot(world_data_points[0], world_data_points[1], color + 'o', markersize=1)
