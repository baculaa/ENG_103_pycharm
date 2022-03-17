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

    def plot_rectangle(self,corner1_x,corner1_y,corner2_x,corner2_y,outline_color,outline_width,fill_color,fill_opacity):
        self.fig.add_shape(type="rect",
        x0=corner1_x, y0=corner1_y, x1=corner2_x, y1=corner2_y,
        line=dict(
          color=outline_color,
          width=outline_width,
        ),
        fillcolor=fill_color,
        opacity=fill_opacity,)

    def plot_circle(self,center_x,center_y,radius,outline_color,outline_width,fill_color,fill_opacity):
        # Calculate plotly points based on center and radius
        x0 = center_x - radius
        y0 = center_y - radius
        x1 = center_x + radius
        y1 = center_y + radius
        self.fig.add_shape(type="circle",
        x0 = x0, y0 = y0, x1 = x1, y1 = y1,
        opacity=fill_opacity,
        fillcolor=fill_color,
        line=dict(
        color=outline_color,
        width = outline_width))


if __name__ == '__main__':
    creative_code_lib = creative_code_lib()
    print('hi')
