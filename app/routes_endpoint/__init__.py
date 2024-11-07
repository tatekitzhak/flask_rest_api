from flask import Flask

app = Flask(__name__)

##
# File Size Restrictions - Limiting the size of uploaded
##

# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 megabytes

from app.routes_endpoint import endpoints, put
