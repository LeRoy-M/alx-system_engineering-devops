#!/usr/bin/python3
"""Module that queries a Reddit API and prints the title of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Function that returns first 10 hot posts listed for given subreddit"""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 " +
               "Safari/537.36"}
    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9"
        response = requests.get(url, headers=headers)
        top_titles = response.json().get("data").get("children")

        [print(_.get("data").get("title")) for _ in top_titles]
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(subreddit)
