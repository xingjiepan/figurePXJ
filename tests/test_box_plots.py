#!/usr/bin/env python3

import pytest
from figurePXJ import *

def test_NormalBoxPlot():
    info_dict = {'data':[[0.1, 1.1, 1.5, 1.6, 2, 3, 2.5, 2.1, 2.2, 2.3, 2.4, 5],
                        [0.5, 3, 5, 2.5]],
                 'y_min': 0,
                 'y_max': 6,
                 'style':Style('rainbow'),
                 'labels':['a', 'b'],
                 'title':'test_title',
                 'auxiliary_lines':[((1, -1), (1, -2)), ((-1, -1), (1, 2))]}
    
    nbp = NormalBoxPlot(info_dict)
    #nbp.save('test_NormalBoxPlot.png')
    nbp.show()
