import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False) 

gpio.setup(11, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(13, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(15, gpio.OUT)
gpio.setup(18, gpio.OUT) 

while True:
	button_state_1 = (gpio.input(11)==0)
	button_state_2 = (gpio.input(13)==0)


#Directions: Use "and" to compare button_state_1 and button_state_2 as true statements. 
#Write code such that when both are pressed at the same time, both lights will turn on
#and when you only press one button, neither light should turn on. When neither button
#is pressed, the lights should also remain off.
# ~~~~~~~~~~~~~~~~~~~~~~~~~ Type Code Here ~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	if #Enter Condition Using "and" comparison here# :

	else:	


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End Code ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	time.sleep(0.5)
	print "CTRL + C to Stop Code!"  
 
gpio.cleanup()

