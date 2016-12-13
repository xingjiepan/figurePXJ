

styles = {
    'red_blue_black_light':{
        'colors':['#F06449', '#5BC3EB', '#36382E', '#DADAD9', '#EDE6E3']
    }
    
}


class Style:
    '''Style defines colors, fonts and other features of a figure.'''
    def __init__(self, style_name):
        self.style = styles[style_name]

    def color(self, color_index):
        return self.style['colors'][color_index]
