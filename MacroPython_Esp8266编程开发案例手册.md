# MacroPython_Esp8266编程开发手册

案例参考

<http://wiki.micropython.org/Home>

<https://github.com/dhylands/upy-examples>

## GPIO控制

引脚分布

![](E:\QRobot\科目\NO.2 电子技术\MicroPython\NO.4 项目\McrioPython开发平台\ESP8266_MicroPython\NO.4 项目\NO.1 MacroPython_Esp8266编程开发案例手册\micropython_example_lib\ESP8266_PIN.PNG)

### 引脚输入

```shell
button = Pin(4, Pin.IN)
pin_value=button.value()
```

### 引脚输出

```python
gpio = Pin(5, Pin.OUT)
gpio.value(0)#输出0
gpio.value(1)#输出1
```

### Led.py

```python
#点亮引脚2上的LED 低电平有效  0 亮 1灭
import machine
p=machine.Pin(2,Pin.OUT)#定义GPIO 引脚
p.off()#关
p.on()#开
p.value(0)#设置p输出为0
p.value(1)#设置p输出1
```

### Gpio.py

```python
# Complete project details at https://RandomNerdTutorials.com
#0.5秒闪烁一次LED
from machine import Pin
from time import sleep#引入休眠

led = Pin(2, Pin.OUT)
#print(esp.flash_size())
while True:
  led.value(not led.value())
  sleep(0.5)
```

### button_led

```python
#一个按键控制led的开关
from machine import Pin
led=Pin(2,Pin.OUT)
Button=Pin(4,Pin.IN)
while True:
  led.value(Button.value())
```

## 文件的创建和读取

ESP8266上的MicroPython支持使用内置`open()`函数在Python中访问文件的标准方法。

```python
>>> f = open('data.txt', 'w')
>>> f.write('some data')
9#写入字节数
>>> f.close()
```

回读这个新文件的内容

```python
>>> f = open('data.txt')
>>> f.read()
'some data'
>>> f.close()
```

> 打开文件时的默认模式是以只读模式打开它，并将其作为文本文件打开。
>
> 指定`'wb'`作为第二个参数`open()`打开以便以二进制模式写入，并`'rb'`打开以便以二进制模式读取。

### micropython_fwrite.py

```python
f=open('data.txt','wb')#打开文件，如果没有就创建一个
f.write('some data')#写入文件内容
f.close()#关闭文件
#将文件添加到文件末尾
f=open('data.txt','a')
f.write("hello world")
f.close()
```

### micropython_fread.py

```python
filename="data.txt"#文件名
f=open(filename,'r')
len=f.read()
print(len)
f.close()
```

### filedelete.py

```python
import os
def delete(filename):
    print(os.remove(filename))
```

## 串口通讯

补丁-->boot.py

```python
import uos, machine
uart = machine.UART(0, 115200)
uos.dupterm(uart, 1)
```

分离代码

```python
uos.dupterm(None, 1)
```

### micropythonuart.py

```python
import machine
u0=machine.UART(0,115200)#定义串口
a=u0.write("hello from micropython \n")#输出字符串
a=123456
a=u0.write(str(a))#数字转字符串输出
```

### uartread.py

```python
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
  led.value(not led.value())#led 反转
  sleep(0.5)
  if uart.any():#查询串口有没有数据
    rdata=uart.read()#读取数据
    uart.write(rdata)#打印出数据
  else:
    uart.write("There is no data \n")
```

### uartwrite.py

```python
import machine
import uos
uos.dupterm(None, 1)#把串口0 从repl分离出来


uart=machine.UART(0,115200)
uart.init(115200, bits=8, parity=None, stop=1) # init with given parameters


len=uart.write("hello \n")#uart 写字符串

a=1234
len=uart.write(str(a))#uart 写数据

a=0x12
len=uart.write(hex(a))#uart 写16进制

uos.dupterm(uart, 1)#重新uart连接repl

```

## 网络通信

### WiFiAP.py

