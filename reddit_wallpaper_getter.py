import ctypes
import praw
import requests

# This is the path to the picture you want as your desktop background
desktop_picture_location = 'put your file path to picture here'

# You must have a Reddit account registered as a bot.
# When you do you will have an id, secret, and user agent.
client_id = 'put your id here'
client_secret = 'put your secret here'
user_agent = 'put your user agent here'

# Connects you to Reddit using the Reddit API
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

reddit.read_only = True

# Searches the subReddit wallpaper and gets the top post of the week.
# If you wanted the top from the month or day just change week to month or day.
for submission in reddit.subreddit("wallpaper").top('week', limit=1):
    picture_url = submission.url

# Saves the image to your computer at desktop image location
with open(desktop_picture_location, 'wb') as handle:
    response = requests.get(picture_url, stream=True)

    if not response.ok:
        print
        response

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)

# Set image to be new background picture
ctypes.windll.user32.SystemParametersInfoW(20, 0, desktop_picture_location, 0)
