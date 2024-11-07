from app import app
# from markupsafe import escape
from flask import url_for, request, jsonify


@app.route('/')
def index():
    return 'Index Page'


# @app.route('/upload_file', methods=['POST'])
@app.post('/upload_file')
def upload_file():
    if request.method == 'POST':
        request_data = request.get_json()

        language = request_data['language']
        framework = request_data['framework']
        return language, 201
    else:
        return new_friend, 201


@app.route('/topic/<int:post_id>', methods=['GET', 'PUT'])
def get_text(post_id):

    if request.method == 'PUT':

        topic1 = data['topic1']
        topic2 = data['topic2']

        # return {'message': f'User {post_id} updated successfully', 'method': {request.method}}, 200
        return {'message': f'User {topic2} updated successfully', 'method': f'{request.method}'}, 200
    else:
        # return {'message': f'parm_req {post_id} updated successfully', 'method': {request.method}}, 200
        return {'message': f'User {post_id} updated successfully', 'method': f'{request.method}'}, 200


@app.errorhandler(404)
def not_found():
    """Page not found."""
    return jsonify({'message': 'Error', 'method': f'{request.method}'}), 404


@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return jsonify({'message': 'Error', 'method': f'{request.method}'}), 400


@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return jsonify({'message': 'Error', 'method': f'{request.method}'}), 500
