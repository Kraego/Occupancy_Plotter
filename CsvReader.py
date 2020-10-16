import csv

CSV_DELIMITER = ','

'''
    Read csv file, in Format 
    "x1,y1
    x2,y2"

    :param path: path to the csv
    :return: tuple(list[x], list[y]] 
'''
def read_csv(path):
    data_points = []

    with open(path, encoding='utf-8-sig') as csv_file:
        print('Read csv file "{}"', csv_file)
        row_reader = csv.reader(csv_file, delimiter=CSV_DELIMITER, quotechar='|', )
        x_values = []
        y_values = []

        for row in row_reader:
            x_values.append(float(row[0]))
            y_values.append(float(row[1]))
        data_points.append(x_values)
        data_points.append(y_values)
    return data_points
