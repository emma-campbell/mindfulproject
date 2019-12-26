#!/bin/sh
# this script is used to boot the docker container
source venv/bin/activate
while true; do
    flask db upgrade
    if [[ "$?" == 0 ]]; then
        break
    fi
    echo Deploy command failed, trying again in 5 seconds...
    sleep 5
done
exec gunicorn -b :5000 --access-logfile - --error-logfile - run:app
