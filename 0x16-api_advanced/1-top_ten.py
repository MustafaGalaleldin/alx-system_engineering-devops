#!/usr/bin/python3
"""
a function that queries the Reddit API and  prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    "print the 10 titles"
    url = f"https://api.reddit.com/r/{subreddit}/hot"
    headers = {"User-Agent": "python:subreddit.subscriber.counter:v1.0"}
    try:
        count = 0
        response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            result = response.json()
            for dic in result["data"]["children"]:
                if count < 10:
                    print(dic["data"].get("title"))
                    count += 1
                else:
                    break
    except Exception:
        print(None)
