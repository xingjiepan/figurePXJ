import matplotlib.pyplot as plt
from .Figure import Figure


class NormalScatterPlot(Figure):
    '''A class for creating a normal scatter plot.'''

    def __init__(self, info_dict={}):
        super().__init__(info_dict)

    def make_plot(self):
        plt.scatter(self.info_dict['x'], self.info_dict['y'],
                    s=40, c=self.get_colors(),
                    edgecolors='none')
        self.set_axes()
        self.draw_auxiliary_lines()
        self.plot_labels()
        self.plot_title()

    def get_colors(self):
        color_id = self.info_dict.setdefault('color_id', 0)
        return self.info_dict['style'].color('normal', 'basics', color_id)


class ComparisionScatterPlot(Figure):
    '''A class for creating comparision scatter plots.'''
    
    def __init__(self, info_dict={}):
        super().__init__(info_dict)

    def make_plot(self):
        plt.scatter(self.info_dict['x'], self.info_dict['y'], 
                s=40, c=self.get_colors(),
                edgecolors='none', zorder=2)
        self.plot_ref_line()
        self.set_axes()
        self.draw_auxiliary_lines()
        self.plot_labels()
        self.plot_title()

    def plot_ref_line(self):
        min_value = min(self.info_dict['x_min'], self.info_dict['y_min'])
        max_value = max(self.info_dict['x_max'], self.info_dict['y_max'])

        plt.plot([min_value, max_value], [min_value, max_value],
                c=self.info_dict['style'].color('normal', 'black'), zorder=1)

    def get_colors(self):
        x = self.info_dict['x']
        y = self.info_dict['y']
        threshold = self.info_dict['diff_threshold']
        
        colors = []

        for i in range(len(x)):

            if y[i] > x[i] + threshold:
                colors.append(self.info_dict['style'].color('normal', 'basics', 0))

            elif x[i] > y[i] + threshold:
                colors.append(self.info_dict['style'].color('normal', 'basics', 1))

            else:
                colors.append(self.info_dict['style'].color('normal', 'black'))

        return colors
