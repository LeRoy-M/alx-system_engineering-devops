#!/usr/bin/python3
"""Module that uses a REST API for a given employee ID and then
returns information about their TODO list progress
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url1 = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    url2 = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    response1 = json.loads(requests.get(url1).text)
    response2 = json.loads(requests.get(url2).text)
    tasks = response2.__len__()
    tc_list = [i for i in range(tasks) if response2[i]["completed"]]

    print("Employee {} is done with tasks({}/{}):".format(
        response1.get("name"), len(tc_list), tasks))
    for i in range(len(tc_list)):
        print(f"\t {response2[tc_list[i]]['title']}")
