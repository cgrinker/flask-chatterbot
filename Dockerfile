from python:alpine-3.7
add . /app
WORKDIR /app
run pip install -r requirements.txt

ENTRYPOINT ["python"  "app.py"]
