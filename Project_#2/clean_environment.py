import requests

#Stopping rest & web servers
try:
    requests.get( 'http://127.0.0.1:5000/stop_server')
    print("Rest app stopped")
except:
    print("Server not responding for request")

try:
    requests.get( 'http://127.0.0.1:5001/stop_server')
    print("Web app stopped")
except:
    print("Server not responding for request")
