# MacroPython_Esp8266编程开发手册

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



## 网络协议的各种项目开发

TCP

UDP 

MQTT

SOCKET

## 串口通讯

