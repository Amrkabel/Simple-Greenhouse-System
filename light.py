#By Amr Kabel

from time import *
from engi1020.arduino import *

"""
Turns on the lights

Parameters:
    pin - the pin where the lights are connected
"""
def low_light(pin):
    print('Lights will be turned on due to low light levels')
    digital_write(pin, 1)
    return

"""
Turns off the lights

Parameters:
    pin - the pin where the lights are connected
"""
def high_light(pin):
    print('Lights will be turned off due to high light levels')
    digital_write(pin, 0)
    return