FROM python:3.6-alpine3.9

RUN apk add --update alpine-sdk

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install -r requirements.txt

COPY server-producer.py /usr/src/app
COPY settings.py /usr/src/app

EXPOSE 8000

ENTRYPOINT ["python3"]

CMD ["server-producer.py"]
