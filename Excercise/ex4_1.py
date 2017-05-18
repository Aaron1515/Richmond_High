import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(11, gpio.IN, gpio.PUD_UP)
gpio.setup(13, gpio.OUT)

while True:
	button_state = (gpio.input(11)==0)

# Directions: Fill in the conditions for the "if" statement below, and fill in
# the codes for the LED lights such that the LED light is turned off in its
# default state, and when the button is pressed, the light will turn on.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BEGIN CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
	
	if #button is pressed# :
		#Enter code to have LED light turn on here from GPIO Pin 13#
		print ("BUTTON PRESSED")
	else:
		#Enter code for default LED light state (off) from GPIO Pin 13#
		print ("CTRL+C To Stop Code!")
	time.sleep(0.5)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


gpio.cleanup()
