from machine import Pin, SoftI2C
import network
from time import sleep_ms, sleep
import bme280_float as bme280   #https://github.com/robert-hh/BME280
import ssd1306

led_onboard = Pin(2, Pin.OUT) #built-in blue LED
led_onboard.value(1)

pin_reset = Pin(16, Pin.OUT)
pin_reset.value(0)
sleep_ms(10)
pin_reset.value(1)

i2c = SoftI2C(scl=Pin(15), sda=Pin(4), freq=400000, timeout=255)
print (i2c.scan()) #I2C test

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

bme = bme280.BME280(i2c=i2c)

#Wifi test
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
print (sta_if.scan())

while True:
    #print(bme.values)
    t,p,h=bme.values #strings returned, for raw values use read_compensated_data
    str1='Temp: '+t
    str2='Press: '+p
    str3='Hum: '+h
    oled.fill(0)
    oled.text('A Industriosa',12,50)
    oled.text(str1,0,0)
    oled.text(str2,0,10)
    oled.text(str3,0,20)
    oled.show()
    led_onboard.value(not led_onboard.value())
    sleep(1)