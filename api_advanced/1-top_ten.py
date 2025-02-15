#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """Return titles of first 10 hot posts if subreddit is valid.
    Print None if subreddit is invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'linux:0.1:1.0 (by /u/aaaaaaa)'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        try:
            children = response.json().get('data', {}).get('children', [])
            for i in range(10):
                print(children[i].get('data', {}).get('title', ''))
        except Exception:
            print(None)
    else:
        print(None)
