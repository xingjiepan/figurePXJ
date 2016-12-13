import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


class Figure:
    '''Base class for figures.'''
    def __init__(self, info_dict={}):
        self.info_dict = info_dict

    def show(self):
        self.make_plot()
        plt.show()

    def save(self, path):
        self.make_plot()
        plt.savefig(path)

    def set_axes(self):
        plt.axis([self.info_dict['x_min'],
                  self.info_dict['x_max'],
                  self.info_dict['y_min'],
                  self.info_dict['y_max']])

    def plot_labels(self):
        font = FontProperties()
        font.set_family('sans-serif')
        font.set_size('x-large')

        plt.xlabel(self.info_dict['x_label'], fontproperties=font)
        plt.ylabel(self.info_dict['y_label'], fontproperties=font)

    def plot_title(self):
        font = FontProperties()
        font.set_family('sans-serif')
        font.set_size('xx-large')
        #font.set_weight('bold')
        
        plt.title(self.info_dict['title'], fontproperties=font)
