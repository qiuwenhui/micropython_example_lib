from umqtt.simple import MQTTClient

# Test reception e.g. with:
# mosquitto_sub -t foo_topic

def main(server="192.168.31.244"):
    c = MQTTClient("umqtt_client", server)
    c.connect()
    c.publish(b"foo_topic", b"hello from micropython")
    c.disconnect()

if __name__ == "__main__":
    main()

