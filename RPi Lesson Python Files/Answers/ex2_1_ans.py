import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setwarnings(False) 

#Directions: Create a For loop that will repeat itself five times using
#the syntax from the background information

# ~~~~~~~~~~~~~~~~~~~~~~~~~ Type Code Here ~~~~~~~~~~~~~~~~~~~~~~~~~~~#

for x in  range(5): 
	gpio.output(11, gpio.HIGH)
	time.sleep(1)
	gpio.output(11, gpio.LOW) 
	time.sleep(1)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End Code ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
gpio.cleanup()
