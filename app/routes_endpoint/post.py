from app import app
from flask import url_for, request, jsonify, abort, make_response
import os

from mimetypes import add_type, guess_extension, guess_type
from werkzeug.utils import secure_filename

from app.utils.log_request_info import log_request_info

#: This contains audio file types (.wav, .mp3, .mp4, .aac, .ogg, .oga, and .flac).
ALLOWED_EXTENSIONS_AUDIO = tuple('.wav .mp3 .mp4 .aac .ogg .oga .flac'.split())


@app.route('/upload_audio_file_to_transcribe', methods=['GET', 'POST'])
def upload_audio_file():
    if request.method == 'POST':

        file = request.files['audio_file_rose']
        ext_name = guess_extension(file.mimetype)

        # if not ext_name:
        #     print("request::", ext_name)
        #     abort(400)
        print("request:", ext_name, ALLOWED_EXTENSIONS_AUDIO)

        if ext_name not in ALLOWED_EXTENSIONS_AUDIO:
            print(f'{ext_name} Not in: {ALLOWED_EXTENSIONS_AUDIO}')
            abort(400)

        # file.save('uploads/audio_file_rose.mp3')

        response_handle = {'message': f'User {1} updated successfully', 'method': f'{request.method}',
                           'file': f'{file}'}
        print(response_handle)
        return response_handle, 200
    else:
        return request.method, 201


@app.route("/transcribe", methods=['GET', 'POST'])
def transcribe_audio_file():
    ##
    # 4xx: Client Error
    ##

    if request.method == "GET":
        response_handle = {"status": 400, "method": f'{request.method}', "message": "Error", "error": {}}
        return jsonify(response_handle), 400

    print(f'{request.files.to_dict(flat=True)} Not in: {ALLOWED_EXTENSIONS_AUDIO}')
    uploaded_file_info = {}

    if request.method == 'POST':

        try:
            request_files_info = request.files.to_dict(flat=False)

            if 'hello_file' in request_files_info:
                print('audio_file_name1:', request_files_info, request.files.keys())

            log_request_info(request)

            print('form info:', request.form.to_dict(flat=False))
            for file_name in request.files.keys():
                uploaded_file = request.files[file_name].filename
                audio_file_name = request.files[file_name]
                ext_name = guess_extension(audio_file_name.mimetype)
                type_file = guess_type(uploaded_file)[0]

                uploaded_file_info = {
                    "origin_source_file_name": uploaded_file,
                    "file_name": file_name,
                    "extension_type": ext_name,
                    "Type file": type_file
                }

            print('uploaded_file_info:', uploaded_file_info)

            ##
            # Integrate A DeepSpeech - Speech to Text
            ##

            for list_type in request.files.to_dict(flat=False):
                getlist_type = request.files.to_dict(flat=False)[list_type][0]
                print('**', list_type, request.files.to_dict(flat=False)[list_type][0])
            ##
            # save files in a separate directory
            ##

            """  
            audio_file.seek(0)
            temp_path = f'uploads/temp_audio{ext_name}'
            audio_file.save(temp_path)
           #

           # clean up
           os.remove(temp_path)
           """

            ##
            # 2xx: Successful
            ##
            response_handle = {
                "status": 200,
                "method": f'{request.method}',
                "message": "ok",
                "data": uploaded_file_info,
                "transcribe": {}
            }
            return jsonify(response_handle), 200
        except Exception as e:
            ##
            # 5xx: Server Error
            ##
            print(e)
            response_handle = {
                "status": 500,
                "method": f'{request.method}',
                "message": "Error",
                "error": str(e)
            }
            return jsonify(response_handle), 500

##
# Handling large file uploads
##
@app.errorhandler(413)
def too_large(e):
    return make_response(jsonify(message="File is too large"), 413)

