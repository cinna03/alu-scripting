#!/usr/bin/python3
"""
Get top 10 hot posts function
"""

import json
import requests
import sys


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    result = requests.get(url, headers=headers, allow_redirects=False)
    if result.status_code != 200:
        print("NO")  # Changed output to "NO" for errors
    else:
        data = json.loads(result.text)["data"]["children"]
        for post in data[:10]:
            print(post["data"]["title"])
        print("OK")  # Print "OK" after successful retrieval


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("NO")  # Print "NO" if subreddit name is not provided
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)

