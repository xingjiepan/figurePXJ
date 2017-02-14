#!/usr/bin/env python3

import pytest
from figurePXJ import *


def test_SmoothCurvePlot():
    info_dict = {'distributions' : [([1, 2, 3, 2.5], [0.5, 3, 5, 2.5]),
                             ([1, 3, 5, 7, 9], [1, 9, 1, 4, 6])],
                 'x_min':0,
                 'x_max':10,
                 'y_min':0,
                 'y_max':10,
                 'style':Style('red_blue_black_light'),
                 'x_label':'test_x',
                 'y_label':'test_y',
                 'title':'test_title',
                 'auxiliary_lines':[((1, -1), (1, -2)), ((-1, -1), (1, 2))]}

    scp = GaussianKernelPlot(info_dict)
    scp.show()


