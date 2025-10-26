import requests

def send_idle(ip="192.168.4.1"):
    b = 0
    s = -45
    e = 110
    t = 100

    url = f"http://{ip}/js?json={{\"T\":122,\"b\":{b},\"s\":{s},\"e\":{e},\"h\":{t},\"spd\":40,\"acc\":10}}"

    try:
        response = requests.get(url)
        print("Idle Response:", response.text)
    except Exception as e:
        print("ERROR SENDING CMD: ", e)

if __name__ == "__main__":
    send_idle()