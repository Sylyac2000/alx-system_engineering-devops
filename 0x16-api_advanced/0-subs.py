#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given, the function should
return 0."""

import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number
        of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "Sylyac2000@alx-africa"
    }
    results = requests.get(url, headers=headers).json()
    nbre_subscribers = results.get('data', {}).get('subscribers')
    if not nbre_subscribers:
        return 0
    return nbre_subscribers
