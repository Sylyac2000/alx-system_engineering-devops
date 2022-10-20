#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""


import csv
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        theid = int(argv[1])
        API_URL = "https://jsonplaceholder.typicode.com/"
        user = requests.get("{}users/{}".format(API_URL, theid)).json()
        name = user.get("name")
        if name is not None:
            todos = requests.get(
                "{}todos?userId={}".format(
                    API_URL, theid)).json()

            with open("{}.csv".format(theid), 'w', newline='') as csvfile:
                taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                for t in todos:
                    taskwriter.writerow([theid, user.get('username'),
                                        t.get('completed'), t.get('title')])
