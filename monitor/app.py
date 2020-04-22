from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__, static_url_path='', static_folder='static')

app.config['SECRET_KEY'] = 'ok093f-=o1kdj09j3f'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('game-state')
def handle_game_state(data):
    socketio.emit('game-state', data)


if __name__ == "__main__":
    socketio.run(app, debug=True, port=5000)
