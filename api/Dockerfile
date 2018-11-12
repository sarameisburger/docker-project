FROM python:3.7-alpine

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY . /app/
WORKDIR /app

ENV FLASK_APP="api.py"
CMD [ "flask", "run", "--port=9001", "--host=0.0.0.0" ]