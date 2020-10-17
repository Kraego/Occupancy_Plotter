from CsvReader import read_csv
import math
import numpy as np


DEBUG_TRANSFORMATION = False


def __calculate_robot_coordinate(alpha, distance):
    alpha_rads = math.radians(alpha)
    x = math.sin(alpha_rads) * distance
    y = math.cos(alpha_rads) * distance
    return x, y


def transform_to_world(robot_coordinates, x_offset, y_offset, theta):
    points = len(robot_coordinates[0])
    transformed_x = []
    transformed_y = []
    theta_rads = math.radians(theta)

    transformation_matrix = np.array([[math.cos(theta_rads), -math.sin(theta_rads), x_offset],
                                      [math.sin(theta_rads), math.cos(theta_rads),  y_offset],
                                      [0,                             0,                   1]])

    for point in range(points):
        x = robot_coordinates[0][point]
        y = robot_coordinates[1][point]
        robot_point = np.array([[x], [y], [1]])
        result = np.matmul(transformation_matrix, robot_point)
        if DEBUG_TRANSFORMATION:
            print_transformation(result, robot_point, transformation_matrix)
        transformed_x.append(result[0])
        transformed_y.append(result[1])

    return transformed_x, transformed_y


def print_transformation(result, robot_point, transformation_matrix):
    print('\n#########################################' + '\n')
    print(robot_point)
    print('\n\tx\n')
    print(transformation_matrix)
    print('\n\t=\n')
    print(result)


def calculate_robot_coordinates(robot_data_points):
    points = len(robot_data_points[0])
    robot_x = []
    robot_y = []

    for point in range(points):
        alpha = robot_data_points[0][point]
        distance = robot_data_points[1][point]
        robot_point = __calculate_robot_coordinate(alpha, distance)
        robot_x.append(robot_point[0])
        robot_y.append(robot_point[1])

    return robot_x, robot_y


def calculate_coordinates_of_robot_file(filepath):
    robot_data_points = read_csv(filepath)
    return calculate_robot_coordinates(robot_data_points)


def print_roboter_subplot(pl, robot_coordinates, name, color):
    pl.add_to_robot_subplot(robot_coordinates, color, name)