```python
#默认的IP 192.168.4.1
#ssid='MicroPython-259a36'
#password='micropythoN'
import network
ap_if=network.WLAN(network.AP_IF)#声明

print("wifi AP mode  state is:"+str(ap_if.active()))#查看是否激活
if not ap_if.active():  #如果没有激活则激活AP 模式
  ap_if.active(True)
  apstat=ap_if.active()
  print(apstait)


#输出配置信息#IP sybnet gateway dns
#IP地址，子网掩码，网关和DNS服务器
print(str(ap_if.ifconfig()))


#配置AP 接口信息
ap_ip='192.168.5.1' #IP地址
ap_sybnet='255.255.255.0' #子网掩码
ap_gateway='192.168.5.1' #网关
ap_dns='8.8.8.8' #DNS服务器

ap_if.ifconfig((ap_ip,ap_sybnet,ap_gateway,ap_dns))
print(str(ap_if.ifconfig()))

#查询常规连接参数
print(ap_if.config('mac'))
print(ap_if.config('essid'))
print(ap_if.config('channel'))
print(ap_if.config('authmode'))
#print(ap_if.config('password')) #无法查询
#print(ap_if.config('dhcp_hostname')) #无法查询

#设置常规连接参数
ap_essid='qrobot_iot'#ssid
ap_channel=2#changle
ap_password='12345678'#password
ap_if.config(essid=ap_essid,channel=ap_channel,password=ap_password)

```

### wifista.py

wifi STA 模式设置

```python

import network
sta_if=network.WLAN(network.STA_IF)#创建STA连接

print("WIFI sta state is:"+str(sta_if.active()))#sta激活状态
if not sta_if.active():#如果没有激活sta模式
    sta_if.active(True)#激活sta mode
    print("WIFI STA MODD state is:"+str(sta_if.active()))

#判断是否连接到连接网络
print("sta mode is connected intenet:"+str(sta_if.isconnected()))

#wifi is state
sta_if_state=sta_if.status()

def wifistate(sta_if_state):
  if sta_if_state==0:
    return "STAT_IDLE no connection and no activity"
  if sta_if_state==1:
    return "STAT_CONNECTING – connecting in progress"
  if sta_if_state==2:
    return "STAT_WRONG_PASSWORD – failed due to incorrect password"
  if sta_if_state==3:
    return "STAT_NO_AP_FOUND – failed because no access point replied"
  if sta_if_state==4:
    return "STAT_CONNECT_FAIL – failed due to other problems"
  if sta_if_state==5:
    return "STAT_GOT_IP – connection successful"

print("wifi sta state:"+wifistate(sta_if_state))
#扫描网络ssid
ssid=sta_if.scan()#扫描空中的wifi=(ssid，bssid，channel，RSSI，authmode，hidden)
for i in range(len(ssid)):
  ssids=str(ssid[i][0],'utf-8')
  print(ssids)
 
#连接网络
ssid_='ChangyanAiedu'
password_='iFlytek1234'

sta_if.active(True)#一定要激活sta mode
if not sta_if.isconnected():#如果没有连接
  print('connecting to network...')
  sta_if.connect(ssid_,password_)#连接到指定特定网洛
  while not sta_if.isconnected():
    print(".")
  print("wifi connect souccess network config:"+str(sta_if.ifconfig()))

#连接信息
print("wifi sta state:"+wifistate(sta_if.status()))#连接状态
print("wifi connect souccess network config:"+str(sta_if.ifconfig()))#连接信息
print("connect ssid  is :"+str(sta_if.config('essid')))
print("mac is:"+str(sta_if.config('mac')))
#print("channel is :"+tr('channel')) #只适合AP 模式
sta_if.disconnected()#断开连接
sta_if.activet(FLASH)
```

### Micropython网络编程Scoket

一但设置了WiFi，就可以使用套接字来访问网络。套接字表示网络设备上的端点，当两个套接字连接在一起时，可以继续进行通信。<font color="red">Internet协议构建在套接字</font>之上，例如电子邮件（SMTP），Web（HTTP），telnet，ssh等等。为这些协议中的每一个分配一个特定的端口，它只是一个整数。给定IP地址和端口号，您可以连接到远程设备并开始与之通信。

<http://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html>

<http://wiki.micropython.org/Home>

#### showip2connet2ip.py

