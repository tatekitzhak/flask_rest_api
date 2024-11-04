from app import app
from flask import url_for, request


# @app.route('/upload_file', methods=['POST'])
@app.post('/upload_file2')
def upload_file2():
    if request.method == 'POST':
        print()
        request_data = request.get_json()

        language = request_data['language']
        framework = request_data['framework']
        return language, 201
    else:
        return new_friend, 201


@app.route('/upload_audio_file2', methods=['GET', 'POST'])
def upload_audio_file2():
    if request.method == 'POST':
        print(request.method)
        # f = request.files['the_file']
        # f.save('uploads/uploaded_file.txt')
