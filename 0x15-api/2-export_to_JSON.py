#!/usr/bin/python3
"""Module that uses a REST API for a given employee ID to export
data into a JSON file
"""
import json
import requests
import sys


def export_to_json(sys.argv):
    url1 = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    url2 = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos"
    response1 = json.loads(requests.get(url1).text)
    response2 = json.loads(requests.get(url2).text)
    tasks = response2.__len__()
    tc_list = [i for i in range(tasks) if response2[i]["completed"]]

    print("Employee {} is done with tasks({}/{}):".format(
        response1.get("name"), len(tc_list), tasks))
    for i in range(len(tc_list)):
        print(f"\t {response2[tc_list[i]]['title']}")

    t_lists = {
        f"{response1.get('id')}": [{
            "task": f"{response2[i].get('title')}",
            "completed": f"{response2[i].get('completed')}",
            "username": f"{response1.get('username')}"}
            for i in range(tasks)]}

    with open(f"{sys.argv[1]}.json", mode="w") as to_json:
        json.dump(t_lists, to_json)


if __name__ == "__main__":
    export_to_json(sys.argv)
