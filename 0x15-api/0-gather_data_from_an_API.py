#!/usr/bin/python3
"""
a Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

if __name__ == '__main__':
    import requests
    import sys

    employee_id = int(sys.argv[1])
    url_todos = "https://jsonplaceholder.typicode.com/todos/"
    url_users = "https://jsonplaceholder.typicode.com/users/"
    todo_response = requests.get(url_todos)
    todo_response_list = todo_response.json()
    user_response = requests.get(url_users)
    user_response_list = user_response.json()
    EMPLOYEE_NAME = ""
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = ""
    for user in user_response_list:
        if user.get('id') == employee_id:
            EMPLOYEE_NAME = user.get('name')
    for todo in todo_response_list:
        if todo.get('userId') == employee_id:
            TOTAL_NUMBER_OF_TASKS += 1
            if todo.get('completed') == True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE += f"\n\t {todo.get('title')}"
    print(f"Employee {EMPLOYEE_NAME} is done with tasks("
            f"{NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):", end="")
    print(TASK_TITLE)
