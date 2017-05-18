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


#Directions: Set up your if/else statements. Use the "is not" comparison statement, !=,
#to create a condition where both LED lights remain on if both buttons are not pressed.
#If either button or both buttons are pressed, both LED lights will turn off. Note the 
#default state of the lights should be on.

# ~~~~~~~~~~~~~~~~~~~~~~~~~ Type Code Here ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End Code ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
	time.sleep(0.1)
	print("Ctrl + C to stop code!")
 
gpio.cleanup()
