FROM tensorflow/tensorflow:latest-py3

RUN pip install superintendent
RUN pip install sqlalchemy==1.3.24
RUN mkdir /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["app.py"]