from machine import Pin, SoftI2C
from time import sleep
import dht
import ssd1306
from servo import Servo
import time

i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
sensor = dht.DHT11(Pin(14))
led1 = Pin(12, Pin.OUT)
led2 = Pin(13, Pin.OUT)

motor=Servo(pin=22)
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
  try:
    sleep(2)
    led1.value(0)
    led2.value(1)
    sensor.measure()
    temp = sensor.temperature()
    print(temp)
    oled.text(str(temp), 0, 0)
    oled.show()
    oled.fill(0)
    if temp >25:
       motor.move(90)
    elif 15< temp <25:
       motor.move(45)
    else:
       motor.move(0)            
  except OSError as e:
    print('Failed to read sensor.')
    oled.text('Failed to read', 0, 0)
    oled.text('sensor.', 0, 10)
    oled.show(  )
    oled.fill(0)
    led1.value(1)
    led2.value(0)
