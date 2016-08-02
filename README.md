## Simple Python script monitor website

Check website with python, send notification if response code <> 200 or response time > 3


- Edit includes/settings.py.
- Run monitor.py with crontab

`* * * * * python /path/to/monitor.py > /dev/null &2 > 1`
