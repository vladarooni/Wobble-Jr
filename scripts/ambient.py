import requests

def send_ambient_pose(ip="192.168.4.1"):
    b = 0
    s = 0
    e = 0
    t = 85

    url = f"http://{ip}/js?json={{\"T\":122,\"b\":{b},\"s\":{s},\"e\":{e},\"h\":{t},\"spd\":40,\"acc\":10}}"

    try:
        response = requests.get(url)
        print("Lamp Response:", response.text)
    except Exception as e:
        print("ERROR SENDING CMD: ", e)

if __name__ == "__main__":
    send_ambient_pose()