#!/usr/bin/python3
"""Module that queries a Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""
import requests


def count_words(subreddit, word_list):
    """Function that returns first 10 hot posts listed for given subreddit"""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 " +
               "Safari/537.36"}

    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        response = requests.get(url, headers=headers)
        hot_artls = response.json().get("data").get("children")

        titles = []
        [titles.append(_.get("data").get("title").lower()) for _ in hot_artls]

        new = []
        [new.append(_.lower()) for _ in word_list if _.lower() not in new]

        count = 0
        for title in titles:
            if new[0] in title:
                count += 1

        print(f"{new[0]}: {count}")

        if len(new):
            new.pop(0)
        else:
            return

        count_words(subreddit, new)
    except Exception:
        pass


if __name__ == "__main__":
    count_words(subreddit, word_list)
