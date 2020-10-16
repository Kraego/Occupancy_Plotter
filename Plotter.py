import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


class Plotter:
    def __init__(self):
        self.plotNbr = 0
        self.figure = plt.figure(constrained_layout=True)
        gs = self.figure.add_gridspec(2, 3)
        self.occupancy = self.figure.add_subplot(gs[0, :])
        self.ax0 = self.figure.add_subplot(gs[1, 0])
        self.ax1 = self.figure.add_subplot(gs[1, 1])
        self.ax2 = self.figure.add_subplot(gs[1, 2])
        self.occupancy.set_title('Absolut Position in Room')
        self.occupancy.grid()

    def add_to_robot_subplot(self, data, color='r', title='untitled', xmin=-100, xmax=100, ymin=-100, ymax=100):
        plt.axis((xmin, xmax, ymin, ymax))
        if self.plotNbr == 0:
            axis = self.ax0
        elif self.plotNbr == 1:
            axis = self.ax1
        elif self.plotNbr == 2:
            axis = self.ax2

        axis.set_title(title)
        axis.grid()
        axis.plot(data[0], data[1], color + 'o')
        self.plotNbr += 1

    def plot(self):
        plt.show()

    def plot_to_room(self, world_data_points, color):
        self.occupancy.plot(world_data_points, color + 'o')
