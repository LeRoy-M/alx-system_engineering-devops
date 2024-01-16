0x16. API advanced
------------------

**0. How many subs?** `[0-subs.py]` >> Python script with a function that queries a [Reddit API](https://www.reddit.com/dev/api/) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. The function returns `0` if an invalid subreddit is given.

**1. Top Ten** `[1-top_ten.py]` >> Python script with a function that queries a [Reddit API](https://www.reddit.com/dev/api/) and prints the titles of the first 10 hot posts listed for a given subreddit.

**2. Recurse it!** `[2-recurse.py]` >> Python script with a recursive function that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns a list containing the titles of all hot articles for a given subreddit. The function returns `None` if no results are found for a given subreddit.

**3. Count it** `[100-count.py]` >> Python script with a recursive function that queries the [Reddit API](https://www.reddit.com/dev/api/), parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive and delimited by spaces, where `Javascript` should count as `javascript`, but `java` should not).
