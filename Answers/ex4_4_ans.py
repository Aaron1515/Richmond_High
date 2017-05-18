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


#Directions: After setting up the bread board correctly using GPIO Pins 15 and 18
#for your LED lights and GPIO Pin 11 and 13 for your buttons, create multiple if 
#statements that will control each LED. Use the function, button_state_1 as GPIO Pin 11
#that will control the LED on GPIO PIN 15 and the function button_state_2 as GPIO Pin 13
#that will control the LED on GPIO PIN 18. From there, use If/Else statement to turn on 
#the light if the button is pressed and if the button is not pressed, then the LED light
#will be turned off

# ~~~~~~~~~~~~~~~~~~~~~~~~~ Type Code Here ~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	if button_state_1 == True :
		gpio.output(15,gpio.HIGH)
#		print('Button Pressed') 
#		time.sleep(0.2)
	else:
		gpio.output(15,gpio.LOW)
#		print('Button Not Pressed')
#		time.sleep(0.2)
	if button_state_2 == True :
		gpio.output(18,gpio.HIGH) 
		print('Button Pressed 2')
#		time.sleep(0.2)
	else:
		gpio.output(18,gpio.LOW)
		print('Button Not Pressed 2') 
#		time.sleep(0.2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End Code ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	time.sleep(0.5)
 
gpio.cleanup()

