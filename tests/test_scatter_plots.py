#!/usr/bin/env python3

import pytest
from figurePXJ import *

def test_ComparisionScatterPlot():
    info_dict = {'x':[1, 2, 3, 2.5],
                 'y':[0.5, 3, 5, 2.5],
                 'x_min':0,
                 'x_max':10,
                 'y_min':0,
                 'y_max':10,
                 'diff_threshold':0.1,
                 'style':Style('red_blue_black_light'),
                 'x_label':'test_x',
                 'y_label':'test_y',
                 'title':'test_title',
                 'auxiliary_lines':[((1, -1), (1, -2)), ((-1, -1), (1, 2))]}
    
    csp = ComparisionScatterPlot(info_dict)
    #csp.save('test_ComparisionScatterPlot.png')
    csp.show()
