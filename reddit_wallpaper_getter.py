import ctypes

import praw
import requests

with open('./private_info/id.txt', 'r') as file:
    client_id = file.read().replace('\n', '')

with open('./private_info/secret.txt', 'r') as file:
    client_secret = file.read().replace('\n', '')

with open('./private_info/user_agent.txt', 'r') as file:
    user_agent = file.read().replace('\n', '')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

reddit.read_only = True

for submission in reddit.subreddit("wallpaper").top('week', limit=1):
    picture_url = submission.url

with open('./images/reddit_picture.jpg', 'wb') as handle:
    response = requests.get(picture_url, stream=True)

    if not response.ok:
        print
        response

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)


ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/cdhay/Desktop/this/Reddit_Wallpaper/images/reddit_picture.jpg", 0)
