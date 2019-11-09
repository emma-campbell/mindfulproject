# MindfulProject :low_brightness:

Open-source symptom tracking the the growth minded.

## Running

Begin by activating a new virtual environment. On MacOS, this can be done by:

```
python3 -m virtualenv venv
```

and then activate this environment by running `. venv/bin/activate`. Once you are in your virtualenv, you can install all the required dependencies using the command

```
pip install -r requirements.txt
```

Finally, run `flask run` and if everything is successful you should see the following:

```
* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [09/Nov/2019 16:26:25] "GET / HTTP/1.1" 200 -
```
