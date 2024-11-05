from app import app

#  https://github.com/wulfebw/flask_attempts/blob/master/video_upload.py

if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0", port=5000, debug=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# app.wsgi_app = ProxyFix(app.wsgi_app)
#
# if __name__ == '__main__':
#     app.run(
#         host="0.0.0.0",
#         port=int("80"),
#         debug=True
#     )
#
# flask --app example_app.py --debug run



########################## DEMO
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello():
#     return "Demo Flask & Docker application is up and running!"
#
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000)