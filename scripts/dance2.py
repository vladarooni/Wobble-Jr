#wiggle wiggle
import requests
import time
from idle import send_idle

def send_dance2(ip="192.168.4.1"):
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

        #wait 
        time.sleep(.6) 

        #for loop
        for i in range(4):
            #move to left
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":55,\"s\":-70,\"e\":150,\"h\":70,\"spd\":100,\"acc\":60}}"
            try:
                response = requests.get(url)
                print("Dance2 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)

            #wait 
            time.sleep(1.2)     

            #move to right
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":-55,\"s\":-70,\"e\":150,\"h\":110,\"spd\":100,\"acc\":60}}"
            try:
                response = requests.get(url)
                print("Dance2 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)

            #wait 
            time.sleep(1.2) 

    except Exception as e:
        print("ERROR SENDING CMD: ", e)

    #send idle again
    send_idle()

if __name__ == "__main__":
    send_dance2()
