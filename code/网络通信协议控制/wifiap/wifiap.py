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
ap_essid='qrobot_iot'
ap_channel=2
ap_password='12345678'
ap_if.config(essid=ap_essid,channel=ap_channel,password=ap_password)

