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

### Flask 2.2
- We needed to set the FLASK_APP and FLASK_ENV=development environment variables.

- `export FLASK_APP=main.py`
- `export FLASK_ENV=development`
- `flask run`
- It is still possible to set FLASK_APP and FLASK_DEBUG=1 in Flask 2.2.