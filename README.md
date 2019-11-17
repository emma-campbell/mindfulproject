# MindfulProject :low_brightness:

Approximately one in six college aged kids will experience suicidal thoughts, yet no one talks about it. Backed by research, and utilizing CBT (*Cognitive Behavioral Therapy*)
**mindful.** aims to fix that. Watch as methods based on the science in [Mind Over Mood](https://www.amazon.com/Mind-Over-Mood-Second-Changing/dp/1462520421/ref=sr_1_1?keywords=mind+over+mood&qid=1573778033&sr=8-1) change the way you think, through the ease of your browser.

The MindfulProject web application will allow users to track, graph, and be mindful of their moods. The first four chapters of *Mind Over Mood* tackle the idea of becoming integrated with the way that you are feeling.

Today, journaling is a popular way to track things like our habits, thoughts and moods. However, it can be a very time consuming task that may bring more stress to a busy person’s life than it does comfort. Our website can serve as a quicker and more efficient way to track moods for people that don’t feel they are able to make time for traditional journaling. With targeted prompts, journaling can become easier and more effective than ever.


## Team

| Author        | Email                    |
| :--:          | :--:                     |
| Emma Campbell | ecampb10@u.rochester.edu |
| Melissa Welsh | mwelsh2@u.rochester.edu  |

## Running

Begin by activating a new virtual environment. On MacOS, this can be done by:

```
python3 -m virtualenv venv
```

and then activate this environment by running `. venv/bin/activate`. Once you are in your virtualenv, you can install all the required dependencies using the command

```
pip install -r requirements.txt
```

Now, you're going to want to create a `.env` file to toggle all your environment settings.

Run the following command to set up the required options!
```
cp .env-example .env
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

### Dependencies

To run and develop this application, you must use `virtualenv`. You can find download instructions in its documentation [here](https://virtualenv.pypa.io/en/latest/).
