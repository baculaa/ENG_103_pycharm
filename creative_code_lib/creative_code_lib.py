## AUTHOR: Alexandra Bacula
### based on: https://plotly.com/python/shapes/

import plotly.graph_objects as go

class creative_code_lib:
    def __init__(self):
        self.fig = go.Figure()

    def plot_line_endpoints(self,start_x,start_y,end_x,end_y,line_color,line_width,dash_type):
        self.fig.add_shape(type="line",
        x0=start_x, y0=start_y, x1=end_x, y1=end_y,
        line=dict(
          color=line_color,
          width=line_width,
          dash=dash_type))

    def plot_rectangle(self,corner1_x,corner1_y,corner2_x,corner2_y,outline_color,outline_witdh,fill_color,fill_opacity):
        self.fig.add_shape(type="rect",
        x0=corner1_x, y0=corner1_y, x1=corner2_x, y1=corner2_y,
        line=dict(
          color=outline_color,
          width=outline_witdh,
        ),
        fillcolor=fill_color,
        opacity=fill_opacity,)

    def plot_circle(self,):
        pass


if __name__ == '__main__':
    creative_code_lib = creative_code_lib()
    print('hi')
