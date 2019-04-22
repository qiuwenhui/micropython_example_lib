#'''
 # @ Author: qiuwenhui
 # @ Create Time: 2019-04-22 11:22:27
 # @ Modified by: qiuwenhui
 # @ Modified time: 2019-04-22 12:21:34
 # @ 代码描述:
 #'''

#一个按键控制led的开关
from machine import Pin
led=Pin(2,Pin.OUT)
Button=Pin(4,Pin.IN)
while True:
  led.value(Button.value())