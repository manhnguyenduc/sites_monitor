# -*- coding: utf-8 -*-

from Queue import Queue
from threading import Thread
import requests
from includes.settings import urls, num_threads
from includes.TaskSendNotifications import send_notifications

q = Queue()

notifications = []


def check_domain(domain):
    try:
        r = requests.get(domain, timeout=3)
        if r.status_code != 200:
            notifications.append({domain: r.status_code})
    except:
        notifications.append({domain: "is timeout"})


def mon_domain(q):
    while True:
        check_domain(q.get())
        q.task_done()


for u in urls:
    q.put(u)

for t in range(num_threads):
    worker = Thread(target=mon_domain, args=(q,))
    worker.setDaemon(True)
    worker.start()

q.join()

if notifications:
    print notifications
    send_notifications(str(notifications))
else:
    print "May vkl"
