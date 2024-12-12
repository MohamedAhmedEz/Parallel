import datetime
import json
import re

from Data.Post import Post
from parsers.IFetch import SocialMediaFileFetcher


class redditFetcher(SocialMediaFileFetcher):
    def Parse(self):
        with open('reddit.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for post in data["data"]["children"]:
                info = post["data"]
                username = info["author"]
                text = info["selftext"]
                Utc_date = info["created_utc"]
                date = datetime.datetime.utcfromtimestamp(Utc_date)

                self.shared_list.add(Post(
                    platform="reddit",
                    author=username,
                    post=text,
                    date=date
                ))









