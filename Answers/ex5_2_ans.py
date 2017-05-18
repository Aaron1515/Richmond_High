import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False) 

gpio.setup(11, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(13, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(15, gpio.OUT)
gpio.setup(18, gpio.OUT) 

while True:
	button_state_1 = (gpio.input(11)==0)
	button_state_2 = (gpio.input(13)==0)


#Directions: Below is the code from the last exercise. Add on to the code with a new 
#if-else statement and using an "or" statement to turn your second LED light (connected
#to GPIO Pin 18) turn on if either button 1 or button 2 is pressed. Note that when both
#are pressed, both LED lights should turn on.

# ~~~~~~~~~~~~~~~~~~~~~~~~~ Type Code Here ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

	if button_state_1 == True and button_state_2 == True:
		gpio.output(15, gpio.HIGH)
		gpio.output(18, gpio.HIGH)
		
	else:
		gpio.output(15, gpio.LOW)
		gpio.output(18, gpio.LOW)
		

	if button_state_1 == True or button_state_2 == True:
		gpio.output(18, gpio.HIGH)
	else:
		gpio.output(18, gpio.LOW)
		gpio.output(15, gpio.LOW)
		

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End Code ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
	time.sleep(0.5)
	print("Ctrl + C to stop code!")
 
gpio.cleanup()
