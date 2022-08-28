import RPi.GPIO as GPIO
from time import sleep

R_channel = 19
G_channel = 13
B_channel = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(R_channel,GPIO.OUT)
GPIO.setup(G_channel,GPIO.OUT)
GPIO.setup(B_channel,GPIO.OUT)

r = GPIO.PWM(R_channel,60)
g = GPIO.PWM(G_channel,60)
b = GPIO.PWM(B_channel,60)

# Reverse
# r.start(90)
# g.start(90)
# b.start(100)

# input("fsdf");

while True:
	try:
		for i in range(255):
			increasing = ((i/255)*100)
			decresing = (((255-i)/255)*100)
			value_r = increasing
			value_g = decresing
			value_b = decresing
			r.start(value_r)
			g.start(value_g)
			b.start(value_b)
			print(value_r,value_g,value_b)
			sleep(0.01)
		for i in range(255):
			increasing = ((i/255)*100)
			decresing = (((255-i)/255)*100)
			value_r = decresing
			value_g = increasing
			value_b = decresing
			r.start(value_r)
			g.start(value_g)
			b.start(value_b)
			print(value_r,value_g,value_b)
			sleep(0.01)
		for i in range(255):
			increasing = ((i/255)*100)
			decresing = (((255-i)/255)*100)
			value_r = decresing
			value_g = decresing
			value_b = increasing
			r.start(value_r)
			g.start(value_g)
			b.start(value_b)
			print(value_r,value_g,value_b)
			sleep(0.01)

	except KeyboardInterrupt as e:
		print("Recieved Ctrl+C Quiting\n")
		break

r.stop()
g.stop()
b.stop()
GPIO.cleanup()
print("Quiting\n")