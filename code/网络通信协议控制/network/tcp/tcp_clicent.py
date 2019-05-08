try:
    import usocket as socket
except:
    import socket

import time
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
  print("wifi connect souccess network config:"+str(sta_if.ifconfig()))

MESSAGE = "Hello, World!"


server_ip = '192.168.4.3'
server_port = 12345
tcp_client = socket.socket()
try:
  #time.sleep(500)
  a=tcp_client.connect((server_ip, server_port))
  print(a)
  time.sleep_ms(500)
  #tcp_client.send(MESSAGE)
except :
  print('fail to setup socket connection')
tcp_client.close()



