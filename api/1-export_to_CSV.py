#!/usr/bin/python3
"""Gathering the needed informations from the API."""
import csv
import json
import requests
from sys import argv

if __name__ == '__main__':
    resp_users = requests.get('https://jsonplaceholder.typicode.com/users')
    resp_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    user_id = argv[1]

    for i in resp_users.json():
        if i['id'] == int(user_id):
            user_name = i['username']
    with open(f'{user_id}.csv', 'w') as f:
        for i in resp_todos.json():
            if i['userId'] == int(user_id):
                task = i['completed']
                title = i['title']
                f.write(
                    f"\"{argv[1]}\",\"{user_name}\",\"{task}\",\"{title}\"\n")
