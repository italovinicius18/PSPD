FROM python:3.7

WORKDIR /producer

COPY . .

RUN pip install -r requirements.txt