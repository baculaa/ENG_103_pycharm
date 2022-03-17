import matplotlib.pyplot as plt

class creativecode_lib:
    def __init__(self):
        pass
    def plot_circle(self,center_x,center_y,radius):
        plt.axes()
        circle = plt.Circle((center_x, center_y), radius, fc='y')
        plt.gca().add_patch(circle)
        plt.axis('scaled')
        plt.show()

if __name__ == '__main__':
    creativecode = creativecode_lib()
    creativecode.plot_circle(0,0,5)