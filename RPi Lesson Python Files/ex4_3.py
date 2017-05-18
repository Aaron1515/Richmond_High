import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(11, gpio.IN, gpio.PUD_UP)
gpio.setup(13, gpio.OUT)

while True:
	button_state = (gpio.input(11)==0)

# Directions: Fill in the conditions for the "if" and "then" statements below
# and the code such that when the button is held down, the LED 
# light will blink 3 times.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BEGIN CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

	if #button is pressed# :
		#Add for loop to make LED light blink 3 times here#
		print ("BUTTON PRESSED")
	else:
		#Code for default state of LED light (off)#
		print ("Button is not pressed")
	time.sleep(0.5)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


gpio.cleanup()
