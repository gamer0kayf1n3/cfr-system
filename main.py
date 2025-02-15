from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send, emit
import requests
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('about')

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', to=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)

@socketio.on('connect')
def test_connect(auth):
    
    emit('global', "Connected (server)")

@socketio.on('disconnect')
def test_disconnect(reason):
    print('Client disconnected, reason:', reason)

if __name__ == '__main__':
    app.run(debug=True)