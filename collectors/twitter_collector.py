import tweepy, os
from dotenv import load_dotenv
load_dotenv()
TWITTER_KEY = os.getenv("TWITTER_KEY")
TWITTER_SECRET = os.getenv("TWITTER_SECRET")
def fetch_twitter(query="OSINT", count=20):
    auth = tweepy.AppAuthHandler(TWITTER_KEY, TWITTER_SECRET)
    api = tweepy.API(auth)
    tweets = api.search_tweets(q=query, count=count, lang="en")
    results = []
    for t in tweets:
        results.append({
            "platform": "twitter",
            "user": t.user.screen_name,
            "timestamp": str(t.created_at),
            "text": t.text,
            "url": f"https://twitter.com/{t.user.screen_name}/status/{t.id}"
        })
    return results