import RPi.GPIO as IO
import time
import requests
import json
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(2,IO.OUT) #GPIO 2 -> Red LED as output
IO.setup(3,IO.OUT) #GPIO 3 -> Green LED as output
IO.setup(14,IO.IN) #GPIO 14 -> IR sensor as input
isItemPickedUp=False
previousState=False
while 1:
    if(IO.input(14)==True): #object is far away
        IO.output(2,True) #Red led ON
        IO.output(3,False) # Green led OFF
        isItemPickedUp=True
        #print ('Green off')
    
    if(IO.input(14)==False): #object is near
        IO.output(3,True) #Green led ON
        IO.output(2,False) # Red led OFF
        #print('Red off')
        isItemPickedUp=False
    if(previousState != isItemPickedUp):
        previousState=isItemPickedUp
        response = requests.post("https://api.pluspin.com:1233/tv-api/rack-Service", json={
            "rackId":"1824",
            "rackGridId":"2418",
            "pickUp":isItemPickedUp
            })
        print(response);
        print(response.content)        
        
    
