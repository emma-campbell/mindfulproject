#!/bin/sh

# The postgres container takes longer to start up than the flask container does,
# therefore, we will wait until db activates to connect flask

SQL_HOST=db
SQL_PORT=5432

while ! nc -z $SQL_HOST $SQL_PORT; do
    echo Waiting for postgres server to start...
    sleep 5
done

echo Postgres started!
exec gunicorn -b :5000 run:app --reloads