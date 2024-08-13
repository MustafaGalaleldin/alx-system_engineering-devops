#!/usr/bin/python3
"a function that queries the Reddit API and returns the number of subscribers"
import requests


def number_of_subscribers(subreddit):
    "returns the number of subscribers or 0 if invalid"
    subscribers = 0
    url = f"https://api.reddit.com/r/{subreddit}/about"
    headers = {"User-Agent": "python:subreddit.subscriber.counter:v1.0"}
    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        result = response.json()
        for k, v in result["data"].items():
            if k == "subscribers":
                subscribers = v
                break
    except Exception:
        pass
    return subscribers
