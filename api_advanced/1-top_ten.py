#!/usr/bin/python3
"""API"""
import requests


def top_ten(subreddit):
    """API"""
    reddit_url = "https://www.reddit.com/r/{}/hot.json" \
        .format(subreddit)
    headers = {"User-Agent": "linux:0:1.0 (by /u/JuiceExtension6952)"}
    response = requests.get(reddit_url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']
        for post in data['children'][:10]:
            print(post['data']['title'])
    else:
        print(None)
