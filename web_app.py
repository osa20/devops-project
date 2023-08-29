import os
import signal
from flask import Flask
from method_type import get_user

app = Flask(__name__)


# # accessed via <HOST>:<PORT>/get_user_name/<user_id>
# Web interface returns the user name of a given user id  stored inside users table
@app.route('/get_user_name/<user_id>')
def get_user_name(user_id):
    global user_name
    try:
        user_name = (get_user(user_id))[1]
    except IndexError:
        return f"<H1 id='error'>no such user: {user_id}</H1>"
    except TypeError:
        return f"<H1 id='error'>no such user: {user_id}</H1>"
    return f"<H1 id='user'>{user_name}</H1>"


# Adding automatic termination to web application server
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


@app.errorhandler(404)
def page_not_found(err):
    return "<H1> 404 </H1><p>Page not found!</p>", 404


app.run(host='127.0.0.1', debug=True, port=5001)
