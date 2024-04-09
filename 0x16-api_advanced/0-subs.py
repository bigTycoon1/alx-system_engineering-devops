#!/usr/bin/python3
'''
contains the function numbers_of_subscriber
'''
import requests


def number_of_subscribers(subreddit):
    """ return the num of sub """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code != 200:
        return 0
    dic = resp.json()
    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0
    return resp.json()['data']['subscribers']
