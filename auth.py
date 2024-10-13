from flask import request, jsonify

def token_required():
    auth_header = request.headers.get('Authorization')

    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header.split(" ")[1]
        if token == "secret-token":
            return True
        else:
            return jsonify({'message': 'Invalid token!'}), 401
    else:
        return jsonify({'message': 'Token missing or incorrect format!'}), 401