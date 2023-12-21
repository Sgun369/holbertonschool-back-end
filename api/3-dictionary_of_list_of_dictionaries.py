#!/usr/bin/python3
""" export data in the JSON format."""
import json
import requests


if __name__ == '__main__':
    resp_users = requests.get('https://jsonplaceholder.typicode.com/users')
    resp_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    json_dict = dict()
    small_dict = dict()

    for u in resp_users.json():
        user_id = u['id']
        if user_id not in json_dict:
            json_dict[user_id] = []

        for t in resp_todos.json():
            small_dict["username"] = u['username']
            small_dict["task"] = t['title']
            small_dict["completed"] = t['completed']

            json_dict[user_id].append(small_dict)

    with open(f"todo_all_employees.json", "w") as j_file:
        json.dump(json_dict, j_file, indent=2)
