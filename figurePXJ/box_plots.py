import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from .Figure import Figure


class NormalBoxPlot(Figure):
    '''Make a normal box plot.'''
    
    def __init__(self, info_dict={}):
        super().__init__(info_dict)

    def make_plot(self):
        
        plt.clf()

        bp = plt.boxplot(self.info_dict['data'],
                    labels=self.info_dict['labels'],
                    patch_artist=True)

        self.get_colors(bp)
        self.set_axes()
        self.plot_title()
    
    def get_colors(self, bp):
       
        normal_colors = self.info_dict['style'].color_genus('normal', 'basics') 
        intense_colors = self.info_dict['style'].color_genus('intense', 'basics') 
        black = self.info_dict['style'].color('normal', 'black')

        for i in range(len(bp['boxes'])):
        
            bp['boxes'][i].set_facecolor(normal_colors[i])
            bp['boxes'][i].set_edgecolor(intense_colors[i])
            bp['medians'][i].set_color(black)
            bp['whiskers'][2 * i].set_color(intense_colors[i])
            bp['whiskers'][2 * i +1].set_color(intense_colors[i])
            bp['caps'][2 * i].set_color(intense_colors[i])
            bp['caps'][2 * i + 1].set_color(intense_colors[i])
            bp['fliers'][i].set(marker='o', markerfacecolor=normal_colors[i], markeredgecolor='None')


