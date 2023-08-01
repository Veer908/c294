import time
from datetime import datetime
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = 'topicName/time'

client_id = 'iot'
username = 'test'
password = ''

def connect_mqtt():
	client = mqtt_client.Client(client_id)
	client.username_pw_set(username, password)
	client.connect(broker, port)
	return client

def publish(client):
	while True:
		time.sleep(1)
		now = datetime.now()
		current_time = now.strftime("%H%M")
		print("Current time:",current_time)
		client.publish(topic, current_time)


# Write code here.





def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()#project 294
    


