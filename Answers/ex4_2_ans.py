import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(11, gpio.IN, gpio.PUD_UP)
gpio.setup(13, gpio.OUT)

while True
	button_state = (gpio.input(11)==0)

# Directions: Fill in the conditions for the "if" and "then" statements below
# and the conditional code such that the light's default state is on, and 
# when the button is pressed, the LED light will turn off.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BEGIN CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

	if button_state == True:
		gpio.output(13, gpio.LOW)
		print ("BUTTON PRESSED")
	else:
		gpio.output(13, gpio.HIGH)
		print ("CTRL+C To Stop Code!")
	time.sleep(0.5)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


gpio.cleanup()
