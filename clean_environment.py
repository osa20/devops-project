import requests

# frontend server
try:
    requests.get('http://127.0.0.1:5000/stop_server')
except Exception as err:
    print(err)

# backend server
try:
    requests.get('http://127.0.0.1:5001/stop_server')
except Exception as err:
    print(err)