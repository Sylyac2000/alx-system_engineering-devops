#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    if len(argv) == 2:
        id = int(argv[1])

        API_URL = "https://jsonplaceholder.typicode.com"

        """ get user """
        response = requests.get('{}/users/{}'.format(API_URL, id))
        user = response.json()

        """ get user's todos """
        response = requests.get('{}/todos'.format(API_URL))
        todos = response.json()
        emp_name = user.get('name')
        tasks = list(filter(lambda x: x.get('userId') == id, todos))
        completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
        print(
            'Employee {} is done with tasks({}/{}):'.format(
                emp_name,
                len(completed_tasks),
                len(tasks)
            )
        )
        if len(completed_tasks) > 0:
            for task in completed_tasks:
                print('\t {}'.format(task.get('title')))
