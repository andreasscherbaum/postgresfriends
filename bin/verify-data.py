#!/usr/bin/env python3

import sys
import json
from urllib.parse import urlparse


# read all of STDIN
# input should already be sorted
input_text = sys.stdin.read()

#print(input_text)

# load JSON (will fail if the input is not valid JSON)
input_json = json.loads(input_text)

#print (input_json)
#print(json.dumps(input_json, indent=4))


def validate_url(url: str, socialname: str) -> bool:
    print(url)
    try:
        res = urlparse(url)
    except:
        print("Invalid URL: {url}".format(url = url))
        sys.exit(1)

    print(res)
    if (socialname in ['Twitter', 'Mastodon', 'Mastodon', 'LinkedIn', 'Polywork']):
        if (res.scheme != 'https'):
            print("URL schema must be https! (URL: {url})".format(url = url))
            sys.exit(1)

    if (socialname == 'Twitter'):
        if (res.netloc != 'twitter.com' and res.netloc != 'www.twitter.com'):
            print("Twitter URL is invalid! (URL: {url})".format(url = url))
            sys.exit(1)

    if (socialname == 'LinkedIn'):
        if (res.netloc != 'linkedin.com' and res.netloc != 'www.linkedin.com'):
            print("LinkedIn URL is invalid! (URL: {url})".format(url = url))
            sys.exit(1)

    if (socialname == 'Polywork'):
        if (res.netloc != 'polywork.com' and res.netloc != 'www.polywork.com'):
            print("Polywork URL is invalid! (URL: {url})".format(url = url))
            sys.exit(1)

    if (socialname in ['Twitter', 'Mastodon', 'LinkedIn', 'Polywork']):
        if (len(res.path) < 2):
            print("Path for {sn} is invalid! (URL: {url})".format(sn = socialname, url = url))
            sys.exit(1)
        if (socialname == 'Mastodon' and res.path[:2] != '/@'):
            print("Path for {sn} is invalid! (URL: {url})".format(sn = socialname, url = url))
            sys.exit(1)
        if (socialname == 'Twitter' and res.path.find('@') != -1):
            print("Path for {sn} is invalid! (URL: {url})".format(sn = socialname, url = url))
            sys.exit(1)

    return True



for username, userdata in input_json.items():
    if (username.find('"') != -1):
        print("No double quotes in name allowed")
        sys.exit(1)

    for socialname, socialdata in userdata.items():
        if (socialname.lower().find('twitter') != -1 and socialname != 'Twitter'):
            print("Invalid social media name: {n}, should be 'Twitter'".format(n = socialname))
            sys.exit(1)
        if (socialname.lower().find('mastodon') != -1 and socialname != 'Mastodon'):
            print("Invalid social media name: {n}, should be 'Mastodon'".format(n = socialname))
            sys.exit(1)
        if (socialname.lower().find('mastadon') != -1):
            print("Invalid social media name: {n}, should be 'Mastodon'".format(n = socialname))
            sys.exit(1)
        if (socialname.lower().find('blog') != -1 and socialname != 'Blog'):
            print("Invalid social media name: {n}, should be 'Blog'".format(n = socialname))
            sys.exit(1)
        if (socialname.lower().find('linkedin') != -1 and socialname != 'LinkedIn'):
            print("Invalid social media name: {n}, should be 'LinkedIn'".format(n = socialname))
            sys.exit(1)
        if (socialname.lower().find('polywork') != -1 and socialname != 'Polywork'):
            print("Invalid social media name: {n}, should be 'Polywork'".format(n = socialname))
            sys.exit(1)
        if (socialname in ['Twitter', 'Mastodon', 'Blog', 'LinkedIn', 'Polywork', 'Website']):
            for url in socialdata:
                validate_url(url, socialname)
