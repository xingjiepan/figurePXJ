import matplotlib.pyplot as plt
from .Figure import Figure


class ComparisionScatterPlot(Figure):
    '''A class for creating comparision scatter plots.'''
    
    def __init__(self, info_dict={}):
        super().__init__(info_dict)

    def make_plot(self):
        plt.clf()
        self.plot_ref_line()
        plt.scatter(self.info_dict['x'], self.info_dict['y'], 
                s=40, c=self.get_colors(),
                edgecolors='none')
        self.set_axes()
        self.plot_labels()
        self.plot_title()

    def plot_ref_line(self):
        min_value = min(self.info_dict['x_min'], self.info_dict['y_min'])
        max_value = max(self.info_dict['x_max'], self.info_dict['y_max'])

        plt.plot([min_value, max_value], [min_value, max_value],
                c=self.info_dict['style'].color(2))

    def get_colors(self):
        x = self.info_dict['x']
        y = self.info_dict['y']
        threshold = self.info_dict['diff_threshold']
        
        colors = []

        for i in range(len(x)):

            if y[i] > x[i] + threshold:
                colors.append(self.info_dict['style'].color(0))

            elif x[i] > y[i] + threshold:
                colors.append(self.info_dict['style'].color(1))

            else:
                colors.append(self.info_dict['style'].color(2))

        return colors
