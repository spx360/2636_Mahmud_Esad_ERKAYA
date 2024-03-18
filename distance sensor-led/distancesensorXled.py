from hcsr04 import HCSR04
from machine import Pin, PWM
from time import sleep

sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
led1 = Pin(12, Pin.OUT)
led2 = Pin(14, Pin.OUT)

while True:
    distance = sensor.distance_cm()
    if distance < 10:
       led1.value(1)
       led2.value(0)
    elif distance > 10:
       led2.value(1)
       led1.value(0)
    sleep(1)