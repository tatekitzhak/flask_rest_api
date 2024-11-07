from app import app
import time


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
