#!/usr/bin/python3
"""
a function that queries the Reddit API and  prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    "print the 10 titles"
    url = f"https://api.reddit.com/r/{subreddit}/hot"
    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            result = response.json()
            for dic in result["data"]["children"]:
                print(dic["data"].get("title"))
    except Exception:
        print(None)