```python
# connect/ show IP config a specific network interface
# see below for examples of specific drivers
import network
import utime

# enable station interface and connect to WiFi access point
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('ChangyanAiedu', 'iFlytek1234')
# now use sockets as usual

if not nic.isconnected():#是否连接
    nic.connect()
    print("Waiting for connection...")#输出等待连接
    while not nic.isconnected():
        utime.sleep(1)#休眠1秒
print(nic.ifconfig())

# now use usocket as usual
import usocket as socket
addr = socket.getaddrinfo('micropython.org', 80)[0][-1]#地址信息

s = socket.socket()
s.connect(addr)
s.send(b'GET / HTTP/1.1\r\nHost: micropython.org\r\n\r\n')
data = s.recv(1000)#获取1000个byte
s.close()
```

#### HTTP GET 请求

##### http_get.py

```python
import network
import usocket as socket
def http_get(url):
    _, _, host, path = url.split('/', 3)#分析地址信息路径 获得地址
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))#插入路径和主机
    while True:
        data = s.recv(100)#获得100个字符
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()
```

##### http_server_pinsetae.py

```python
#显示引脚状态服务器
#创建一个简单的HTTP服务器，该服务器为单个网页提供一个包含所有GPIO引脚状态的表
import machine
pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]#定义引脚

#html 标记文本 code
html="""<!DOCTYPE html>
<html>
<head> <title>ESP8266 Pins</title> 
<style type="text/css">
@media (max-width : 1080px ){
}
</style>
    </head>
    <body>
	<div style="width: auto; margin-left: auto; margin-right: auto;" clase="one">
		<h1 style="margin-left: auto; margin-right: auto; text-align: center;">ESP8266 Pins</h1>
        <table width="1000px" border="1" style="margin-left: auto; margin-right: auto;"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
		</div>
</body>
</html>
"""

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]#获得地址信息

s = socket.socket()#socket 创建
s.bind(addr)#bind 定address
s.listen(1) #限制连接个数

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    response = html % '\n'.join(rows)
    cl.send(response)
    cl.close()
```

##### set_led_httpserver.py

```python
import socket
import machine


#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 LED ON/OFF</title> </head>
<h2>LED's on and off with Micropython</h2></center>
<h3>(ESP8266 HUZZAH Feather)</h3></center>
<form>
LED RED&nbsp;&nbsp;:
<button name="LED" value="ON_RED" type="submit">LED ON</button>
<button name="LED" value="OFF_RED" type="submit">LED OFF</button><br><br>
LED BLUE:
<button name="LED" value="ON_BLUE" type="submit">LED ON</button>
<button name="LED" value="OFF_BLUE" type="submit">LED OFF</button><br><br>
LED Extern:
<button name="LED" value="ON_EX" type="submit">LED ON</button>
<button name="LED" value="OFF_EX" type="submit">LED OFF</button>
</form>
</html>
"""

#Setup PINS
LED_RED = machine.Pin(0, machine.Pin.OUT)
LED_BLUE = machine.Pin(2, machine.Pin.OUT)
LED_EX = machine.Pin(12, machine.Pin.OUT)

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)#5个连接

while True:

    conn, addr = s.accept() #TCP 模式
    #套接字必须绑定到一个地址并侦听连接。返回值是一对（conn，address）
    #其中conn是可用于在连接上发送和接收数据的新套接字对象，address是绑定到连接另一端的套接字的地址。
    print("Got a connection from %s" % str(addr))#输出连接的地址
    request = conn.recv(1024)#接受数据
    print("Content = %s" % str(request))#输出接受的数据
    request = str(request)#数据转换成字符串
    
    LEDON_RED = request.find('/?LED=ON_RED')
    LEDOFF_RED = request.find('/?LED=OFF_RED')
    LEDON_BLUE = request.find('/?LED=ON_BLUE')
    LEDOFF_BLUE = request.find('/?LED=OFF_BLUE')
    LEDON_EX = request.find('/?LED=ON_EX')
    LEDOFF_EX = request.find('/?LED=OFF_EX')    

    if LEDON_RED == 6:
        print('TURN LED0 ON')
        LED_RED.off()
    if LEDOFF_RED == 6:
        print('TURN LED0 OFF')
        LED_RED.on()
    if LEDON_BLUE == 6:
        print('TURN LED2 ON')
        LED_BLUE.off()
    if LEDOFF_BLUE == 6:
        print('TURN LED2 OFF')
        LED_BLUE.on()
    if LEDON_EX == 6:
        print('TURN LED2 ON')
        LED_EX.on()
    if LEDOFF_EX == 6:
        print('TURN LED2 OFF')
        LED_EX.off() 
        
    response = html#发送
    conn.send(response)#发送html数据
    conn.close()#关闭此次连接

```

