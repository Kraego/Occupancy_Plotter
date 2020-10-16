from Occupancy_Plotter import print_roboter_subplot, calculate_coordinates_of_robot_file, transform_to_world
from Plotter import Plotter


if __name__ == '__main__':
    print('Initiating Occupancy_Plotter')
    pl = Plotter()

    coords_robot1 = calculate_coordinates_of_robot_file('C:/Users/tkrax/Nextcloud/Studium/WS20/Autonome Systeme/Teil Merz/Uebungen/04/robot1.csv')
    print_roboter_subplot(pl, robot_coordinates=coords_robot1, name='Robot Scan 1', color='r')
    world_data_points = transform_to_world(coords_robot1, xoffset=10, yoffset=30, theta=45)
    pl.plot_to_room(world_data_points, 'r')

    coords_robot2 = calculate_coordinates_of_robot_file('C:/Users/tkrax/Nextcloud/Studium/WS20/Autonome Systeme/Teil Merz/Uebungen/04/robot2.csv')
    print_roboter_subplot(pl, robot_coordinates=coords_robot2, name='Robot Scan 2', color='b')

    coords_robot3 = calculate_coordinates_of_robot_file('C:/Users/tkrax/Nextcloud/Studium/WS20/Autonome Systeme/Teil Merz/Uebungen/04/robot3.csv')
    print_roboter_subplot(pl, robot_coordinates=coords_robot3, name='Robot Scan 3', color='g')

    pl.plot()