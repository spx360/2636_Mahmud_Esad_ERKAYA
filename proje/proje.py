from machine import Pin
from time import sleep
import dht 
from servo import Servo
import time

sensor = dht.DHT11(Pin(14))
led = Pin(12, Pin.OUT)
motor=Servo(pin=22)

while True:
  try:
    sleep(2)
    led.value(0)
    sensor.measure()
    temp = sensor.temperature()
    print(temp)
    if temp >25:
       motor.move(90)
    elif 15< temp <25:
       motor.move(45)
    else:
       motor.move(0)            
  except OSError as e:
    print('Failed to read sensor.')
    led.value(1)