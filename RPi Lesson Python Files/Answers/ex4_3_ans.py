import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(11, gpio.IN, gpio.PUD_UP)
gpio.setup(13, gpio.OUT)

while True:
	button_state = (gpio.input(11)==0)

# Directions: Fill in the conditions for the "if" and "then" statements below
# and the conditional code such that when the button is held down, the LED 
# light will blink 3 times.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BEGIN CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

	if button_state == True:
		for i in range(3):
			gpio.output(13, gpio.HIGH)
			time.sleep(0.5)
			gpio.output(13, gpio.LOW)
			time.sleep(0.5)
		print ("BUTTON PRESSED")
	else:
		gpio.output(13, gpio.LOW)
		print ("Button is not pressed")
	time.sleep(0.5)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


gpio.cleanup()
