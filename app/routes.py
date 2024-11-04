from app import app
# from markupsafe import escape
from flask import url_for, request


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
        data = request.get_json()
        topic1 = data['topic1']
        topic2 = data['topic2']

        # return {'message': f'User {post_id} updated successfully', 'method': {request.method}}, 200
        return {'message': f'User {topic2} updated successfully', 'method': f'{request.method}'}, 200
    else:
        # return {'message': f'parm_req {post_id} updated successfully', 'method': {request.method}}, 200
        return {'message': f'User {post_id} updated successfully', 'method': f'{request.method}'}, 200
