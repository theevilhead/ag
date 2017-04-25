import RPi.GPIO as GPIO
import time
import urllib2
GPIO.setmode(GPIO.BCM)

url = 'http://139.59.6.47/gen1.php'

temp_pin = 14
hum_pin = 15
moist_pin = 18

GPIO.setup(14,GPIO.IN)
GPIO.setup(15,GPIO.IN)
GPIO.setup(18,GPIO.IN)

while True:
	# Read temperature
	i_1 = str(GPIO.input(temp_pin))
	# Read moisture
	i_3 = str(GPIO.input(moist_pin))
	time.sleep(5)
	# Call the url endpoint

	req = urllib2.Request(url+'?auth_id=znjMmmVtdE2l&s_1='+i_1+'&s_2='+i_3)
	f = urllib2.urlopen(req)
	print("Inserted")

