from flask import Flask
from db_connector import *
import os
import signal

app = Flask(__name__)

# supported methods
@app.route('/users/get_user_data/<user_id>')
def user(user_id):
    try:
        name = get_user_id(user_id)
        return "<H1 id='user'>" + name + "</H1>", 200
    except:
        return "<H1 id='error'>""no such user: " + user_id + "</H1>", 500

@app.route('/stop_server')
def stop_server():
    try:
        os.kill(os.getpid(),signal.SIGINT)
        return {'status': 'ok', 'server stopped': 'true'}, 200  # status code
    except:
        return {'status': 'error', 'reason': 'server not responding'}, 500

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
app.run(host='127.0.0.1', debug=True, port=5001)
