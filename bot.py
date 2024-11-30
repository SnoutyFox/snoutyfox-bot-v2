import tweepy
import time
import random
import logging

# Ρύθμιση Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Twitter API Keys
API_KEY = "5XiFSdUFY8nBkEpCBp3nB6oGg"
API_SECRET_KEY = "1IUm7XsrKnT8vYCwdpptKXC2UcVMqHsGmkis6ELU0rpIJsvFRp"
ACCESS_TOKEN = "1861412709457100800-sXzNRfY8h8AXa7tU7l0bJnABH3Q3ZH"
ACCESS_TOKEN_SECRET = "Kt5S2jz1nB505IKLexl6H8OLx0N8zefyV2v9DC15361sR"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAABPbxAEAAAAAnK5h6jaKgzhdeudY4ZqsbZmeq7E%3Dd7Qyiyy1tbX9InKQDRfXqjtFlW4fuA29pHYG5jD1J7Egr18Y46"

# Αυθεντικοποίηση στο API V2
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Λίστα μηνυμάτων
messages = [
    "🚀 SnoutyFox: Sniffing the future of meme coins! Join our Telegram: https://t.me/snoutyfoxcoin 💬",
    "💡 Crypto enthusiasts, discover SnoutyFox! Sniff out the next big thing!",
    "🔥 Meme coins just got smarter! SnoutyFox is sniffing its way to the top!",
    "🐾 SnoutyFox is here to lead the pack! Don't miss out: 3HDJV1TVtQJSuH9z1ytKKYqxLHcqgCA59XrWoEEGDEQb",
    "🌟 The future of meme coins smells great! Join the SnoutyFox revolution: https://t.me/snoutyfoxcoin",
    "🔮 Sniff the future with SnoutyFox! Your chance to join the meme coin movement is here: https://t.me/snoutyfoxcoin",
]

# Δημοσίευση Tweet
def post_tweet():
    message = random.choice(messages)
    try:
        response = client.create_tweet(text=message)
        logging.info(f"Tweet posted successfully: {response.data['id']}")
    except tweepy.TweepyException as e:
        logging.error(f"Failed to post tweet: {e}")

# Σχόλιο σε Tweets
def comment_on_tweets():
    keywords = ["crypto", "memes", "meme coin", "cryptocurrency"]
    for keyword in keywords:
        try:
            response = client.search_recent_tweets(query=keyword, max_results=5)
            if response.data:
                for tweet in response.data:
                    try:
                        reply_message = f"🔥 SnoutyFox is the ultimate meme coin! Check it out: https://t.me/snoutyfoxcoin"
                        client.create_tweet(
                            text=reply_message,
                            in_reply_to_tweet_id=tweet.id
                        )
                        logging.info(f"Commented on tweet ID: {tweet.id}")
                    except tweepy.TweepyException as e:
                        logging.error(f"Failed to comment on tweet ID {tweet.id}: {e}")
        except tweepy.TweepyException as e:
            logging.error(f"Error searching tweets for keyword '{keyword}': {e}")

# Αυτόματη Λειτουργία
def auto_tweet_and_comment():
    while True:
        # Δημοσίευση στο προφίλ
        logging.info("Posting tweet to profile...")
        post_tweet()
        time.sleep(3600)  # Αναμονή 1 ώρας

        # Σχόλιο σε tweets άλλων
        logging.info("Commenting on tweets...")
        comment_on_tweets()
        time.sleep(3600)  # Αναμονή 1 ώρας

if __name__ == "__main__":
    auto_tweet_and_comment()
