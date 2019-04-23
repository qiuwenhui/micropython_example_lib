import machine
from machine import Pin
from time import sleep

led=Pin(2,Pin.OUT)

import uos
uos.dupterm(None, 1)#把串口0 从repl分离出来


uart=machine.UART(0,115200)
uart.init(115200, bits=8, parity=None, stop=1) # init with given parameters

uart.write("read uart data \n")


while True:
  led.value(not led.value())
  sleep(0.5)
  if uart.any():
    rdata=uart.read()
    uart.write(rdata)
  else:
    uart.write("There is no data \n")
