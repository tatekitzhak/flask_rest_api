from app import app
from flask import url_for, request


# @app.route('/upload_file', methods=['POST'])
@app.post('/upload_file1')
def upload_file1():
    if request.method == 'POST':
        print()
        request_data = request.get_json()

        language = request_data['language']
        framework = request_data['framework']
        return language, 201
    else:
        return new_friend, 201


@app.route('/upload_audio_file', methods=['GET', 'POST'])
def upload_audio_file():

    if request.method == 'POST':
        f = request.files['audio_file_rose']
        print("request:", f)
        f.save('uploads/audio_file_rose.mp3')

        response_handle = {'message': f'User {1} updated successfully', 'method': f'{request.method}', 'file': f'{f}'}
        print(response_handle)
        return response_handle, 200
    else:
        return request.method, 201
