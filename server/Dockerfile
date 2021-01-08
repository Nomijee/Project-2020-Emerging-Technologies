FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 --no-cache-dir install -r requirements.txt

COPY . .

ENV FLASK_APP=app.py

CMD flask run --host=0.0.0.0