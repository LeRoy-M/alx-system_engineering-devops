#!/usr/bin/python3
"""Module that uses a REST API for all employees ID's to export
data into a JSON file
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url1 = "https://jsonplaceholder.typicode.com/users/"
    url2 = [f"https://jsonplaceholder.typicode.com/users/{i}/todos"
            for i in range(1, (len(url1) + 1))]
    response1 = json.loads(requests.get(url1).text)
    response2 = [json.loads(requests.get(url2[i]).text)
                 for i in range(len(url2))]

    t_lists = []

    for i in range(len(response1)):
        t_lists.append({
            f"{tuple(response1)[i].get('id')}": [{[{
                "username": f"{response1[i].get('username')}",
                "task": f"{response2[i][j].get('title')}",
                "completed": f"{response2[i][j].get('completed')}"}
                for j in range(len(response2[i]))]}]})

    with open(f"todo_all_employees.json", mode="w") as to_json:
        json.dump(t_lists, to_json)
