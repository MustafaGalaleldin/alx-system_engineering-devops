#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    "the function workflow"
    url = f"https://api.reddit.com/r/{subreddit}/hot"
    params = {"limit": 100, "after": after}
    headers = {"User-Agent": "My-User-Agent"}
    try:
        response = requests.get(url, params=params,
                                headers=headers,
                                allow_redirects=False)
        if response.status_code != 200:
            return None
        dic = response.json().get("data")
        posts = dic.get("children")
        after = dic.get("after")
        if not posts:
            return hot_list if hot_list else None
        hot_list.extend([post["data"]["title"] for post in posts])
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except Exception:
        return None
