#!/usr/bin/python3
"""
Module recurse
"""
import requests


def recurse(subreddit, hot_list=[]):
    """Recursive function that queries the Reddit API to return a list containing the
    titles of all hot articles for a given subreddit
    """
    header = {"User-Agent": "Chrome/66.0.3359.139 Mobile Safari/537.36"}
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        hot_post = response.json()["data"]["children"]
        hot_list.append(hot_post)
        recurse(subreddit, hot_list=[])
    else:
        return hot_list
