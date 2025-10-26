from flask import Flask, render_template
import os
import sys

# initialize flask
app = Flask(__name__)

# determine absolute paths
base_dir = os.path.dirname(os.path.abspath(__file__))        # /path/to/wobble-jr/Website
scripts_dir = os.path.join(base_dir, '..', 'scripts')        # /path/to/wobble-jr/scripts

# add 'scripts' folder to python path so we can import _____.py
sys.path.insert(0, os.path.abspath(scripts_dir))

#imports
from lamp import send_lamp_pose
from wave import send_wave
from idle import send_idle
from ambient import send_ambient_pose
from dance1 import send_dance1

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/command/<action>')
def command(action):
    if action == 'lamp':
        try:
            send_lamp_pose()
        except Exception as e:
            print(f"Error running {action}: {e}", 500)
    elif action == 'wave':
        try:
            send_wave()
        except Exception as e:
            print(f"Error running {action}: {e}", 500)
    elif action == 'idle':
        try:
            send_idle()
        except Exception as e:
            print(f"Error running {action}: {e}", 500)
    elif action == 'ambient':
        try:
            send_ambient_pose()
        except Exception as e:
            print(f"Error running {action}: {e}", 500)
    elif action == 'dance1':
        try:
            send_dance1()
        except Exception as e:
            print(f"Error running {action}: {e}", 500)
    else:
        print(f"Unknown command: {action}", 400)
    return f"Running {action}"


if __name__ == '__main__':
    app.run(debug=True)
