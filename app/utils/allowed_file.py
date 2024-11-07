
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_EXTENSIONS_AUDIO = tuple('.wav .mp3 .mp4 .aac .ogg .oga .flac'.split())
MIME_TYPE = ['audio/mp3', 'audio/mp4', 'audio/wav', 'audio/x-wav', 'audio/x-m4a', 'audio/mpeg', 'audio/mpeg']


def allowed_mime_type(file):
    mime = magic.from_buffer(file.stream.read(2048), mime=True)
    file.stream.seek(0)  # Reset file pointer after reading
    return mime in ['image/png', 'image/jpeg', 'application/pdf']


def allowed_file(filename):
    allowed_mime_type = mime in MIME_TYPE
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS