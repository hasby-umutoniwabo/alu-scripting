#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """Prints titles of first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0:1.0 (by /u/JuiceExtension6952)"}
    params = {"limit": 10}

    r = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    if r.status_code == 404:
        print("None")
        return

    if r.status_code == 200:
        try:
            data = r.json().get("data", {}).get("children", [])
            for post in data:
                title = post.get("data", {}).get("title")
                print(title)
        except Exception:
            print("None")
            return
    else:
        print("None")
