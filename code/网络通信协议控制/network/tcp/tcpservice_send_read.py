#micropython tcp client server 
#for esp8266
#http server send  recv data http 收发数据
import socket
import math
import os
from machine import Pin
led = Pin(2, Pin.OUT)

sta_if = network.WLAN(network.STA_IF)
if not sta_if.active():
  sta_if.active(True)

#连接网络
ssid_='ChangyanAiedu'
password_='iFlytek1234'

if not sta_if.isconnected():#如果没有连接
  print('connecting to network...')
  sta_if.connect(ssid_,password_)#连接到指定特定网洛
  print("s")
  #while not sta_if.isconnected():
  #print("wifi connect souccess network config:"+str(sta_if.ifconfig()))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ap 和sta模式
s.bind(('',8080))#绑定地址
s.listen(5)#最多5个连接
conn, addr = s.accept()
print('Got a connection from %s' % str(addr))

while True:
  request = conn.recv(1024)
  request = str(request,'utf-8')
  
  print(request)
  response = "hello world"
  conn.sendall(response)
  #conn.close()#连接关闭

