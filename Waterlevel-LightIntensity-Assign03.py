import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

#Provide your IBM Watson Device Credentials
organization = "0z828r"
deviceType = "iotdevice"        #Credentials of Watson IoT sensor simulator
deviceId = "1001"
authMethod = "token"
authToken = "prathyusha"


# Initialize the device client.
W=0
L=0

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
    W=random.randint(40,90)
    L=random.randint(30,95)
    #Send Temperature & Humidity to IBM Watson
    data = {"d":{ 'waterLevel' : W, 'lightIntensity': L }}
    #print data
    def myOnPublishCallback():
        print ("Published WaterLevel = %s %%" % W, "Light Intensity = %s %%" % L, "to IBM Watson")

    success = deviceCli.publishEvent("Data", "json", data, qos=0, on_publish=myOnPublishCallback)
    time.sleep(12)
    if not success:
        print("Not connected to IoTF")
    time.sleep(1)

deviceCli.disconnect()