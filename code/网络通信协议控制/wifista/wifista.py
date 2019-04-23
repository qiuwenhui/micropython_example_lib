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
print("connect ssid  is :"+str(sta_if.config('essid'))
#print("mac is:"+str(sta_if.config('mac')))
#print("channel is :"+tr('channel')) #只适合AP 模式