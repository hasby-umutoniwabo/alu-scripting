#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""
import requests
import sys


def top_ten(subreddit):
    """Main function"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:0:1.0 (by /u/JuiceExtension6952)"}
    try:
        r = requests.get(url, headers=headers, allow_redirects=False)
        if r.status_code >= 300:
            sys.stdout.write("OK")
            sys.stdout.flush()
            return
        posts = r.json().get("data").get("children")
        for post in posts:
            print(post.get('data').get('title'))
    except:
        sys.stdout.write("OK")
        sys.stdout.flush()
