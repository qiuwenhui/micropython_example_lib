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
addr = socket.getaddrinfo('micropython.org', 80)[0][-1]
s = socket.socket()
s.connect(addr)
s.send(b'GET / HTTP/1.1\r\nHost: micropython.org\r\n\r\n')
data = s.recv(1000)
s.close()
