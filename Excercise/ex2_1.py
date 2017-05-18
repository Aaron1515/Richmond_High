import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setwarnings(False) 

#Directions: Create a For loop that will turn your LED light on for one second
#and turn your LED light off for one second and have this repeat five times.
#Use the syntax from the pre-lesson and the time.sleep(1) function.
# ~~~~~~~~~~~~~~~~~~~~~~~~~ Type Code Here ~~~~~~~~~~~~~~~~~~~~~~~~~~~#



	

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End Code ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
gpio.cleanup()
