import webiopi
import datetime

GPIO = webiopi.GPIO

# PIN number
LIGHT = 17

HOUR_ON = 8
HOUR_OFF = 18

def setup():
    GPIO.setFunction(LIGHT, GPIO.OUT);
    now = datetime.datetime.now()
    if (now.hour >= HOUR_ON) and now.hour <= HOUR_OFF:
        GPIO.digitalWrite(LIGHT, GPIO.HIGH)

def loop():
    now = datetime.datetime.now()

    if (now.hour == HOUR_ON) and (now.minute == 0) and (now.second == 0):
        if (GPIO.digitalRead(LIGHT) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT, GPIO.HIGH)

    if (now.hour == HOUR_OFF) and (now.minute == 0) and (now.second == 0):
        if (GPIO.digitalRead(LIGHT) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT, GPIO.LOW)

    webiopi.sleep(1)

def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)
