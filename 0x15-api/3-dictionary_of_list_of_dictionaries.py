#!/usr/bin/python3
"""Python script to export ALL data in the JSON format"""

if __name__ == "__main__":
    import requests
    import json

    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    todo_list = todo_response.json()
    user_response = requests.get("https://jsonplaceholder.typicode.com/users/")
    user_list = user_response.json()
    result = {}
    for user in user_list:
        task_list = []
        user_id = user.get("id")
        for todo in todo_list:
            if todo.get("userId") == user_id:
                task_dict = {k: v for k, v in todo.items()
                             if k == "title" or k == "completed"}
                task_dict["task"] = task_dict.get("title")
                task_dict["username"] = user.get("username")
                del task_dict["title"]
                task_list.append(task_dict)
        result[f"{user_id}"] = task_list
    with open("todo_all_employees.json", "w") as f:
        f.write(json.dumps(result))
