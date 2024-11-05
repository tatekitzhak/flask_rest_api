# FROM python:3.7.10
FROM python:3.7-slim

RUN pip install --upgrade pip
RUN pip install Flask

WORKDIR /app

COPY . .

# flask --app main.py --debug run -h localhost
#CMD ["flask", "--app", "main.py", "--debug", "run", "-h", "localhost"]

CMD ["python3", "main.py"]