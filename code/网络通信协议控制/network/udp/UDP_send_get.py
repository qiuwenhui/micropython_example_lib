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
