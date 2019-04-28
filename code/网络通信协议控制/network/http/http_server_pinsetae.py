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
