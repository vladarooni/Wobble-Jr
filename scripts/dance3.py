#elbow front and back
import requests
import time
from idle import send_idle


def send_dance3(ip="192.168.4.1"):
    #start idle
    send_idle

    #wait 
    time.sleep(2) 
    sleep = .5

    try: 
        #for loop
        for i in range(2):
            #move to mid-left
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":40,\"s\":-35,\"e\":70,\"h\":120,\"spd\":80,\"acc\":30}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)

            #wait 
            time.sleep(sleep) 

            #move to left
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":80,\"s\":-60,\"e\":120,\"h\":165,\"spd\":80,\"acc\":30}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)

            #wait 
            time.sleep(sleep)     

            #move to mid-left
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":40,\"s\":-35,\"e\":70,\"h\":120,\"spd\":80,\"acc\":30}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)

            #wait 
            time.sleep(sleep) 

            #move to mid
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":0,\"s\":-20,\"e\":35,\"h\":80,\"spd\":80,\"acc\":30}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)

            #wait 
            time.sleep(sleep) 

            #move to mid-right
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":-40,\"s\":-35,\"e\":70,\"h\":120,\"spd\":80,\"acc\":30}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)
        
            #wait 
            time.sleep(sleep) 

            #move to right
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":-80,\"s\":-60,\"e\":120,\"h\":165,\"spd\":80,\"acc\":30}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)
            
            #wait 
            time.sleep(sleep) 

            #move to mid-right
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":-40,\"s\":-35,\"e\":70,\"h\":120,\"spd\":80,\"acc\":30}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)        

            #wait 
            time.sleep(sleep) 

            #move to mid
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":0,\"s\":-20,\"e\":35,\"h\":80,\"spd\":80,\"acc\":30}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)

            #wait 
            time.sleep(sleep) 

    except Exception as e:
        print("ERROR SENDING CMD: ", e)



if __name__ == "__main__":
    send_dance3()
