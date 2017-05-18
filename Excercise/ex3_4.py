import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(11, gpio.OUT)


# Directions: Define variables using the "=" sign and use the "==" sign to
# make a comparison to form a True statement. Define the variable x as 2, 
# and a variable y as 1+1. Then compare the variables using "==" for the
# while loop. 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BEGIN CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

x = 
y =  




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
	
	gpio.output(11, gpio.HIGH)
	time.sleep(0.5)
	gpio.output(11, gpio.LOW)
	time.sleep(0.5)
	print("CTRL+C to stop this code")

gpio.cleanup()
