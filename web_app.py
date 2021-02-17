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


app.run(host='127.0.0.1', debug=True, port=5001)
