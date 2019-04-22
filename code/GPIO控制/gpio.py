# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    gpio.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: anonymous <anonymous@student.codam.nl>       +#+                      #
#                                                    +#+                       #
#    Created: 2019/04/22 10:57:18 by anonymous      #+#    #+#                 #
#    Updated: 2019/04/22 10:57:18 by anonymous     ########   odam.nl          #
#    GPIO micropython
#                                                                              #
# **************************************************************************** #
# Complete project details at https://RandomNerdTutorials.com

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
#print(esp.flash_size())
while True:
  led.value(not led.value())
  sleep(0.5)
