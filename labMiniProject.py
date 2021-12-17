#By Amr Kabel

from engi1020.arduino import *
from light import *
from temperature import *
from time import *

#initial values
timer = time()
tempPin = int(input('Please input the number of the pin for the temperature sensor'))
lightPin = int(input('Please input the number of the pin for the light sensor'))
ledPin = int(input('Please input the number of the pin for the LED Light'))
buttonPin = int(input('Please input the number of the pin for the button'))
buzzerPin = int(input('Please input the number of the pin for the Buzzer'))
tempList = []
lightList = []
lcd_rgb(255,255,255)
z = False

#starting the loop
while True:
    tempRead = temp_celsius(tempPin)
    lightRead = analog_read(lightPin)
    
#filling in values in the list
    tempList.append(tempRead)
    lightList.append(lightRead)
    
#temperature
    if tempRead >= 21:
        y = high_temp(timer)
        if y == 255:
            timer = time()
            sleep(10)
            lcd_rgb(255,255,255)
      

        if tempRead <= 22:
            y = low_temp(buttonPin, buzzerPin)
            if y == 255:
                timer = time()
                sleep(10)
                lcd_rgb(255,255,255)
                
                
                
            
#time
    if time() - timer >= 30:
#low temperature
        if tempRead <= 20:
            y = low_temp(buttonPin, buzzerPin)
            if y == 255:
                timer = time()
                sleep(10)
                lcd_rgb(255,255,255)
#normal temperature
        else:
            timer = time()
            lcd_rgb(0,0,255)
            print('Watering Sytem has been activated')
            sleep(20)
            lcd_rgb(255,255,255)
            
            
#light
    if lightRead < 100 and z == False:
        low_light(ledPin)
        z = True
        
    if z == True and lightRead >= 100:
        high_light(ledPin)
        z = False
        
        
#leaving the loop
    button = digital_read(buttonPin)
    if button == 1:
        break
    
    
    
    sleep(1)
    
    
#printing lists
print('All recorded temperatures are ', tempList)
print('And all recorded light levels are ', lightList)
    