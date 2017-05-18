import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(11, gpio.OUT)


# Directions: Use the comparison operator ">" to create a True 
# statement for the while loop. After, try using "<" too.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BEGIN CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
	
	gpio.output(11, gpio.HIGH)
	time.sleep(0.5)
	gpio.output(11, gpio.LOW)
	time.sleep(0.5)
	print("CTRL+C to stop this code")

gpio.cleanup()
