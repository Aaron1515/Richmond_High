import RPi.GPIO as GPIO
import time as Time

# tester
def helloWorld():
	print("Hello World!")


def setupBoard():
	import RPi.GPIO as GPIO
	import time as Time
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	Print("Raspberry used as GPIO")
	Print("Time used as Time")
	Print("Please setup pins")


def resetAll():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)
	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(19, GPIO.OUT)
	GPIO.cleanup()


def resetOne(pinNumber):
	GPIO.setmode(GPIO.Board)
	GPIO.setwarings(False)
	GPIO.setup(pinNumber, GPIO.OUT)
	GPIO.cleanup()

def setupPinOut(pinNumber):
	GPIO.setup(pinNumber, GPIO.OUT)

def setupPinIn(pinNumber):
	GPIO.setup(pinNumber, GPIO.IN)



def sleep(sleepTime):
	Time.sleep(sleepTime)	





print("*" * 50)
print("************ Aaron's Library Loaded: *************")
print("**************** Known commands: *****************")
print("*" * 50)
print("      setupBoard() - Setup board")
print("      resetAll() - Reset all pins")
print("      resetOne(pin #) - Reset one pin")
print("      setupPinOut(pin #) - Setup pin out")
print("      setupPinIn(pin #) - Setup pin in")