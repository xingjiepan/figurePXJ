import numpy as np
import matplotlib.pyplot as plt

from .Figure import Figure


class GaussianKernelPlot(Figure):
    '''A class for creating a plot of smooth distributions.
       The distributions are specified in the info_dict as
       'distributions' : [([x10, x11, ...], [y10, y11, ...]), ...]
    '''

    def __init__(self, info_dict={}):
        super().__init__(info_dict)

    def make_plot(self):
        for i, distribution in enumerate(self.info_dict['distributions']):
            self.plot_one_distribution(distribution, i)

        self.set_axes()
        self.draw_auxiliary_lines()
        self.plot_labels()
        self.plot_title()

    def plot_one_distribution(self, distribution, index):
       
        # Use the Gaussian Kernel to make a smooth distribution

        x = distribution[0]
        y = distribution[1]

        new_x = np.linspace(min(x), max(x), 200)
        bin_width = (max(x) - min(x)) / 20
        new_y = np.zeros(200)

        for i in range(len(x)):
            new_y += y[i] * self.gaussian(x[i], bin_width, new_x)

        # Draw the plot

        color = self.info_dict['style'].color('normal', 'basics', index)
        
        plt.plot(new_x, new_y,
                 color=color, linewidth=4)

    def gaussian(self, mu, sigma, x):
        return 1 / np.sqrt(2 * np.pi * sigma**2) * np.exp( - (x - mu)**2 / (2 * sigma**2))
