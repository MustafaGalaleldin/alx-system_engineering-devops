#!/usr/bin/python3
"""export data in the JSON format"""

if __name__ == "__main__":
    import requests
    import sys
    import json

    user_name = ""
    results = []
    user_id = int(sys.argv[1])
    filename = f"{user_id}.json"
    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    todo_list = todo_response.json()
    user_response = requests.get("https://jsonplaceholder.typicode.com/users/")
    user_list = user_response.json()
    for user in user_list:
        if user.get("id") == user_id:
            user_name = user.get("username")
            break
    for todo in todo_list:
        if todo.get("userId") == user_id:
            temp_dic = {k: v for k, v in todo.items()
                        if k == "title" or k == "completed"}
            temp_dic["task"] = temp_dic.get("title")
            temp_dic["username"] = user_name
            del temp_dic["title"]
            results.append(temp_dic)
    jso = {f"{user_id}": results}
    with open(filename, "w") as f:
        f.write(json.dumps(jso))
