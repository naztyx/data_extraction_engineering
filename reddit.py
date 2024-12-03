import praw
import json
import time

reddit = praw.Reddit(
    client_id="cfjmESR9b0GbnudSODviTw",
    client_secret="_ODs3OYZRh-YGD6RV-ceFdZiZCHqdQ",
    user_agent="windows:bitcoin.sentiment.fetcher:v1.0 (by /u/qraxex)"
)

# Subreddit and query
subreddit = reddit.subreddit("Bitcoin")
query = "Bitcoin"

def fetch_and_send_posts():
    try:
        posts = subreddit.search(query, limit=10)
        for post in posts:
            data = {
                "id": post.id,
                "title": post.title,
                "selftext": post.selftext,
                "score": post.score,
                "created_utc": post.created_utc,
                "url": post.url
            }
            # producer.send("reddit_bitcoin", data)
            # print(f"Sent post {post.id} to Kafka topic 'reddit_bitcoin'.")

            # Respect API rate limits
            remaining = reddit.auth.limits.get("remaining", 60)
            reset_time = reddit.auth.limits.get("reset", 60)
            if remaining <= 1:
                print(f"Rate limit hit. Sleeping for {reset_time + 1} seconds.")
                time.sleep(reset_time + 1)

    except Exception as e:
        print(f"Error: {e}")

# Run the function
fetch_and_send_posts()
