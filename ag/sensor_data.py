import RPi.GPIO as GPIO
import time
import urllib2
GPIO.setmode(GPIO.BCM)

url = 'http://localhost:8080/listen.php'

temp_pin = 14
hum_pin = 15
moist_pin = 18

GPIO.setup(a_pin,GPIO.IN)
GPIO.setup(14,GPIO.OUT)
while True:
	# Read temperature
	i_1 = GPIO.input(temp_pin)
	# Read humidity
	i_2 = GPIO.input(hum_pin)
	# Read moisture
	i_3 = GPIO.input(moist_pin)
	time.sleep(60000)
	# Call the url endpoint

	req = urllib2.Request(url)
	f = urllib2.urlopen(req)


