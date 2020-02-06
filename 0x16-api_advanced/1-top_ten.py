#!/usr/bin/python3
"""Task 1"""
from requests import get


def top_ten(subreddit):
    """GET to Reddit api for the top 10
    posts of a subreddit"""
    info = get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "Doom-Agent"},
        allow_redirects=False)

    info_json = info.json()
    data = info_json.get("data")
    if data:
        for post in data.get("children"):
            print(post.get("data").get("title"))
    else:
        print("None")
