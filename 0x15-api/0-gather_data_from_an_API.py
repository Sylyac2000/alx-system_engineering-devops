#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    id = int(argv[1])

    """ get user """
    theurl = "https://jsonplaceholder.typicode.com/users/{:d}".format(id)
    response = requests.get(theurl)
    user = response.json()

    """ get user's todos """
    baseurl = "https://jsonplaceholder.typicode.com/users/"
    theurl = baseurl + "{:d}/todos".format(id)
    response = requests.get(theurl)
    todos = response.json()
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("     {}".format(c)) for c in completed]
