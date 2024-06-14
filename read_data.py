import csv
from os import listdir
import matplotlib.pyplot as plt

def read_from_csv_to_data(filepath: str):
    if isinstance(filepath, str) == False:
        raise TypeError(f'{filepath} is not a string')

    if listdir().__contains__(filepath) == False:
        raise FileNotFoundError(f'{filepath} does not exist in the directory')

    data = list(csv.reader(open(filepath)))

    return data

def generate_graph(x_index: int, y_index: int, data: list, label_index = 17):
    if isinstance(data, list) == False or isinstance(data[0],list) == False:
        raise TypeError(f'{data} must be a 2d list')


    x_with_parksinson = get_values_by_label(data[1:], x_index, 1, label_index)
    y_with_parkinson = get_values_by_label(data[1:], y_index, 1, label_index)
    x_without_parksinson = get_values_by_label(data[1:], x_index, 0, label_index)
    y_without_parkinson = get_values_by_label(data[1:], y_index, 0, label_index)
    x_axis_label = data[0][x_index]
    y_axis_label = data[0][y_index]
    plt.scatter(x_with_parksinson, y_with_parkinson, color='red', label='With Parkinson')
    plt.scatter(x_without_parksinson, y_without_parkinson, color='blue',label='Without Parkinson')
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.legend()
    plt.tight_layout()
    
    plt.show()

def get_values_by_label(data: list,value_index: int, label: int, label_index: int):
    values = []
    for row in data:
        if int(row[label_index]) == label:
            values.append(float(row[value_index]))
    return values