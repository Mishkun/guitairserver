from flask import render_template, request, jsonify
from app import app, data
import logging

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", page_code= data.generate_code())

@app.route('/mobile', methods= ['PUT'])
def mobile():
    ip = request.remote_addr
    try:
        code = request.get_json(force= True)['code']
        data.codes.index(code)
    except:
        logging.info('Registration of {} failed, no such code: {}!'.format(ip, code))
        return '', 204
    data.codes.remove(code)
    data.mobile_clients[code] = ip
    logging.info('Registered code {} from {}'.format(data, ip))      
    return '', 200

@app.route('/app', methods= ['GET', 'DELETE'])
def app_request():
    code = request.args.get('code')
    logging.debug('Got a request from page with code {}'.format(code)) 
    if request.method == 'GET':
        client_ip = data.mobile_clients.setdefault(code, None)
        if client_ip:
            logging.debug('Connected {} to page!'.format(client_ip))
            return jsonify({'ip' : client_ip}), 200
        else:
            logging.debug('No connected ip-s with that code')
            return jsonify({'ip' : client_ip}), 204
    elif request.method == 'DELETE':
        try:
            data.codes.remove(code)
            return '', 200
        except ValueError:
            return '', 204

@app.route('/app/song', methods= ['GET'])
def song_request():
    song_name = request.args.get('name')
    import json
    logging.debug('Sending song data...')
    return json.dumps({ 'song_array' : data.song, 'song_bpm' : data.bpm }), 200
    
