import RPi.GPIO as GPIO
from time import sleep

R_channel = 19
G_channel = 13
B_channel = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(R_channel,GPIO.OUT)
GPIO.setup(G_channel,GPIO.OUT)
GPIO.setup(B_channel,GPIO.OUT)

r = GPIO.PWM(R_channel,1000)
g = GPIO.PWM(G_channel,1000)
b = GPIO.PWM(B_channel,1000)	

FAST = 0.005
SLOW = 0.05

while True:
	try:

		#RED -> WHITE -> CYAN (Full Wave)
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
			sleep(SLOW)

		#WHITE (Half Wave)
		for i in range(0,127):
			increasing = ((i/255)*100)
			decresing = (((255-i)/255)*100)
			r.start(decresing)
			g.start(increasing)
			b.start(increasing)
			print(increasing,decresing)
			sleep(FAST)

		#MAGENTA (Half Wave)
		for i in range(127,255):
			increasing = ((i/255)*100)
			decresing = (((255-i)/255)*100)
			r.start(decresing)
			g.start(increasing)
			b.start(decresing)
			print(increasing,decresing)
			sleep(SLOW)

		#WHITE (Half Wave)
		for i in range(0,127):
				increasing = ((i/255)*100)
				decresing = (((255-i)/255)*100)
				r.start(increasing)
				g.start(decresing)
				b.start(increasing)
				print(increasing,decresing)
				sleep(FAST)

		#GREEN (Half Wave)
		for i in range(127,255):
			increasing = ((i/255)*100)
			decresing = (((255-i)/255)*100)
			r.start(increasing)
			g.start(decresing)
			b.start(increasing)
			print(increasing,decresing)
			sleep(SLOW)

		#WHITE (Half Wave)
		for i in range(0,127):
			increasing = ((i/255)*100)
			decresing = (((255-i)/255)*100)
			r.start(decresing)
			g.start(increasing)
			b.start(decresing)
			print(increasing,decresing)
			sleep(FAST)

		#YELLOW (Half Wave)
		for i in range(127,255):
			increasing = ((i/255)*100)
			decresing = (((255-i)/255)*100)
			r.start(decresing)
			g.start(decresing)
			b.start(increasing)
			print(increasing,decresing,decresing)
			sleep(SLOW)

		#WHITE (Half Wave)
		for i in range(0,127):
			increasing = ((i/255)*100)
			decresing = (((255-i)/255)*100)
			r.start(increasing)
			g.start(increasing)
			b.start(decresing)
			print(increasing,decresing)
			sleep(FAST)

		#WHITE FULL WAVE
		for i in range(127,255):
			increasing = ((i/255)*100)
			decresing = (((255-i)/255)*100)
			r.start(decresing)
			g.start(increasing)
			b.start(increasing)
			print(increasing,decresing,decresing)
			sleep(FAST)

	except KeyboardInterrupt as e:
		print("Recieved Ctrl+C Quiting\n")
		break

r.stop()
g.stop()
b.stop()
GPIO.cleanup()
print("Quiting\n")