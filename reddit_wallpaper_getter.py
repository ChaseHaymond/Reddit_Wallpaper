import praw

reddit = praw.Reddit(client_id="",
                     client_secret="",
                     password="",
                     user_agent="",
                     username="")

print(reddit.user.me())

reddit.read_only = True

print(reddit.user.me())
