#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter"""
import json
from requests import get


if __name__ == '__main__':
    d = {}
    for user_id in range(1, 11):
        u1 = get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                 user_id))
        u2 = get('https://jsonplaceholder.typicode.com/users/{}'.format(
                 user_id))

        d_todos = u1.json()
        d_us = u2.json()

        d[str(user_id)] = [dict(task=task['title'],
                                completed=task['completed'],
                                username=d_us['username']) for task in d_todos]

    with open('todo_all_employees.json', 'w') as outfile:
        json.dump(d, outfile)
