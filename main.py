from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('about')

if __name__ == '__main__':
    app.run(debug=True)