import tweepy
import schedule
import time
from datetime import datetime, timedelta
import pytz
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Twitter API credentials from environment variables
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Set up Twitter authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def send_weekly_tweet():
    tweet = "What did you get done this week?"
    try:
        api.update_status(tweet)
        print(f"Tweet sent: {tweet}")
    except Exception as e:
        print(f"Failed to send tweet: {e}")

# Define the schedule
def schedule_post():
    cet = pytz.timezone('CET')
    target_time = cet.localize(datetime.now().replace(hour=16, minute=0, second=0, microsecond=0))

    # Schedule task for every Friday at 4 PM CET
    schedule.every().friday.at(target_time.strftime('%H:%M')).do(send_weekly_tweet)

    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait a minute between checks

# Run the scheduling function
if __name__ == "__main__":
    print("Scheduling weekly tweet every Friday at 4 PM CET.")
    schedule_post()
