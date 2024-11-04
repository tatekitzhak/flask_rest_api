from app import app
from flask import url_for, request


@app.route('/topic12/<int:post_id>', methods=['GET', 'PUT'])
def get_text2(post_id):

    if request.method == 'PUT':
        data = request.get_json()
        topic1 = data['topic1']
        topic2 = data['topic2']

        # return {'message': f'User {post_id} updated successfully', 'method': {request.method}}, 200
        return {'message': f'User {topic2} updated successfully', 'method': f'{request.method}'}, 200
    else:
        # return {'message': f'parm_req {post_id} updated successfully', 'method': {request.method}}, 200
        return {'message': f'User {post_id} updated successfully', 'method': f'{request.method}'}, 200
