#this program should send movement commands to the RoArm MS-2 via HTTP requests
#it's configured to run when the laptop is connected directly to the robot's default wifi access point (AP)

#imports
import requests
import sys

#configuration (AP MODE)
ROBOT_IP = "192.168.4.1"    #fixed IP addresse bc it's what the robot uses when broadcasting its wifi
ROBOT_PORT = "80"           #default port for RoArm MS-2
COMMAND_ENDPOINT = "/"

ROBOT_URL = f"http://{ROBOT_IP}:{ROBOT_PORT}{COMMAND_ENDPOINT}" 

#Payload to move joint 1 (Base aka Yaw)
MOVE_BASE_PAYLOAD = {
    "servos": [
        {
            "id": 2,
            "angle": 60,
            "speed": 50     #not measured in exact units
        }
    ],
    "mode": "position_control"
}

#Payload to move to init pos
INIT_PAYLOAD = {
    "servos": [
        {"id": 1, "angle": 0, "speed": 50},  # base
        {"id": 2, "angle": 45, "speed": 50}, # shoulder
        {"id": 3, "angle": 90, "speed": 50}, # elbow 
        {"id": 4, "angle": 45, "speed": 50}, # wrist
        {"id": 5, "angle": 90, "speed": 50}, # wrist roll
        {"id": 6, "angle": 0, "speed": 50},  # gripper
    ],
    "mode": "position_control"
}

#sends a specified JSON cmd to the robot and prints the result
def send_move_command(payload, description):
    print(f"Connecting to RoArm at: {ROBOT_URL}")
    print(f"Attempting command: {description}...")

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(
            ROBOT_URL,
            json=payload,
            headers=headers,
            timeout=5
        )
        response.raise_for_status()

        print(f"\n Command send successfully! {description}")
        print(f"Status Code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print(f"\nCONNECTION FAILED: Is your laptop connected to the 'RoArm-M2' Wi-Fi (192.168.4.1)?")
    except requests.exceptions.RequestException as e:
        print(f"\nREQUEST FAILED: {e}")
    except Exception as e:
        print(f"\nUNEXPECTED ERROR: {e}")

if __name__ == "__main__":
    #check if user passed 'init' as a cmd lin argument
    if 'init' in sys.argv:
        send_move_command(INIT_PAYLOAD, "Move to INIT Pos")
    else:
        send_move_command(MOVE_BASE_PAYLOAD, "Move Joint 1 to 90 deg")