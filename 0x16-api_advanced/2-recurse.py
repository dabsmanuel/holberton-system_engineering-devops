#!/usr/bin/python3
"""Task 2"""
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """GET to Reddit api for every hot post
    in a subreddit"""
    info = get(
        "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit),
        headers={"User-Agent": "Doom-Agent"},
        params={"after": after})

    data = info.json().get("data")
    if data:
        for post in data.get("children"):
            hot_list.append(post.get("title"))
        return recurse(subreddit, hot_list, data.get("after"))
    else:
        return None
