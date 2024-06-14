import ipywidgets as widgets
from read_data import *
from IPython.display import display

def create_screen(data: list):
    x_dropdown = widgets.Dropdown(options=data[0], description='X axis:')
    y_dropdown = widgets.Dropdown(options=data[0], description='Y axis:')
    plot_button = widgets.Button(description='Plot')