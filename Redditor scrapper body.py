import praw
from redditor_scrapper import awards_iterator
from redditor_scrapper import comments_iterator
from redditor_scrapper import submission_iterator
from redditor_scrapper import save_to_json


# Data for reddit API
reddit = praw.Reddit(
    user_agent="praw_scrapper",
    client_id= input("Enter Client_id: "),
    client_secret=input("Enter Client_secret: "),
    username=input("Enter Username: "),
    )
# Number of news
limit = 30

# Tech data
n = 1
DATA = []


subreddit = reddit.subreddit('news').hot(limit=limit)

for submission in subreddit:
    awards = awards_iterator(submission)
    comments = comments_iterator(submission)
    DATA = submission_iterator(submission, DATA, awards, comments)
    print('News # ' + str(n) + ' of '+ str(limit)+ ' saved')
    n += 1

save_to_json(DATA)