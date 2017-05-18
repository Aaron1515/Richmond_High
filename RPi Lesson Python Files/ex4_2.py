import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(11, gpio.IN, gpio.PUD_UP)
gpio.setup(13, gpio.OUT)

while True:
	button_state = (gpio.input(11)==0)

# Directions: Fill in the conditions for the "if" statement below
# and the conditional code such that the light's default state is on, and 
# when the button is pressed, the LED light will turn off.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BEGIN CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

	if #button is pressed# #Remember to add colon!#
		#Enter in code to turn off LED light#
		print ("BUTTON PRESSED")
	else:
		#Enter in code for LED light's default state (on)#
		print ("CTRL+C To Exit Code!")
	time.sleep(0.5)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


gpio.cleanup()