webserverset_pin.py

```python
# Complete project details at https://RandomNerdTutorials.com
# 远程设置led 开关
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'ChangyanAiedu'
password = 'iFlytek1234'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)

def web_page():
  if led.value() == 1:
    gpio_state="O0F"
  else:
    gpio_state="ON"
  
  html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
  <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ap 和sta模式
s.bind(('', 80))#绑定地址
s.listen(205)#最多5个连接

while True:
  conn, addr = s.accept()#s 被connt sockt 连接
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  #print('Content = %s' % request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6:
    print('LED ON')
    led.value(0)
  if led_off == 6:
    print('LED OFF')
    led.value(1)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()


```

http_send_recv.py

```python
#http server send  recv data http 收发数据
#http 接收 发送数据到浏览器
import socket
import math
import os
from machine import Pin
led = Pin(2, Pin.OUT)

def web_page(gpio_state):
  html1 = """
  <html><head>
<meta charset="utf-8">
<title>http收发数据</title>
	<style>
	html{
    font-family: Helvetica;
    display: inline-block;
    margin: 0px auto;
    text-align: left;
    line-height: 31px;
    width: 200px;
    height: 80px;
}
  h1{color: #0F3376; padding: 2vh;}
	</style>
</head>

<body style="text-align: center">
	<h1>http 数据收发 </h1>
<!--<p>收到的数据:</p>-->
	<p>收到的数据
<textarea name="textarea" style="width: 180px; height: 150px;">"""+gpio_state+"""</textarea></p>
	<form action="form_action.asp" method="get">
    <p>发数据： <input type="text" name="inputdata" /><input type="submit" value="Submit" /></p>	
</form>
</body></html>
  """
  return html1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ap 和sta模式
s.bind(('', 80))#绑定地址
s.listen(205)#最多5个连接

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  i=-1
  i= request.find('inputdata=')+10
  strdata=""
  a=request[i]
  if i != -1 :
    while True:
      if a == '\\':
        break
      strdata=strdata+str(a)
      
      i=i+1
      
      
      a=request[i]
  
  print(strdata)
  response = web_page(strdata)
  #提取字符串 inputdata=？？\r\n
  
  #conn.send('HTTP/1.1 200 OK\n')
  #conn.send('Content-Type: text/html\n')
  #conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()

```

#### UDP 通信

```python
#micropython UDP 
import socket

#创建 socket 套字节
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port=10086
s.bind(('',port)) #绑定端口binding the port
print('waiting...')

while True:   #接收数据receiving data
  data,addr=s.recvfrom(1024)#_ _=socket.recvfrom(bufsize)  接受最大1024个数据 返回 data 和 地址信息
  s.sendto('heello from micropython',addr)#将信息发送到目的地址addr=('192.168.31.28',1024)
 print('received:',data,'from',addr)
```

python UDP

```python
    #python 3.7
import socket
    
UDP_IP = "192.168.31.119"
UDP_PORT = 10086
MESSAGE = "Hello, World!"
    
print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)
   
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))

```

```python
from socket import *
 
host = '192.168.31.119' # 这是客户端的电脑的ip
port = 10086 #接口选择大于10000的，避免冲突
bufsize = 1024 #定义缓冲大小
 
addr = (host,port) # 元祖形式
udpClient = socket(AF_INET,SOCK_DGRAM) #创建客户端
 
while True:
  data = input('>>> ')
  if not data:
    break
  data = data.encode(encoding="utf-8") 
  udpClient.sendto(data,addr) # 发送数据
  data,addr = udpClient.recvfrom(bufsize) #接收数据和返回地址
  print(data.decode(encoding="utf-8"),'from',addr)
 
udpClient.close()
```

#### TCP通信

服务端

```python
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

```

客户端

参考：<https://randomnerdtutorials.com/how-to-make-two-esp8266-talk/>

```python
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
```

### MQTT协议通信

##### 测试服务器

MQTT服务软件

mosquitto

mosquito-Client

电脑：Ubuntu 18.04LTS

