from evohomeclient import EvohomeClient
import datetime

client = EvohomeClient('xxx', 'xxxx')

for device in client.temperatures(force_refresh=True):
    print (datetime.datetime.now().isoformat() + "," + device["name"] + "," + str(device["setpoint"]) +"," + str(device["temp"]))