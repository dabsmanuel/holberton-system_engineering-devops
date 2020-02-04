#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter"""
from requests import get
from sys import argv


if __name__ == '__main__':
    url1 = get('https://jsonplaceholder.typicode.com/todos?userId=' + argv[1])
    url2 = get('https://jsonplaceholder.typicode.com/users/' + argv[1])

    d_todos = url1.json()
    d_users = url2.json()
    completed = 0

    if d_todos and d_users:
        name = d_users.get('name')
        for task in d_todos:
            if task.get('completed') is True:
                completed += 1
        cmp_tasks = completed
        tot_tasks = len(d_todos)

        print("Employee {} is done with tasks({}/{}):".format(
            name, cmp_tasks, tot_tasks))
        for task in d_todos:
            if task.get('completed') is True:
                print("\t{}".format(task.get('title')))
