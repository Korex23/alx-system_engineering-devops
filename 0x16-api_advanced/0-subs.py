#!/usr/bin/python3
"""Defines a number_of_subscribers function."""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users) for a given subreddit.
    
    If an invalid subreddit is given, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyBot/1.0 (by Cipher10X)"}
    
    try:
        # Query Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        
        # If status code is 200 (success), extract number of subscribers
        if response.status_code == 200:
            data = response.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers
        
        # If subreddit is not found (e.g., invalid subreddit), return 0
        elif response.status_code == 404:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    
    # In all other cases, return 0
    return 0
