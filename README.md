# flask_rest_api

```
├── flask_hello_world
           ├── app
           │   ├── __init__.py
           │   └── routes.py
           └── run.py
```

## Auto-reloading a Flask application
- Use the --debug option when you run your Flask app to enable debug mode
- `flask --app example_app.py --debug run`
- `flask --app main.py --debug run -h localhost`
- `flask run -h localhost`

### Flask 2.2
- We needed to set the FLASK_APP and FLASK_ENV=development environment variables.

- `export FLASK_APP=main.py`
- `export FLASK_ENV=development`
- `flask run`
- It is still possible to set FLASK_APP and FLASK_DEBUG=1 in Flask 2.2.


# POST an mp3 file using CURL
```
curl \
  -F "audio_file_id=1" \
  -F "file_comment=This is an audio file comment" \
  -F "file_name=@/Users/eli/Desktop/www/audio/roses.mp3; type=audio/mpeg" \
  http://127.0.0.1:5000/transcribe
```

## Query string arguments in REST APIs
http://127.0.0.1:5000/transcribe?fName=Ran&lName=Itzhak

# Docker
- `docker build . -t <new_image_name> `
- `docker container run --name new_container_name -t -d image_name`
```
docker container run -d \
    --name container_flask_rest_api -it \
    -p 5000:5000 \
    flask_rest_api
```
