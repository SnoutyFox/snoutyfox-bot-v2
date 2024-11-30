import tweepy
import os
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

# Δημοσίευση Tweet με Εικόνα
def post_tweet():
    try:
        # Επιλέγουμε τυχαίο μήνυμα
        message = random.choice(messages)
        
        # Βρίσκουμε τυχαία εικόνα από τον φάκελο images
        image_path = os.path.join("images", random.choice(os.listdir("images")))
        
        # Μεταφόρτωση εικόνας
        media = client.media_upload(image_path)
        
        # Δημοσίευση tweet με την εικόνα
        response = client.create_tweet(text=message, media_ids=[media.media_id])
        logging.info(f"Tweet posted successfully: {response.data['id']}")
    except Exception as e:
        logging.error(f"Failed to post tweet: {e}")

# Αυτόματη Λειτουργία
def auto_tweet_and_comment():
    while True:
        logging.info("Posting tweet to profile...")
        post_tweet()
        time.sleep(3600)  # Αναμονή 1 ώρας

if __name__ == "__main__":
    auto_tweet_and_comment()
