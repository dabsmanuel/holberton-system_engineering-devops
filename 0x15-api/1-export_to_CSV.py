#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter"""
import csv
from requests import get
from sys import argv


if __name__ == '__main__':
    url1 = get('https://jsonplaceholder.typicode.com/todos?userId=' + argv[1])
    url2 = get('https://jsonplaceholder.typicode.com/users/' + argv[1])

    d_todos = url1.json()
    d_users = url2.json()

    with open(argv[1] + '.csv', 'w') as file1:
        file_write = csv.writer(file1, quoting=csv.QUOTE_ALL)
        for i in range(len(d_todos)):
            file_write.writerow([d_users['id'],
                                d_users['username'],
                                d_todos[i]['completed'],
                                d_todos[i]['title']])
