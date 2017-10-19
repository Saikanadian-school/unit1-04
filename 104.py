#coding: utf-8

# Created by: Anthony Freeman
# Created on: September 2017
# Created for: ICS3U

import ui

def calculate_touch_up_inside(sender):

    PI = 3.14

    radius = int(view['radius'].text)

    circumference = 2 * PI * radius

    view['answer_label'].text = 'The circumference is: ' + str(circumference) + ' cm'

view = ui.load_view()
view.present('full_screen')

