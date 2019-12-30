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

For cross-platform reliability, development and running of this application is done through [Docker](https://www.docker.com/get-started). After installing, make sure that you have both
Docker and docker-compose installed on your machine by issuing the command

```bash
docker --version
```
and
```bash
docker-compose --version
```
Once you have docker, set up is simple. With the provided Makefile you
can get all the containers up and running by executing

```bash
make up
```

After this, navigate to http://localhost:8080 and check it out!
## Debugging

The command `make up` doesn't show the logs of all containers by default, 
to check the logs, run 

```bash
docker logs <container-name>
```

to view the logs of a specific container.
