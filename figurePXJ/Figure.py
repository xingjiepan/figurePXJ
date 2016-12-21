import numpy as np
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
        x_min, x_max, y_min, y_max = plt.axis()
        
        x_min = self.info_dict.setdefault('x_min', x_min)
        x_max = self.info_dict.setdefault('x_max', x_max)
        y_min = self.info_dict.setdefault('y_min', y_min)
        y_max = self.info_dict.setdefault('y_max', y_max)

        plt.axis([x_min, x_max, y_min, y_max])

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

    def draw_auxiliary_lines(self):
        '''Draw auxiliary lines specified by users.
           The format in the info_dict is:
           'auxiliary_lines' : [ ((x1,y1), (x2,y2)), ... ]
        '''
        for line in self.info_dict.setdefault('auxiliary_lines', []):
            self.draw_one_auxiliary_line(np.array(line[0]), np.array(line[1]))

    def draw_one_auxiliary_line(self, p1, p2):
        '''Draw one axuilary line given two points.
           p1 and p2 are numpy arrays.
        '''
        x_min, x_max, y_min, y_max = plt.axis()
        
        # Get the vector of the line

        v = p2 - p1

        if v[0] == 0 and v[1] == 0: raise Exception("Zero vector")

        # Get the upper point to draw the line

        scale_up = ((x_max - p1[0]) / v[0]) if v[0] != 0 \
                    else (y_max - p1[1]) / v[1]

        p_up = p1 + scale_up * v

        # Get the lower point to draw the line

        scale_low = ((x_min - p1[0]) / v[0]) if v[0] != 0 \
                    else (y_min - p1[1]) / v[1]

        p_low = p1 + scale_low * v

        # Draw the line
       
        xy = list(zip(p_up, p_low))

        plt.plot(xy[0], xy[1], '--', color=self.info_dict['style'].color('normal', 'black'))

