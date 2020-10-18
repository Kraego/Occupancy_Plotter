# Occupancy_Plotter
Prints an Occupancy Grid for the given csv File.

Usage see main.

## Dependencies

* numpy: *pip install numpy*
* matplotlib: *pip install matplotlib*

## csv format:

[Angle of scan], [distance to object]

* Angle of scan ... degrees - from robots x-axis
* distance to object ... distance to object detected by LIDAR

## Todos:

* make it more generic to work with n-scans not fixed 3
* more library style move stuff from main to class
* ...