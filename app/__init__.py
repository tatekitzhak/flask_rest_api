from flask import Flask

app = Flask(__name__)

from app import routes
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 megabytes


from app.routes_endpoint import endpoints, post, put
from app.utils import log_request_info
