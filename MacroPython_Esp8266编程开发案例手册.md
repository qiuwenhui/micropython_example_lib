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

htpp









TCP

UDP 

MQTT

