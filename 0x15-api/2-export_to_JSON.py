#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the JSON format.
"""


import json
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        theid = int(argv[1])
        API_URL = "https://jsonplaceholder.typicode.com/"
        user = requests.get("{}users/{}".format(API_URL, theid)).json()
        name = user.get("name")
        if name is not None:
            username = user.get('username')
            todos = requests.get(
                "{}todos?userId={}".format(
                    API_URL, theid)).json()

            tasks = [{"task": t.get("title"),
                      "username": username,
                      "completed": t.get("completed")} for t in todos]
            tasks_dict = {}
            tasks_dict[theid] = tasks

            with open("{}.json".format(theid), 'w', newline='') as jsonfile:
                json.dump(tasks_dict, jsonfile)
