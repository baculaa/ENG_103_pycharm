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

    def plot_rectangle(self,corner1_x,corner1_y,corner2_x,corner2_y):
        pass

if __name__ == '__main__':
    creative_code_lib = creative_code_lib()
    print('hi')
