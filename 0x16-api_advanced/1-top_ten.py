#!/usr/bin/python3
"""
Module 1-top_ten
"""
import requests


def top_ten(subreddit):
    """Function that queries the Reddit API and prints the top 10 titles of the
    hottest posts listed for a given subreddit
    """
    header = {"User-Agent": "Chrome/66.0.3359.139 Mobile Safari/537.36"}
    url = "https://api.reddit.com/r/{}/top".format(subreddit)
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        count = 10
        hot_ten = response.json()["data"]["children"]

        for hot in hot_ten:
            if count == 0:
                break
            print(hot["data"]["title"])
            count -= 1
    else:
        print("None")
