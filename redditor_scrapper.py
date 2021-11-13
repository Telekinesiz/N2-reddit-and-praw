from praw.models import MoreComments
import json

# Geting info about rewards, name and discription can be usefull for human, but for ML model i would left only id price, and count
def awards_iterator(submission):
    awards = []

    for award in submission.all_awardings:
        name = award["name"]
        id = award["id"]
        description = award["description"]
        coin_price = award["coin_price"]
        count = award["count"]

        awards.append(
            {"name": name,
             "id": id,
             "description": description,
             "coin_price": coin_price,
             "count": count}
        )
    return awards

#Receiveing info about comments. Sticked and Distinguished comments can receive additional vote because more people will be able to see it, so this parameters should be count
def comments_iterator(submission):
    comments = []
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue

        comments.append(
            {'Comment': top_level_comment.body,
             'Is_submitter': top_level_comment.is_submitter,
             'Score': top_level_comment.score,
             'Sticked': top_level_comment.stickied,
             'Distinguished': top_level_comment.distinguished}
        )
    return comments

def submission_iterator(submission, DATA, awards, comments):


    DATA.append(
        {'ID': submission.id,
         'Date': submission.created_utc,
         'Name': submission.title,
         'Text': submission.selftext,
         'Score': submission.score,
         'Ratio': submission.upvote_ratio,
         'Comments_num': submission.num_comments,
         'Page_url': str('https://www.reddit.com') + submission.permalink,
         'Awards': awards,
         'Comments': comments}
            )
    return DATA

def save_to_json(DATA):
    with open('Reddit.json', "w", encoding='utf-8') as file:
        json.dump(DATA, file, indent=4, ensure_ascii=False)
        print("Done")

