#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""


import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        user = argv[1]
        API_URL = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(API_URL, user))
        name = req.json().get("name")
        if name is not None:
            jreq = requests.get(
                "{}todos?userId={}".format(
                    API_URL, user)).json()
            alltask = len(jreq)
            completed = []
            for t in jreq:
                if t.get("completed") is True:
                    completed.append(t)
            count = len(completed)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, count, alltask))
            for title in completed:
                print("\t {}".format(title.get("title")))
