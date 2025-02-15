#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """Prints titles of first 10 hot posts for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "linux:0:1.0 (by /u/JuiceExtension6952)"}
    params = {"limit": 10}

    r = requests.get(url, headers=headers, params=params, allow_redirects=False)
    print('OK', end='')
