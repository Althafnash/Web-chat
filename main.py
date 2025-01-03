from flask import Flask ,  render_template
from flask_socketio import SocketIO , send
import os 
from dotenv import load_dotenv

load_dotenv()
password = os.getenv("PASSWORD")

app = Flask(__name__)
app.config['SECRET'] = password
socketio = SocketIO(app , cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
    print(f"Recived Message: {message}")
    if message != 'User connected':
        send(message , broadcast=True)

@app.route('/')
def index():
    return render_template("index.html")

# Change localhsot to your ip addresse so you can talk with other compute in your network
if __name__ == "__main__":
    socketio.run(app, host="localhost")
    