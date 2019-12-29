FROM alpine:latest
LABEL Server image for mindful project

RUN apk update && \
    apk add build-base python3 python3-dev postgresql-dev libffi-dev openssl-dev && \
    cd /usr/local/bin && \
    ln -s /usr/bin/python3 python && \
    pip3 install --upgrade pip

ENV APP_PATH /usr/src/app/server
RUN mkdir -p $APP_PATH
WORKDIR $APP_PATH

COPY requirements.txt requirements.txt
RUN pip3 install --no-dependencies  -r requirements.txt
RUN pip3 install gunicorn

RUN adduser -D mindful
RUN chown -R mindful /usr/src/app/server && chmod -R 755 /usr/src/app/server

COPY . .
RUN chmod +x scripts/boot.sh
USER mindful

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 5000
ENTRYPOINT [ "./scripts/boot.sh" ]