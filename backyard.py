import json
import re
i = 1
# Open the file and load the data into a Python dictionary
with open('twitter.json', 'r' , encoding='utf-8') as file:
    data = json.load(file)
    for post in data["data"]:
        tweet_text = post['text']
        match = re.match(r'@(\w+)', tweet_text)
        if match:
            first_mentioned_username = match.group(1)
            postl = tweet_text[len(match.group(0)):]
        else:
            first_mentioned_username = "No mention at the start"
            postl = tweet_text
        print(i,"  ",first_mentioned_username,"\n",postl)
        i+=1

# Print the data
print(data)
