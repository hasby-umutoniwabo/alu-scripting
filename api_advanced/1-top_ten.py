#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for a given subreddit.
    
    Args:
        subreddit: Name of the subreddit to query
    """
    # Use proper URL and add /hot.json to get hot posts
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Custom User-Agent to avoid potential Reddit API restrictions
    headers = {
        'User-Agent': 'linux:0.1:1.0 (by /u/aaaaaaa)',
        # Don't follow redirects as specified in requirements
        'Allow-Redirects': 'False'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if response is successful and not a redirect
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            
            # Print first 10 post titles
            for i in range(min(10, len(posts))):
                title = posts[i].get('data', {}).get('title', '')
                print(title)
        else:
            print(None)
            
    except Exception:
        print(None)
