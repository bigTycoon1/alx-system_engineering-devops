#!/usr/bin/python3
""" function that queries the Reddit API """
import requests
import sys


def top_ten(subreddit):
    """ queries to Reddit_API """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    params = {
        "limit": 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    dic = response.json()
    hot_posts = dic['data']['children']
    if len(hot_posts) is 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
