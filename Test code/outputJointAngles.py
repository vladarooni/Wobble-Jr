import requests
import argparse
import json
import time
import math

def get_joint_angles(ip):
    url = f"http://{ip}/js?json={{\"T\":105}}"  # command for servo rad feedback
    try:
        response = requests.get(url)
        response.raise_for_status()
        angles = json.loads(response.text)
        return angles
    except Exception as e:
        print("ERROR GETTING JOINT ANGLES: ". e)
        return None

def disable_torque(ip):
    url = f"http://{ip}/js?json={{\"T\":210,\"cmd\":0}}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Torque OFF. You can safely move joints manually")
    except Exception as e:
        print("FAILED. Torque ON: ", e)

def main():
    parser = argparse.ArgumentParser(description='Continuosuly get RoArm-M2 joint angles')
    parser.add_argument('ip', type=str, help='IP address of RoArm-M2')
    args = parser.parse_args()

    disable_torque(args.ip)

    try:
        while True:
            angles = get_joint_angles(args.ip)
            if angles:
                #convert rad to deg for readability
                base_deg = math.degrees(angles.get('b', 0))
                shoulder_deg = math.degrees(angles.get('s',0))
                elbow_deg = math.degrees(angles.get('e', 0))
                hand_deg = math.degrees(angles.get('t', 0))

                print(f"Base: {base_deg:.2f}°, Shoulder: {shoulder_deg:.2f}°, Elbow: {elbow_deg:.2f}°, Hand: {hand_deg:.2f}°")

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped by user")

if __name__ == "__main__":
    main()
