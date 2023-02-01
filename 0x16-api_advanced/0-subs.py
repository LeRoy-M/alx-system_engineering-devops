#!/usr/bin/python3
"""
Module 0-subs
"""
import requests

def number_of_subscribers(subreddit):
    """Function that returns number of subscribers via Reddit API"""
    header = {"User-Agent": "Chrome/66.0.3359.139 Mobile Safari/537.36"}
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    response = requests.get(url, headers=header)
    
    if response.status_code == 200:
        subs = response.json()["data"]["subscribers"]
    else:
        subs = 0

    return subs
