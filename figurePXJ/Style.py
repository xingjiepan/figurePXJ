

styles = {
    'red_blue_black_light':{
        'colors':{
            'normal':{
                'basics':['#F06449', '#5BC3EB', '#DADAD9'],
                'black':['#36382E'],
                'white':['#EDE6E3'],
            },
            'intense':{
                'basics':['#C5523C', '#4BA0C1', '#B3B3B2'],
                'black':['#2D2E26'],
                'white':['#C2BDBA'],
            }
        }
    },
    
    'rainbow':{
        'colors':{
            'normal':{
                'basics':['#46237A', '#256EFF', '#3DDC97', '#FCD0A1', '#FF495C'],
                'black':['#000000'],
                'white':['#FFFFFF'],
            },
            'intense':{
                'basics':['#3A1D64', '#1F5BD1', '#32B57C', '#CFAB84', '#D13C4C'],
                'black':['#000000'],
                'white':['#FFFFFF'],
            }
        }
    },
    
}


class Style:
    '''Style defines colors, fonts and other features of a figure.'''
    def __init__(self, style_name):
        self.style = styles[style_name]

    def color(self, family, genus, species=0):
        return self.style['colors'][family][genus][species]
    
    def color_genus(self, family, genus):
        return self.style['colors'][family][genus]