详情请看《MQTT协议/Mosquitto服务器安装》

LIB:

umqtt.simple

umqtt_simple.py

```python
import usocket as socket
import ustruct as struct
from ubinascii import hexlify

class MQTTException(Exception):
    pass

class MQTTClient:

    def __init__(self, client_id, server, port=0, user=None, password=None, keepalive=0,
                 ssl=False, ssl_params={}):
        if port == 0:
            port = 8883 if ssl else 1883
        self.client_id = client_id
        self.sock = None
        self.server = server
        self.port = port
        self.ssl = ssl
        self.ssl_params = ssl_params
        self.pid = 0
        self.cb = None
        self.user = user
        self.pswd = password
        self.keepalive = keepalive
        self.lw_topic = None
        self.lw_msg = None
        self.lw_qos = 0
        self.lw_retain = False

    def _send_str(self, s):
        self.sock.write(struct.pack("!H", len(s)))
        self.sock.write(s)

    def _recv_len(self):
        n = 0
        sh = 0
        while 1:
            b = self.sock.read(1)[0]
            n |= (b & 0x7f) << sh
            if not b & 0x80:
                return n
            sh += 7

    def set_callback(self, f):
        self.cb = f

    def set_last_will(self, topic, msg, retain=False, qos=0):
        assert 0 <= qos <= 2
        assert topic
        self.lw_topic = topic
        self.lw_msg = msg
        self.lw_qos = qos
        self.lw_retain = retain

    def connect(self, clean_session=True):
        self.sock = socket.socket()
        addr = socket.getaddrinfo(self.server, self.port)[0][-1]
        self.sock.connect(addr)
        if self.ssl:
            import ussl
            self.sock = ussl.wrap_socket(self.sock, **self.ssl_params)
        premsg = bytearray(b"\x10\0\0\0\0\0")
        msg = bytearray(b"\x04MQTT\x04\x02\0\0")

        sz = 10 + 2 + len(self.client_id)
        msg[6] = clean_session << 1
        if self.user is not None:
            sz += 2 + len(self.user) + 2 + len(self.pswd)
            msg[6] |= 0xC0
        if self.keepalive:
            assert self.keepalive < 65536
            msg[7] |= self.keepalive >> 8
            msg[8] |= self.keepalive & 0x00FF
        if self.lw_topic:
            sz += 2 + len(self.lw_topic) + 2 + len(self.lw_msg)
            msg[6] |= 0x4 | (self.lw_qos & 0x1) << 3 | (self.lw_qos & 0x2) << 3
            msg[6] |= self.lw_retain << 5

        i = 1
        while sz > 0x7f:
            premsg[i] = (sz & 0x7f) | 0x80
            sz >>= 7
            i += 1
        premsg[i] = sz

        self.sock.write(premsg, i + 2)
        self.sock.write(msg)
        #print(hex(len(msg)), hexlify(msg, ":"))
        self._send_str(self.client_id)
        if self.lw_topic:
            self._send_str(self.lw_topic)
            self._send_str(self.lw_msg)
        if self.user is not None:
            self._send_str(self.user)
            self._send_str(self.pswd)
        resp = self.sock.read(4)
        assert resp[0] == 0x20 and resp[1] == 0x02
        if resp[3] != 0:
            raise MQTTException(resp[3])
        return resp[2] & 1

    def disconnect(self):
        self.sock.write(b"\xe0\0")
        self.sock.close()

    def ping(self):
        self.sock.write(b"\xc0\0")

    def publish(self, topic, msg, retain=False, qos=0):
        pkt = bytearray(b"\x30\0\0\0")
        pkt[0] |= qos << 1 | retain
        sz = 2 + len(topic) + len(msg)
        if qos > 0:
            sz += 2
        assert sz < 2097152
        i = 1
        while sz > 0x7f:
            pkt[i] = (sz & 0x7f) | 0x80
            sz >>= 7
            i += 1
        pkt[i] = sz
        #print(hex(len(pkt)), hexlify(pkt, ":"))
        self.sock.write(pkt, i + 1)
        self._send_str(topic)
        if qos > 0:
            self.pid += 1
            pid = self.pid
            struct.pack_into("!H", pkt, 0, pid)
            self.sock.write(pkt, 2)
        self.sock.write(msg)
        if qos == 1:
            while 1:
                op = self.wait_msg()
                if op == 0x40:
                    sz = self.sock.read(1)
                    assert sz == b"\x02"
                    rcv_pid = self.sock.read(2)
                    rcv_pid = rcv_pid[0] << 8 | rcv_pid[1]
                    if pid == rcv_pid:
                        return
        elif qos == 2:
            assert 0

    def subscribe(self, topic, qos=0):
        assert self.cb is not None, "Subscribe callback is not set"
        pkt = bytearray(b"\x82\0\0\0")
        self.pid += 1
        struct.pack_into("!BH", pkt, 1, 2 + 2 + len(topic) + 1, self.pid)
        #print(hex(len(pkt)), hexlify(pkt, ":"))
        self.sock.write(pkt)
        self._send_str(topic)
        self.sock.write(qos.to_bytes(1, "little"))
        while 1:
            op = self.wait_msg()
            if op == 0x90:
                resp = self.sock.read(4)
                #print(resp)
                assert resp[1] == pkt[2] and resp[2] == pkt[3]
                if resp[3] == 0x80:
                    raise MQTTException(resp[3])
                return

    # Wait for a single incoming MQTT message and process it.
    # Subscribed messages are delivered to a callback previously
    # set by .set_callback() method. Other (internal) MQTT
    # messages processed internally.
    def wait_msg(self):
        res = self.sock.read(1)
        self.sock.setblocking(True)
        if res is None:
            return None
        if res == b"":
            raise OSError(-1)
        if res == b"\xd0":  # PINGRESP
            sz = self.sock.read(1)[0]
            assert sz == 0
            return None
        op = res[0]
        if op & 0xf0 != 0x30:
            return op
        sz = self._recv_len()
        topic_len = self.sock.read(2)
        topic_len = (topic_len[0] << 8) | topic_len[1]
        topic = self.sock.read(topic_len)
        sz -= topic_len + 2
        if op & 6:
            pid = self.sock.read(2)
            pid = pid[0] << 8 | pid[1]
            sz -= 2
        msg = self.sock.read(sz)
        self.cb(topic, msg)
        if op & 6 == 2:
            pkt = bytearray(b"\x40\x02\0\0")
            struct.pack_into("!H", pkt, 2, pid)
            self.sock.write(pkt)
        elif op & 6 == 4:
            assert 0

    # Checks whether a pending message from server is available.
    # If not, returns immediately with None. Otherwise, does
    # the same processing as wait_msg.
    def check_msg(self):
        self.sock.setblocking(False)
        return self.wait_msg()
```

