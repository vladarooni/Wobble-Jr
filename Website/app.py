from flask import Flask, render_template
import os
import sys

# initialize flask
app = Flask(__name__)

# determine absolute paths
base_dir = os.path.dirname(os.path.abspath(__file__))        # /path/to/wobble-jr/Website
scripts_dir = os.path.join(base_dir, '..', 'scripts')        # /path/to/wobble-jr/scripts

# add 'scripts' folder to Python path so we can import lamp.py
sys.path.insert(0, os.path.abspath(scripts_dir))

# Now the import should work
from lamp import send_lamp_pose


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/command/<action>')
def command(action):
    if action == 'lamp':
        try:
            send_lamp_pose()
            return f"Command executed: {action}"
        except Exception as e:
            return f"Error running {action}: {e}", 500
    elif action == 'wave':
        return "Wave command not yet implemented"
    else:
        return f"Unknown command: {action}", 400


if __name__ == '__main__':
    app.run(debug=True)
