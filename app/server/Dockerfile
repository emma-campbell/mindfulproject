FROM alpine:latest

RUN apk update && \
    apk add build-base python3 python3-dev libffi-dev libressl-dev && \
    cd /usr/local/bin && \
    ln -s /usr/bin/python3 python && \
    pip3 install --upgrade pip && \
    pip3 install virtualenv gunicorn

COPY requirements.txt requirements.txt
COPY . /server
RUN pip install -r requirements.txt
WORKDIR /server
EXPOSE 8000

ENTRYPOINT ["sh", "boot.sh"]
CMD ["run:app"]