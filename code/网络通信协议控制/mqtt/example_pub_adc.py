import time
import ubinascii
import machine
import umqtt_simple
from umqtt.simple import MQTTClient
from machine import Pin


# Many ESP8266 boards have active-low "flash" button on GPIO0.
button = Pin(0, Pin.IN)
adc=machine.ADC(0)
# Default MQTT server to connect to
SERVER = "192.168.31.244"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"led"


def main(server=SERVER):
    c = MQTTClient(CLIENT_ID, server)
    c.connect()
    print("Connected to %s, waiting for button presses" % server)
    while True:
        adc_value=adc.read()
        print("adc_value = %d",adc_value)
        adc_value="adc_value = "+str(adc_value)
        c.publish(TOPIC, adc_value.encode("utf-8"))
        time.sleep_ms(200)

    c.disconnect()

