import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

left = [11,12,13,15]
right = [37,35,33,31]

for pin in left:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)

for pin in right:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)

left_seq = [[1,0,0,0],
[1,1,0,0],
[0,1,0,0],
[0,1,1,0],
[0,0,1,0],
[0,0,1,1],
[0,0,0,1],
[1,0,0,1]]

right_seq = [[0,0,0,1],
[0,0,1,1],
[0,0,1,0],
[0,1,1,0],
[0,1,0,0],
[1,1,0,0],
[1,0,0,0],
[1,0,0,1]]

revolutions = 5

for r in range(revolutions):
	for i in range(512):
		for halfstep in range(8):
			for pin in range(4):
				GPIO.output(left[pin], left_seq[halfstep][pin])
				GPIO.output(right[pin], right_seq[halfstep][pin])
			time.sleep(0.001)
			#time.sleep(0.1)

GPIO.cleanup()
