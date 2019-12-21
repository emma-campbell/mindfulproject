#!/bin/sh
# this script is used to boot a Docker container
source venv/bin/activate
while true; do
    flask db upgrade
    if [[ "$?" == 0 ]]; then
        break
    fi
    echo Deploy command failed, trying again in 5 seconds...
    sleep 5
done
exec gunicorn -b --access-logfile - --error-logfile - application:create_app
