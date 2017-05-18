import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setwarnings(False) 

#Directions: Create two different For loops that will cause two individual
#LED lights to turn on at different rates. Make sure that the light only
#blinks five times!

# ~~~~~~~~~~~~~~~~~~~~~~~~~ Type Code Here ~~~~~~~~~~~~~~~~~~~~~~~~~~~#

for x in  range(5): 
	gpio.output(11, gpio.HIGH)
	time.sleep(1)
	gpio.output(11, gpio.LOW) 
	time.sleep(1)
	gpio.output(13, gpio.HIGH)
	time.sleep(0.25)
	gpio.output(13, gpio.LOW)
	time.sleep(0.25)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End Code ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
gpio.cleanup()

