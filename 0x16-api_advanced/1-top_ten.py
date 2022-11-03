#!/usr/bin/python3
"""a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """queries the Reddit API and returns the number
        of subscribers """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "Sylyac2000@alx-africa"
    }
    params = {
        "limit": 10
    }
    results = requests.get(url, headers=headers, params=params,
                           allow_redirects=False).json()
    top_ten = results.get('data', {}).get('children', [])
    if not top_ten:
        print(None)
    for t in top_ten:
        print(t.get('data').get('title'))
