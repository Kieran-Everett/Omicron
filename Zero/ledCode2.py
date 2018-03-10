import RPi as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT) #red
GPIO.setup(27, GPIO.OUT) #green
GPIO.setup(22, GPIO.OUT) #blue
GPIO.setup(18, GPIO.OUT) #heads
GPIO.setup(4, GPIO.OUT)  #deck

x = 1

while x == 1:
	y = input()
	if y == red:
		GPIO.output(17, 1)
	if y == redOff:
		GPIO.output(17, 0)
	if y == green:
		GPIO.output(27, 1)
	if y == greenOff:
		GPIO.output(27, 0)
	if y == blue:
		GPIO.output(22, 1)
	if y == blueOff:
		GPIO.output(22, 0)
	if y == heads:
		GPIO.output(18, 1)
	if y == headsOff:
		GPIO.output(18, 0)
	if y == deck:
		GPIO.output(4, 1)
	if y == deckOff:
		GPIO.output(4, 0)
	if y == off:
		GPIO.output(17, 0)
		GPIO.output(27, 0)
		GPIO.output(22, 0)
		GPIO.output(18, 0)
		GPIO.output(4, 0)
	if y == exit:
		x = 0

GPIO.cleanup()
