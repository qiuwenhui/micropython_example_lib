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



## 网络协议的各种项目开发

TCP

UDP 

MQTT

SOCKET

## 串口通讯

