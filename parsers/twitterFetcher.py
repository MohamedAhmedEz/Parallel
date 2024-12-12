import json
import re

from Data.Post import Post
from parsers.IFetch import SocialMediaFileFetcher


class twitterFetcher (SocialMediaFileFetcher):
    def Parse(self):
        with open('twitter.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for post in data["data"]:
                tweet_load = post['text']
                match = re.match(r'@(\w+)', tweet_load)
                if match:
                    username = match.group(1)
                    postdata = tweet_load[len(match.group(0)):]
                else:
                    username = "No mention at the start"
                    postdata = tweet_load
                self.shared_list.add(Post(
                    platform = "Twitter",
                    author = username,
                    post = postdata,
                    date = None
                ))

