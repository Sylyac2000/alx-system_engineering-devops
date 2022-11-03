#!/usr/bin/python3
""" a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles"""

import requests


def recurse(subreddit, hot_list=[], apres="", count=0):
    """queries the Reddit API and returns a list containing """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "Sylyac2000@alx-africa"
    }
    params = {
        "after": apres,
        "count": count,
        "limit": 100
    }
    results = requests.get(url, headers=headers, params=params,
                           allow_redirects=False)
    if results.status_code == 404:
        return None

    results = results.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