example_sub.py

```python
import usocket as socket
import ustruct as struct
from ubinascii import hexlify

class MQTTException(Exception):
    pass

class MQTTClient:

    def __init__(self, client_id, server, port=0, user=None, password=None, keepalive=0,
                 ssl=False, ssl_params={}):
        if port == 0:
            port = 8883 if ssl else 1883
        self.client_id = client_id
        self.sock = None
        self.server = server
        self.port = port
        self.ssl = ssl
        self.ssl_params = ssl_params
        self.pid = 0
        self.cb = None
        self.user = user
        self.pswd = password
        self.keepalive = keepalive
        self.lw_topic = None
        self.lw_msg = None
        self.lw_qos = 0
        self.lw_retain = False

    def _send_str(self, s):
        self.sock.write(struct.pack("!H", len(s)))
        self.sock.write(s)

    def _recv_len(self):
        n = 0
        sh = 0
        while 1:
            b = self.sock.read(1)[0]
            n |= (b & 0x7f) << sh
            if not b & 0x80:
                return n
            sh += 7

    def set_callback(self, f):
        self.cb = f

    def set_last_will(self, topic, msg, retain=False, qos=0):
        assert 0 <= qos <= 2
        assert topic
        self.lw_topic = topic
        self.lw_msg = msg
        self.lw_qos = qos
        self.lw_retain = retain

    def connect(self, clean_session=True):
        self.sock = socket.socket()
        addr = socket.getaddrinfo(self.server, self.port)[0][-1]
        self.sock.connect(addr)
        if self.ssl:
            import ussl
            self.sock = ussl.wrap_socket(self.sock, **self.ssl_params)
        premsg = bytearray(b"\x10\0\0\0\0\0")
        msg = bytearray(b"\x04MQTT\x04\x02\0\0")

        sz = 10 + 2 + len(self.client_id)
        msg[6] = clean_session << 1
        if self.user is not None:
            sz += 2 + len(self.user) + 2 + len(self.pswd)
            msg[6] |= 0xC0
        if self.keepalive:
            assert self.keepalive < 65536
            msg[7] |= self.keepalive >> 8
            msg[8] |= self.keepalive & 0x00FF
        if self.lw_topic:
            sz += 2 + len(self.lw_topic) + 2 + len(self.lw_msg)
            msg[6] |= 0x4 | (self.lw_qos & 0x1) << 3 | (self.lw_qos & 0x2) << 3
            msg[6] |= self.lw_retain << 5

        i = 1
        while sz > 0x7f:
            premsg[i] = (sz & 0x7f) | 0x80
            sz >>= 7
            i += 1
        premsg[i] = sz

        self.sock.write(premsg, i + 2)
        self.sock.write(msg)
        #print(hex(len(msg)), hexlify(msg, ":"))
        self._send_str(self.client_id)
        if self.lw_topic:
            self._send_str(self.lw_topic)
            self._send_str(self.lw_msg)
        if self.user is not None:
            self._send_str(self.user)
            self._send_str(self.pswd)
        resp = self.sock.read(4)
        assert resp[0] == 0x20 and resp[1] == 0x02
        if resp[3] != 0:
            raise MQTTException(resp[3])
        return resp[2] & 1

    def disconnect(self):
        self.sock.write(b"\xe0\0")
        self.sock.close()

    def ping(self):
        self.sock.write(b"\xc0\0")

    def publish(self, topic, msg, retain=False, qos=0):
        pkt = bytearray(b"\x30\0\0\0")
        pkt[0] |= qos << 1 | retain
        sz = 2 + len(topic) + len(msg)
        if qos > 0:
            sz += 2
        assert sz < 2097152
        i = 1
        while sz > 0x7f:
            pkt[i] = (sz & 0x7f) | 0x80
            sz >>= 7
            i += 1
        pkt[i] = sz
        #print(hex(len(pkt)), hexlify(pkt, ":"))
        self.sock.write(pkt, i + 1)
        self._send_str(topic)
        if qos > 0:
            self.pid += 1
            pid = self.pid
            struct.pack_into("!H", pkt, 0, pid)
            self.sock.write(pkt, 2)
        self.sock.write(msg)
        if qos == 1:
            while 1:
                op = self.wait_msg()
                if op == 0x40:
                    sz = self.sock.read(1)
                    assert sz == b"\x02"
                    rcv_pid = self.sock.read(2)
                    rcv_pid = rcv_pid[0] << 8 | rcv_pid[1]
                    if pid == rcv_pid:
                        return
        elif qos == 2:
            assert 0

    def subscribe(self, topic, qos=0):
        assert self.cb is not None, "Subscribe callback is not set"
        pkt = bytearray(b"\x82\0\0\0")
        self.pid += 1
        struct.pack_into("!BH", pkt, 1, 2 + 2 + len(topic) + 1, self.pid)
        #print(hex(len(pkt)), hexlify(pkt, ":"))
        self.sock.write(pkt)
        self._send_str(topic)
        self.sock.write(qos.to_bytes(1, "little"))
        while 1:
            op = self.wait_msg()
            if op == 0x90:
                resp = self.sock.read(4)
                #print(resp)
                assert resp[1] == pkt[2] and resp[2] == pkt[3]
                if resp[3] == 0x80:
                    raise MQTTException(resp[3])
                return

    # Wait for a single incoming MQTT message and process it.
    # Subscribed messages are delivered to a callback previously
    # set by .set_callback() method. Other (internal) MQTT
    # messages processed internally.
    def wait_msg(self):
        res = self.sock.read(1)
        self.sock.setblocking(True)
        if res is None:
            return None
        if res == b"":
            raise OSError(-1)
        if res == b"\xd0":  # PINGRESP
            sz = self.sock.read(1)[0]
            assert sz == 0
            return None
        op = res[0]
        if op & 0xf0 != 0x30:
            return op
        sz = self._recv_len()
        topic_len = self.sock.read(2)
        topic_len = (topic_len[0] << 8) | topic_len[1]
        topic = self.sock.read(topic_len)
        sz -= topic_len + 2
        if op & 6:
            pid = self.sock.read(2)
            pid = pid[0] << 8 | pid[1]
            sz -= 2
        msg = self.sock.read(sz)
        self.cb(topic, msg)
        if op & 6 == 2:
            pkt = bytearray(b"\x40\x02\0\0")
            struct.pack_into("!H", pkt, 2, pid)
            self.sock.write(pkt)
        elif op & 6 == 4:
            assert 0

    # Checks whether a pending message from server is available.
    # If not, returns immediately with None. Otherwise, does
    # the same processing as wait_msg.
    def check_msg(self):
        self.sock.setblocking(False)
        return self.wait_msg()
```

