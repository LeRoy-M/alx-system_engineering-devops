#!/usr/bin/python3
"""Module that queries a Reddit API and returns the number of
subscribers for a given subreddit.
"""
import json
import requests


def number_of_subscribers(subreddit):
    """Function that returns number of subcribers of given subreddit"""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 " +
               "Safari/537.36"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        return response.json().get("data").get("subscribers")
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(subreddit)
