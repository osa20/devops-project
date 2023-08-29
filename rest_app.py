import os
import signal
from flask import Flask, request, jsonify
from method_type import get_user, create_user, update_user, delete_user


app = Flask(__name__)

# defining my database name
schema_name = "mydb"


# specifying supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user(user_id):
    if request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json

        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        creation_date = request_data.get('creation_date')
        try:
            create_user(user_id, user_name, creation_date)
        except Exception as err:
            if err.args[0] == 1062:
                return jsonify({'status': 'error', 'reason': 'id already exists'}), 500
            return jsonify({'status': 'error', 'reason': str(err)}), 500
        return jsonify({'status': 'ok', 'user_added': user_name}), 200

    elif request.method == 'GET':
        try:
            user_data = get_user(user_id)
        except Exception as err:
            return jsonify({'reason': str(err), 'status': 'error'}), 500
        if not user_data:
            return jsonify({'reason': 'no such id', 'status': 'error'}), 500
        return jsonify({'user_name': user_data[1], 'status': 'ok'}), 200

    elif request.method == 'PUT':
        # getting the json data payload from request
        request_data = request.json

        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        try:
            user_data = update_user(user_id, user_name)
        except Exception as err:
            return jsonify({'reason': str(err), 'status': 'error'}), 500
        if not user_data:
            return jsonify({'reason': 'no such id', 'status': 'error'}), 500
        return jsonify({'user_updated': user_name, 'status': 'ok'}), 200

    elif request.method == 'DELETE':
        try:
            user_data = delete_user(user_id)
        except Exception as err:
            return jsonify({'reason': str(err), 'status': 'error'}), 500
        if not user_data:
            return jsonify({'reason': 'no such id', 'status': 'error'}), 500
        return jsonify({'user_deleted': user_id, 'status': 'ok'}), 200


# Adding automatic termination to the REST API server
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


@app.errorhandler(404)
def resource_not_found(err):
    return jsonify(error=str(err)), 404


app.run(host='127.0.0.1', debug=True, port=5000)