订阅

##### example_sub.py

```python
import time
from umqtt.simple import MQTTClient

# Publish test messages e.g. with:
# mosquitto_pub -t foo_topic -m hello

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))

def main(server="192.168.31.244"):
    c = MQTTClient("umqtt_client", server)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"foo_topic")
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            # Non-blocking wait for message
            c.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    c.disconnect()

if __name__ == "__main__":
    main()

```

发布

##### example_pub.py

```python
from umqtt.simple import MQTTClient

# Test reception e.g. with:
# mosquitto_sub -t foo_topic

def main(server="192.168.31.244"):
    c = MQTTClient("umqtt_client", server)
    c.connect()
    c.publish(b"foo_topic", b"hello from micropython")
    c.disconnect()

if __name__ == "__main__":
    main()
```

##### 实例

###### example_sub_led.py

```python
from umqtt.simple import MQTTClient
from machine import Pin
import ubinascii
import machine
import micropython


# ESP8266 ESP-12 modules have blue, active-low LED on GPIO2, replace
# with something else if needed.
led = Pin(2, Pin.OUT, value=1)

# Default MQTT server to connect to
SERVER = "192.168.31.244"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"led"


state = 0

def sub_cb(topic, msg):
    global state
    print((topic, msg))
    if msg == b"on":
        led.value(0)
        state = 1
    elif msg == b"off":
        led.value(1)
        state = 0
    elif msg == b"toggle":
        # LED is inversed, so setting it to current state
        # value will make it toggle
        led.value(state)
        state = 1 - state


def main(server=SERVER):
    c = MQTTClient(CLIENT_ID, server)
    # Subscribed messages will be delivered to this callback
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (server, TOPIC))

    try:
        while 1:
            #micropython.mem_info()
            c.wait_msg()
    finally:
        c.disconnect()
```

