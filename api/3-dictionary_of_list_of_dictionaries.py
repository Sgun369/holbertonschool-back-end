#!/usr/bin/python3
"""Gathering the needed informations from the API."""
import json
import requests

if __name__ == '__main__':
    resp_users = requests.get('https://jsonplaceholder.typicode.com/users')
    resp_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    json_dic = dict()
    small_dic = dict()
    for u in resp_users.json():
        user_id = u['id']
        if user_id not in json_dic:
            json_dic[user_id] = []

        for t in resp_todos.json():
            small_dic = {}
            if user_id == t['userId']:
                small_dic["username"] = u['username']
                small_dic["task"] = t['title']
                small_dic["completed"] = t['completed']

                json_dic[user_id].append(small_dic)
    with open(f"todo_all_employees.json", 'w') as j_file:
        json.dump(json_dic, j_file, indent=4)
