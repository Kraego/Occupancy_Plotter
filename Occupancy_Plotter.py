from CsvReader import read_csv
import math
import numpy as np


def __calculate_robot_coordinate(alpha, l):
    alpha_rads = math.radians(alpha)
    x = math.sin(alpha_rads) * l
    y = math.cos(alpha_rads) * l
    return x, y


def transform_to_world(coords_robot, xoffset, yoffset, theta):
    points = len(coords_robot[0])
    transformed_coords_x = []
    transformed_coords_y = []
    theta_rads = math.radians(theta)

    transformation_matrix = np.array([[math.cos(theta_rads), -math.sin(theta_rads), xoffset],
                             [math.sin(theta_rads), math.cos(theta_rads), yoffset],
                             [0, 0, 1]])

    for point in range(points):
        x = coords_robot[0][point]
        y = coords_robot[1][point]
        robot_point = np.array([[x], [y], [1]])
        result = transformation_matrix.dot(robot_point)
        transformed_coords_x.append(result[0])
        transformed_coords_y.append(result[1])

    return transformed_coords_x, transformed_coords_y


def calculate_robot_coordinates(robot_data_points):
    points = len(robot_data_points[0])
    robot_coords_x = []
    robot_coords_y = []

    for point in range(points):
        alpha = robot_data_points[0][point]
        l = robot_data_points[1][point]
        coords = __calculate_robot_coordinate(alpha, l)
        robot_coords_x.append(coords[0])
        robot_coords_y.append(coords[1])

    return robot_coords_x, robot_coords_y


def calculate_coordinates_of_robot_file(filepath):
    robot_data_points = read_csv(filepath)
    return calculate_robot_coordinates(robot_data_points)


def print_roboter_subplot(pl, robot_coordinates, name, color):
    pl.add_to_robot_subplot(robot_coordinates, color, name)
