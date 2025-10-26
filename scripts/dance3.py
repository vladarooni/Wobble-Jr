#elbow front and back
import requests
import time
from ambient import send_ambient_pose
from idle import send_idle

def send_dance3(ip="192.168.4.1"):
    #start ambient
    send_ambient_pose()

    #wait 
    time.sleep(1) 
    sleep = .65

    try: 
        #for loop
        for i in range(2):
            #move 1/3 right
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":40,\"s\":5,\"e\":-20,\"h\":85,\"spd\":50,\"acc\":50}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)

            #wait 
            time.sleep(sleep) 

            #move 2/3 right
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":80,\"s\":-15,\"e\":20,\"h\":85,\"spd\":50,\"acc\":50}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)

            #wait 
            time.sleep(sleep)     

            #move 3/3 right
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":120,\"s\":5,\"e\":-20,\"h\":85,\"spd\":50,\"acc\":50}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)

            #wait 
            time.sleep(sleep) 

            #move to 2/3 right
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":80,\"s\":-15,\"e\":20,\"h\":85,\"spd\":50,\"acc\":50}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)

            #wait 
            time.sleep(sleep) 

            #move 1/3 right
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":40,\"s\":5,\"e\":-20,\"h\":85,\"spd\":50,\"acc\":50}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)
        
            #wait 
            time.sleep(sleep) 

            #move to mid
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":0,\"s\":-15,\"e\":20,\"h\":85,\"spd\":50,\"acc\":50}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)
            
            #wait 
            time.sleep(sleep) 

            #move to 1/3 left
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":-40,\"s\":5,\"e\":-20,\"h\":85,\"spd\":50,\"acc\":50}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)       

            #wait 
            time.sleep(sleep) 

            #move to 2/3 left
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":-80,\"s\":-15,\"e\":20,\"h\":85,\"spd\":50,\"acc\":50}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)

            #wait 
            time.sleep(sleep) 

            #move 3/3 left
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":-120,\"s\":5,\"e\":-20,\"h\":85,\"spd\":50,\"acc\":50}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)

            #wait 
            time.sleep(sleep) 

            #move to 2/3 left
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":-80,\"s\":-15,\"e\":20,\"h\":85,\"spd\":50,\"acc\":50}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)

            #wait 
            time.sleep(sleep) 

            #move to 1/3 left
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":-40,\"s\":5,\"e\":-20,\"h\":85,\"spd\":50,\"acc\":50}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)   
                
            #move to mid
            url = f"http://{ip}/js?json={{\"T\":122,\"b\":0,\"s\":-15,\"e\":20,\"h\":85,\"spd\":50,\"acc\":50}}"
            try:
                response = requests.get(url)
                print("Dance1 Response:", response.text)
            except Exception as e:
                print("ERROR SENDING CMD: ", e)
            
            #wait 
            time.sleep(sleep)       

    except Exception as e:
        print("ERROR SENDING CMD: ", e)

    send_idle()


if __name__ == "__main__":
    send_dance3()
