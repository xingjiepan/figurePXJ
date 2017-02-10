import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

from .Figure import Figure


class SmoothCurvePlot(Figure):
    '''A class for creating a plot of smooth curves.
       The curves are specified in the info_dict as
       'curves' : [([x10, x11, ...], [y10, y11, ...]), ...]
    '''

    def __init__(self, info_dict={}):
        super().__init__(info_dict)

    def make_plot(self):
        for i, curve in enumerate(self.info_dict['curves']):
            self.plot_one_curve(curve, i)

        self.set_axes()
        self.draw_auxiliary_lines()
        self.plot_labels()
        self.plot_title()

    def plot_one_curve(self, curve, index):
       
        # Interpolate the input points to get a smooth curve

        x = curve[0]
        y = curve[1]

        interpolate_curve = interp1d(x, y, kind='cubic')

        new_x = np.linspace(min(x), max(x), 200)
        new_y = interpolate_curve(new_x)

        # Draw the plot

        color = self.info_dict['style'].color('normal', 'basics', index)
        
        plt.plot(new_x, new_y,
                 color=color, linewidth=4)

