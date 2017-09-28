# Created by: Jenny Trac
# Created on: Sept 27 2017
# This program is a recreation of Mr. Coxall's local vs. global variables program
# to demonstrate how the order of variables works

import ui

variableX = 25

def local_button_touch_up_inside(sender):
    # shows what happens with local variables
    
    variableX = 10
    variableY = 30
    variableZ = variableX + variableY
    
    view['local_label'].text = str(variableZ)

def global_button_touch_up_inside(sender):
    # shows what happens with global variables
    
    global variableX
    variableX = variableX + 1
    variableY = 30
    variableZ = variableX + variableY
    
    view['global_label'].text = str(variableZ)

view = ui.load_view()
view.present('sheet')
