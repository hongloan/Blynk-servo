import blynklib
import RPi.GPIO as GPIO
import time
import signal
import signal
import atexit

BLYNK_AUTH = 'Your Blynk Auth Token Here'

atexit.register(GPIO.cleanup)

servopin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT, initial=False)
p = GPIO.PWM(servopin,50)
p.start(0)
time.sleep(2)

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"

# register handler for virtual pin V4 write event
@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    time.sleep(0.2)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    time.sleep(0.2)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    time.sleep(0.2)


###########################################################
# infinite loop that waits for event
###########################################################
while True:
    blynk.run()
