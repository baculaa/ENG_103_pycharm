## AUTHOR: Alexandra Bacula
## ENG 103 base code 1

import csv
import plotly.graph_objects as go

# Read the data from the csv
def get_data_from_csv(filename):
    data_x = []
    data_y = []
    with open(filename) as file_name:
        file_read = csv.reader(file_name)
        for row in file_read:
            data_x.append(int(row[0]))
            data_y.append(int(row[1]))


if __name__ == '__main__':
    get_data_from_csv("eng103_data1.csv")