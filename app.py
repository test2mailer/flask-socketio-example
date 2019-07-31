from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html',title='Flask-SocketIO')


@socketio.on('connect', namespace='/chat')
def test_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/chat')
def test_disconnect():
    print('Client disconnected')

@socketio.on('chat message', namespace='/chat'  )
def handle_message(message):
    print('received message: ' + message)
    emit('chat message', message, broadcast=True)

if __name__ == '__main__':
    #socketio.run(app)
    socketio.run(app, host='0.0.0.0', port=None, debug=True)  #allow remote connections to Flask
