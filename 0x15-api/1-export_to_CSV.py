#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""


if __name__ == '__main__':
    import csv
    import requests
    from sys import argv

    if len(argv) == 2:
        id = int(argv[1])

        API_URL = "https://jsonplaceholder.typicode.com"

        """ get user """
        response = requests.get('{}/users/{}'.format(API_URL, id))
        user = response.json()

        """ get user's todos """
        response = requests.get('{}/users/{}/todos'.format(API_URL, id))
        todos = response.json()
        emp_name = user.get('name')
        tasks = list(filter(lambda x: x.get('userId') == id, todos))
        completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
        username = user.get("username")

        with open("{}.csv".format(id), "w", newline="") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            [writer.writerow(
                [id, username, t.get("completed"), t.get("title")]
            ) for t in tasks]
