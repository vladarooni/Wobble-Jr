import requests
import time
from idle import send_idle

def send_wave(ip="192.168.4.1"):
    send_idle()

    time.sleep(1)

    try:
           for i in range(3):
            #move elbow up
            url_up = f"http://{ip}/js?json={{\"T\":121,\"joint\":3,\"angle\":130,\"spd\":70,\"acc\":5}}"
            response_up = requests.get(url_up)
            print("Move up response:", response_up.text)

            #wait 2 seconds
            time.sleep(.35)  

            #move elbow down
            url_down = f"http://{ip}/js?json={{\"T\":121,\"joint\":3,\"angle\":100,\"spd\":70,\"acc\":5}}"
            response_down = requests.get(url_down)
            print("Move down response:", response_down.text)

            #wait 2 seconds
            time.sleep(.35)  

    except Exception as e:
        print("ERROR SENDING CMD: ", e)

if __name__ == "__main__":
    send_wave()