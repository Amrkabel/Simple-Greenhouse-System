#By Amr Hamdy Kabel

from time import *
from engi1020.arduino import *

"""
When called, it waters the plants due to high temperature

Parameters:
    z - The time since the last time the plant was watered.
    
Returns:
    y - The value of blue in the rgb
"""
def high_temp(z):
    x = time() - z
    if x < 30:
        return
    elif x >= 30:
        y = 255
        lcd_rgb(0,0,y)
        print("Watering started due to high temperature")
        return y

"""
When called, it prevents the plant to be watered due to low temperature, unless the user clicks the button

Parameters:
    button - the pin where the button is attached
    buzzer - the pin where the buzzer is attached
    
Returns:
    y - The value of blue in the rgb
"""
def low_temp(button, buzzer):
    print('Temperature is too low. Please check if the water is frozen before pressing the button')
    digital_write(buzzer, 1)
    while True:
        x = digital_read(button)
        if x == 1:
            digital_write(buzzer,0)
            break
    lcd_rgb(0,0,255)
    y = 255
    return y