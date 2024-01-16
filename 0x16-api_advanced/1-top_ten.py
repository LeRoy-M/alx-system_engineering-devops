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
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        for _ in range(10):
            print(response.json().get("data").get("children")[_].
                  get("data").get("title"))
    except Exception:
        print(None)


if __name__ == "__main__":
    subreddit = "programming"
    top_ten(subreddit)
