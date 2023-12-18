#!/usr/bin/python3
"""Script to retrieve TODO list progress for a given employee
ID using REST API
"""
import requests
import sys


if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    api_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{api_url}/users/{employee_id}")
    user_data = user_response.json()

    todos_response = requests.get(f"{api_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    total_done_tasks = len(done_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, total_done_tasks, total_tasks
        )
    )

    for task in done_tasks:
        print(f"\t {task['title']}")
