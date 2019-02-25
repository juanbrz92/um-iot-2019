import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

def on_connect(client, userdata, rc):
    #print ("Connected with rc: " + str(rc))
    client.subscribe("dht11sensor/DHT11")

def on_message(client, userdata, msg):
    #print ("Topic: "+ msg.topic+"\nMessage: "+str(msg.payload))
    if TRUE in msg.payload:
        #print("  Red on!")
        GPIO.output(13, True)
    else:
        #print("  Red off!")
        GPIO.output(13, False)
        

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

client.loop_forever()
