#https://www.cloudmqtt.com
import time
from umqtt.simple import MQTTClient

# Publish test messages e.g. with:
# mosquitto_pub -t foo_topic -m hello

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))

port=12519
user="bnjxtnyp"
passw="2g8dIx_cHIM2"
def main(server="m24.cloudmqtt.com"):
    c = MQTTClient("umqtt_client", server,port,user,passw)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"$SYS/broker/load/connections/+")
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            # Non-blocking wait for message
            c.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    c.disconnect()

if __name__ == "__main__":
    main()

