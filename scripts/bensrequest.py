#wiggle wiggle
import requests
import time
from idle import send_idle

def send_bensrequest(ip="192.168.4.1"):
    #start idle
    send_idle

    #wait 
    time.sleep(2) 

    try:
        #move down
        url = f"http://{ip}/js?json={{\"T\":122,\"b\":0,\"s\":-70,\"e\":150,\"h\":90,\"spd\":60,\"acc\":10}}"
        try:
            response = requests.get(url)
            print("Dance2 Response:", response.text)
        except Exception as e:
            print("ERROR SENDING CMD: ", e)

        #side to side
        for i in range(2):
            #move right
            url_up = f"http://{ip}/js?json={{\"T\":121,\"joint\":1,\"angle\":50,\"spd\":90,\"acc\":70}}"
            response_up = requests.get(url_up)
            print("Move up response:", response_up.text)

            #wait 
            time.sleep(1)  

            #move left
            url_down = f"http://{ip}/js?json={{\"T\":121,\"joint\":1,\"angle\":-50,\"spd\":90,\"acc\":70}}"
            response_down = requests.get(url_down)
            print("Move down response:", response_down.text)

            #wait 
            time.sleep(1)  
    
        #raise
        send_idle()

        #look down & right
        url = f"http://{ip}/js?json={{\"T\":122,\"b\":78,\"s\":-30,\"e\":135,\"h\":175,\"spd\":40,\"acc\":10}}"
        try:
            response = requests.get(url)
            print("Dance1 Response:", response.text)
        except Exception as e:
            print("ERROR SENDING CMD: ", e)
                
        #wait 
        time.sleep(3) 

        #look left
        url = f"http://{ip}/js?json={{\"T\":122,\"b\":-78,\"s\":-70,\"e\":135,\"h\":175,\"spd\":80,\"acc\":20}}"
        try:
            response = requests.get(url)
            print("Dance1 Response:", response.text)
        except Exception as e:
            print("ERROR SENDING CMD: ", e)
        
        time.sleep(2.5)

        #look up slow
        url = f"http://{ip}/js?json={{\"T\":122,\"b\":0,\"s\":-45,\"e\":110,\"h\":100,\"spd\":20,\"acc\":10}}"
        try:
            response = requests.get(url)
            print("Idle Response:", response.text)
        except Exception as e:
            print("ERROR SENDING CMD: ", e)

    except Exception as e:
        print("ERROR SENDING CMD: ", e)

if __name__ == "__main__":
    send_bensrequest()
