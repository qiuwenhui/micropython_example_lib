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

AP





### 网络协议的各种项目开发

### HTTP 

#### web server



TCP

UDP 

MQTT

SOCKET

