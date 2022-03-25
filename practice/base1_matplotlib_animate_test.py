## AUTHOR: Alexandra Bacula
## Adapted from: https://gist.github.com/hugke729/ac3cf36500f2f0574a6f4ffe40986b4f
## ENG 103 base code 1

import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class eng103_base1:

    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.ax.set(xlim=(-3, 3), ylim=(-1, 1))


    def read_in_data(self,file1,file2):
        # READ IN DATA
        self.x = np.loadtxt(file1,delimiter=',',dtype=float)
        self.F = np.transpose(np.loadtxt(file2, delimiter=',', unpack=True, dtype=float))
        self.t = np.linspace(0, 25, np.shape(self.F)[0])

    def set_color_and_size(self,colors):
        self.scatter_plot = self.ax.scatter(self.x[::3], self.F[0, ::3], color=colors)


    def animate(self,i):
        y_i = self.F[i, ::3]
        self.scatter_plot.set_offsets(np.c_[self.x[::3], y_i])

if __name__ == '__main__':
    base1 = eng103_base1()

    ## SET THE FILENAMES HERE
    base1.read_in_data('foo.csv','foo2.csv')

    ## EDIT THE COLORS HERE
    color = 'b'
    base1.set_color_and_size((color))

    anim = FuncAnimation(base1.fig, base1.animate, interval=100, frames=len(base1.t)-1, repeat=True)
    base1.fig.show()
    anim.save('test.gif', writer='imagemagick')
