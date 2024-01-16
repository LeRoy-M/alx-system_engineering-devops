#!/usr/bin/python3
"""Module that queries a Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[]):
    """Function that returns first 10 hot posts listed for given subreddit"""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 " +
               "Safari/537.36"}
    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        response = requests.get(url, headers=headers)
        hot_titles = response.json().get("data").get("children")

        return hot_titles
    except Exception:
        return None


if __name__ == "__main__":
    top_ten(subreddit)
