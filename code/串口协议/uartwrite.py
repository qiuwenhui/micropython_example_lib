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
