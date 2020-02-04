#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter"""
import json
from requests import get
from sys import argv


if __name__ == '__main__':
    url1 = get('https://jsonplaceholder.typicode.com/todos?userId=' + argv[1])
    url2 = get('https://jsonplaceholder.typicode.com/users/' + argv[1])

    d_todos = url1.json()
    d_users = url2.json()

    d_dict = {}
    d_dict[d_users['id']] = []
    for task in d_todos:
        d_dict[d_users['id']].append({"task": task['title'],
                                     "completed": task['completed'],
                                      "username": d_users['username']})

    with open(argv[1] + '.json', 'w') as outfile:
        json.dump(d_dict, outfile)
