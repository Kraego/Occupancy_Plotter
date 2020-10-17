from Occupancy_Plotter import print_roboter_subplot, calculate_coordinates_of_robot_file, transform_to_world
from Plotter import Plotter


if __name__ == '__main__':
    print('Initiating Occupancy_Plotter')
    pl = Plotter()

    robot1_coordinates = calculate_coordinates_of_robot_file('./Testdata/robot1.csv')
    print_roboter_subplot(pl, robot_coordinates=robot1_coordinates, name='Robot Scan 1', color='r')
    world_data_points = transform_to_world(robot1_coordinates, x_offset=10, y_offset=30, theta=45)
    pl.plot_to_room(world_data_points, 'r')

    robot2_coordinates = calculate_coordinates_of_robot_file('./Testdata/robot2.csv')
    print_roboter_subplot(pl, robot_coordinates=robot2_coordinates, name='Robot Scan 2', color='b')
    world_data_points = transform_to_world(robot2_coordinates, x_offset=50, y_offset=50, theta=120)
    pl.plot_to_room(world_data_points, 'b')

    robot3_coordinates = calculate_coordinates_of_robot_file('./Testdata/robot3.csv')
    print_roboter_subplot(pl, robot_coordinates=robot3_coordinates, name='Robot Scan 3', color='g')
    world_data_points = transform_to_world(robot3_coordinates, x_offset=90, y_offset=40, theta=-17)
    pl.plot_to_room(world_data_points, 'g')

    pl.plot()
