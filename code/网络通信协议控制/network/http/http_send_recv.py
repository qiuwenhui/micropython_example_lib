#http server send  recv data http 收发数据
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