###### example_pub_adc.py

```python
import time
import ubinascii
import machine
import umqtt_simple
from umqtt.simple import MQTTClient
from machine import Pin


# Many ESP8266 boards have active-low "flash" button on GPIO0.
button = Pin(0, Pin.IN)
adc=machine.ADC(0)
# Default MQTT server to connect to
SERVER = "192.168.31.244"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"led"


def main(server=SERVER):
    c = MQTTClient(CLIENT_ID, server)
    c.connect()
    print("Connected to %s, waiting for button presses" % server)
    while True:
        adc_value=adc.read()
        print("adc_value = %d",adc_value)
        adc_value="adc_value = "+str(adc_value)
        c.publish(TOPIC, adc_value.encode("utf-8"))
        time.sleep_ms(200)

    c.disconnect()
```

#### CloudMQTT 

参考：

[https://www.cloudmqtt.com](https://www.cloudmqtt.com/)

账号

GITHUB账号

软件：<https://github.com/CloudMQTT>

##### 客户端

cloudmqtt.py

```python
#https://www.cloudmqtt.com
#umqtt.simple
import time
from umqtt.simple import MQTTClient

# Publish test messages e.g. with:
# mosquitto_pub -t foo_topic -m hello

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))

port=12519
user="bnjxtnyp"
passw="2g8dIx_cHIM2"
def main(server="m24.cloudmqtt.com"):
    c = MQTTClient("umqtt_client", server,port,user,passw)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"$SYS/broker/load/connections/+")
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            # Non-blocking wait for message
            c.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    c.disconnect()

if __name__ == "__main__":
    main()

```