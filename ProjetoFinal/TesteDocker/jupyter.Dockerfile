FROM jupyter/pyspark-notebook:latest

WORKDIR notebooks

COPY . .

RUN pip install -r requirements.txt