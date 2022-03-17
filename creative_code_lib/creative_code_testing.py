import creative_code_lib

print('')

if __name__ == '__main__':
    creative_code = creative_code_lib.creative_code_lib()
    # TESTING FUNCTIONS #
    ## Plot a line using endpoints
    # INPUTS: start_x, start_y, end_x, end_y, color, width, line type
    creative_code.plot_line_endpoints(0,0,1,1,'blue',4,'dash')

    ## Plot a second line
    creative_code.plot_line_endpoints(3, 3, 1, 1, 'green',9, 'solid')


    ## Update the figure
    creative_code.fig.update_shapes(dict(xref='x', yref='y'))
    creative_code.fig.show()