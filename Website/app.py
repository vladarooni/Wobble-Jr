from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')    #this is the HTML buttons page

@app.route('/command/<action>')
def command(action):
    #run python scripts here
    if action == 'wave':
        subprocess.Popen(['python', 'wave.py'])
    elif action == 'lamp':
        subprocess.Popen(['python', 'lamp.py'])
    #TODO: add more actions as needed
    return f"Running {action} command"

if __name__ == '__main__':
    app.run(debug=True)