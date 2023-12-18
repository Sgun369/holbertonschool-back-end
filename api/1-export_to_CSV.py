#!/usr/bin/python3
"""Script to retrieve TODO list progress for a given employee
ID using REST API and export data in CSV format
"""
import requests
import csv
import sys

def export_to_csv(employee_id, user_data, todos_data):
    file_name = f"{employee_id}.csv"

    with open(file_name, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in todos_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": user_data['username'],
                "TASK_COMPLETED_STATUS": str(task['completed']),
                "TASK_TITLE": task['title']
            })

    print(f"Data exported to {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    api_url = "https://jsonplaceholder.typicode.com"

    try:
        user_response = requests.get(f"{api_url}/users/{employee_id}")
        user_response.raise_for_status()
        user_data = user_response.json()

        todos_response = requests.get(f"{api_url}/todos?userId={employee_id}")
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task['completed']]
        total_done_tasks = len(done_tasks)

        print(
            f"Employee {user_data['name']} is done with tasks({total_done_tasks}/{total_tasks}):"
        )

        for task in done_tasks:
            print(f"\t{task['title']}")

        export_to_csv(employee_id, user_data, todos_data)

    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
