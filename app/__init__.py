from flask import Flask
import logging
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

if app.debug:
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(message)s', datefmt='%H:%M:%S')
else:
    logging.basicConfig(level=logging.INFO, format='%(levelname)s <%(asctime)s> : %(message)s', datefmt='%d.%m.%Y %H:%M:%S')


from app import views, data
data.load_song()

if __name__ == '__main__':
    socketio.run(app)
