#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""
if __name__ == "__main__":

    import requests
    import csv
    import sys

    user_id = int(sys.argv[1])
    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    todo_list = todo_response.json()
    user_response = requests.get("https://jsonplaceholder.typicode.com/users/")
    user_list = user_response.json()
    user_name = ""
    results = []
    fields = ["userId", "username", "completed", "title"]
    for user in user_list:
        if user.get("id") == user_id:
            user_name = user.get("username")
            break
    for todo in todo_list:
        if todo.get("userId") == user_id:
            temp_dict = {k: v for k, v in todo.items() if k != "id"}
            temp_dict["username"] = user_name
            results.append(temp_dict)
    with open(f"{user_id}.csv", "w") as csvfile:
        writer = csv.DictWriter(f=csvfile, fieldnames=fields, quotechar='"',
                                quoting=csv.QUOTE_ALL)
        writer.writerows(results)
