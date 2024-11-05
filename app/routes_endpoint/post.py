from app import app
from flask import url_for, request, jsonify, abort
import os
import time
from mimetypes import add_type, guess_extension, guess_type

#: This contains audio file types (.wav, .mp3, .mp4, .aac, .ogg, .oga, and .flac).
ALLOWED_EXTENSIONS_AUDIO = tuple('.wav .mp3 .mp4 .aac .ogg .oga .flac'.split())


@app.route('/upload_audio_file', methods=['GET', 'POST'])
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


def log_request_info(request):
    app.logger.warning("\n\nNEW LOG\ntime:".format(time.time()))
    app.logger.warning("request.path: {0}".format(request.path))
    app.logger.warning("request.method: {0}".format(request.method))
    app.logger.warning("request.host: {0}".format(request.host))
    app.logger.warning("request.url: {0}".format(request.url))
    app.logger.warning("request.script_root: {0}".format(request.script_root))
    app.logger.warning("request.files.to_dict(flat=False): {0}".format(str(request.files.to_dict(flat=False))))
    app.logger.warning("request.args.getlist('name'): {0}".format(request.args.getlist('name')))
    app.logger.warning("request.form.to_dict(flat=False): {0}".format(request.form.to_dict(flat=False)))
    app.logger.warning("request.form.keys(): {0}".format(request.form.keys()))
    app.logger.warning("request.files: {0}".format(request.files))
    app.logger.warning("request.files.items(): {0}".format(request.files.items()))
    app.logger.warning("request.headers: {0}".format(request.headers))

    # print('request.method : %s', request.method)
    # print('request.files : %s', str(request.files.to_dict(flat=False)))
    # print('request.args : %s', request.args.getlist('name'))
    # print('request.form : %s', request.form.to_dict(flat=False))
    # print('request.values : %s', request.values)
    # print('request.files.items() : %s', request.files.items())


@app.route("/transcribe", methods=['GET', 'POST'])
def transcribe_audio_file():
    args = request.args
    print("args:", args.get("name"))

    request_files_info = request.files.to_dict(flat=False)
    # audio_file = request.files['audio_file_name']
    # ext_name = guess_extension(audio_file.mimetype)
    log_request_info(request)

    if 'audio_file_name1' in request_files_info:
        print('audio.mp3:', request_files_info)

    if "audio_file_name1" in request.files:
        print('****:', request.files)

    for key in request.files.keys():
        print('****:', key)

    print(f'{request.files.to_dict(flat=True)} Not in: {ALLOWED_EXTENSIONS_AUDIO}')

    for list_type in request.files.to_dict(flat=False):
        getlist_type = request.files.to_dict(flat=False)[list_type][0]
        print('**', list_type, request.files.to_dict(flat=False)[list_type][0])
    ##
    # 4xx: Client Error
    ##
    try:
        # save a temporary instance of the file to satisfy the API
        # audio_file.seek(0)
        # temp_path = f'uploads/temp_audio{ext_name}'
        # audio_file.save(temp_path)
        # #
        # # with open(temp_path, "rb") as file:
        # #     transcription = client.audio.transcriptions.create(
        # #         model="whisper-1",
        # #         file=file
        # #     )
        # #
        # # clean up
        # os.remove(temp_path)

        # #
        # 2xx: Successful
        ##
        response_handle = {"status": 200, "method": f'{request.method}', "message": "ok", "data": ""}
        return jsonify(response_handle), 200
    except Exception as e:
        ##
        # 5xx: Server Error
        ##
        print(e)
        response_handle = {"status": 500, "method": f'{request.method}', "message": "Error", "error": str(e)}
        return jsonify(response_handle), 500


@app.errorhandler(404)
def page_not_found(error):
    response_handle = {"status": 404, "method": f'{error}', "message": "Error", "error": str(error)}
    return jsonify(response_handle), 404


@app.route('/search', methods=['GET'])
def search():
    args = request.args
    print("args:", args)
    return args
