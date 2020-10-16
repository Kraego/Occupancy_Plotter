from Occupancy_Plotter import print_roboter_subplot, calculate_coordinates_of_robot_file, transform_to_world
from Plotter import Plotter


if __name__ == '__main__':
    print('Initiating Occupancy_Plotter')
    pl = Plotter()

    coords_robot1 = calculate_coordinates_of_robot_file('./Testdata/robot1.csv')
    print_roboter_subplot(pl, robot_coordinates=coords_robot1, name='Robot Scan 1', color='r')
    world_data_points = transform_to_world(coords_robot1, xoffset=10, yoffset=30, theta=45)
    pl.plot_to_room(world_data_points, 'r')

    coords_robot2 = calculate_coordinates_of_robot_file('./Testdata/robot2.csv')
    print_roboter_subplot(pl, robot_coordinates=coords_robot2, name='Robot Scan 2', color='b')
    world_data_points = transform_to_world(coords_robot2, xoffset=50, yoffset=50, theta=120)
    pl.plot_to_room(world_data_points, 'b')

    coords_robot3 = calculate_coordinates_of_robot_file('./Testdata/robot3.csv')
    print_roboter_subplot(pl, robot_coordinates=coords_robot3, name='Robot Scan 3', color='g')
    world_data_points = transform_to_world(coords_robot3, xoffset=90, yoffset=40, theta=-17)
    pl.plot_to_room(world_data_points, 'g')

    pl.plot()
