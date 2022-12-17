#!/usr/bin/python3
"""Exports all employees to-do list to JSON format."""

import json
import requests


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/"
    users = requests.get(API_URL + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(API_URL + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
