#!/usr/bin/python3
"""Task 0"""
from requests import get


def number_of_subscribers(subreddit):
    """GET to Reddit api for the number of
    suscribbers in a subbredit"""
    info = get(
               "https://www.reddit.com/r/{}/about.json".format(subreddit),
               headers={"User-Agent": "Doom-Agent"},
               allow_redirects=False)

    info_json = info.json()
    data = info_json.get("data")
    if data:
        return data.get("subscribers")
    else:
        return 0
