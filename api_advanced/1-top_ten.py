#!/usr/bin/python3
"""Module that queries the Reddit API and prints the titles
of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit: subreddit to search

    Returns:
        None
    """
    # Set up the headers with a custom User-Agent
    headers = {
        'User-Agent': 'linux:0:1.0 (by /u/JuiceExtension6952)'
    }

    # Construct the URL for the subreddit's hot posts
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful and the subreddit exists
    if response.status_code == 200:
        # Parse the JSON response
        posts = response.json().get('data', {}).get('children', [])
        
        # Print the titles of the first 10 hot posts
        for post in posts:
            print(post.get('data', {}).get('title'))
    else:
        # If subreddit is invalid or not found, print None
        print(None)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
