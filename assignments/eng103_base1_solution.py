## AUTHOR: Alexandra Bacula
## ENG 103 base code 1

import csv
import numpy as np
import matplotlib.pyplot as plt


class eng103_base1:

    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.ax.set(xlim=(-3, 3), ylim=(-1, 1))
        self.data_x = []
        self.data_y = []

    def read_in_data(self,filename):
        # READ IN DATA
        with open(filename) as file_name:
            file_read = csv.reader(file_name)
            for row in file_read:
                self.data_x.append(float(row[0]))
                self.data_y.append(float(row[1]))

    def set_colors(self,n):
        base_point = np.array((0,0))
        current_point = np.array((self.data_x[n],self.data_y[n]))

        dist = np.linalg.norm(base_point-current_point)

        if dist < 0.65:
            set_color = 'steelblue'
        elif dist < 1:
            set_color = 'mediumturquoise'
        elif dist < 1.5:
            set_color = 'forestgreen'
        elif dist < 2:
            set_color = 'green'
        elif dist < 2.5:
            set_color = 'royalblue'
        else:
            set_color='blueviolet'

        return set_color
# This is a custom function created to read in the CSV file data.
if __name__ == '__main__':
    base1 = eng103_base1()

    ## SET THE FILENAMES HERE
    base1.read_in_data('eng103_data1.csv')

    data_length = len(base1.data_x)
    for n in range(data_length):
        set_color = base1.set_colors(n)
        base1.scatter_plot = base1.ax.scatter(base1.data_x[n], base1.data_y[n], color=set_color)
        base1.fig.show()
        plt.title("Alexandra Bacula")
        plt.pause(0.05)

    plt.savefig('test.png')
    base1.fig.show()
    plt.pause(10)

