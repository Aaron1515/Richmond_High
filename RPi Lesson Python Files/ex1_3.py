import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setwarnings(False)
gpio.output(13, gpio.HIGH)

# Directions: Set GPIO Pin 11 to HIGH and 13 to LOW to turn one
# LED light on and one LED light off.
# ~~~~~~~~~~~~~~~~~~~~~ Type Code Here ~~~~~~~~~~~~~~~~~~~~ #





# ~~~~~~~~~~~~~~~~~~~~~~~~ End Code ~~~~~~~~~~~~~~~~~~~~~~~ #

time.sleep(5)
gpio.cleanup()
