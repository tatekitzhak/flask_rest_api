# flask_rest_api

# The app tree directory
```
├── flask_rest_api
        ├── config.py
        ├── docker-compose.yml
        ├── Dockerfile
        ├── .dockerignore
        ├── .gitignore
        ├── 
        ├── README.md
        ├── requirements.txt
        ├── run.py
        ├── app
        │   ├── api
        │   │   ├── errors.py
        │   │   ├── __init__.py
        │   │   ├── skills.py
        │   │   └── validations.py
        │   ├── auth
        │   │   ├── emails.py
        │   │   ├── __init__.py
        │   │   ├── oauth.py
        │   │   └── routes.py
        │   ├── content
        │   │   ├── forms.py
        │   │   ├── __init__.py
        │   │   └── routes.py
        │   ├── deepspeech-ffmpeg
        │   │   ├── 
        │   │   ├── 
        │   │   └── routes.py
        │   ├── errors
        │   │   ├── handlers.py
        │   │   └── __init__.py
        │   ├── extract-audio-from-yt
        │   │   ├── handlers.py
        │   │   └── __init__.py
        │   ├── __init__.py
        │   ├── main
        │   │   ├── __init__.py
        │   │   └── routes.py
        │   ├── models.py
        │   ├── static        
        │   └── templates    
        ├── skills.db
        └── tests

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
  -F "file_name=@/Users/eli/Desktop/www/audio/manythings-US-History-Series-Jefferson-Is-Elected-President-in-1800-But-Only-on-the-36th-Vote.mp3; type=audio/mpeg" \
  http://127.0.0.1:5000/transcribe
```
- `curl -X POST -H "application/json" -d '{"key":"val"}' UR`

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
