import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setwarnings(False)

# Directions: Set GPIO Pin 11 to HIGH to turn on your LED light.
# ~~~~~~~~~~~~~~~~~~~~~ Type Code Here ~~~~~~~~~~~~~~~~~~~~ #





# ~~~~~~~~~~~~~~~~~~~~~~~~ End Code ~~~~~~~~~~~~~~~~~~~~~~~ #

time.sleep(5)
gpio.cleanup()
