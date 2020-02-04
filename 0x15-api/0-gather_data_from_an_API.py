#!/usr/bin/python3
"""Gets user, their tasks done, undone and total
and prints the done tasks"""
from requests import get
from sys import argv


if __name__ == '__main__':
    url1 = get('https://jsonplaceholder.typicode.com/todos?userId=' + argv[1])
    url2 = get('https://jsonplaceholder.typicode.com/users/' + argv[1])

    d_todos = url1.json()
    d_users = url2.json()
    completed = 0

    name = d_users.get('name')
    for task in d_todos:
        if task.get('completed'):
            completed += 1

    print("Employee {} is done with tasks({}/{}):".format(
        name, completed, len(d_todos)))

    for task in d_todos:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))
