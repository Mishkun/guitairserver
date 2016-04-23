from flask import render_template, request, jsonify
from app import app, data, socketio
import logging



@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", page_code= data.generate_code())

@socketio.on('message', namespace='/mobile')
def mobile(message):
    print('recieved: ' + message)
    emit('message', {'data' : 'UP'})
    
@socketio.on('connect', namespace='/mobile')
def test_connect(message):
    print('connected')
    emit('my response', {'data': 'Connected', 'count': 0})

@socketio.on('disconnect', namespace='/mobile')
def test_disconnect(message):
    print('Client disconnected')

@app.route('/app')
def app_request():
    return '', 204

@app.route('/app/song', methods= ['GET'])
def song_request():
    song_name = request.args.get('name')
    import json
    logging.debug('Sending song data...')
    return json.dumps({ 'song_array' : data.song, 'song_bpm' : data.bpm }), 200
    
