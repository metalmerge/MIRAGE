import tweepy
import configparser
import sys
import os


def api():
    config = configparser.ConfigParser()
    config.read("config.ini")
    try:
        TWITTER_ACCESS_TOKEN = config.get("Credentials", "TWITTER_ACCESS_TOKEN")
        # API_key = config.get("Credentials", "API_key")
        # API_Key_Secret = config.get("Credentials", "API_Key_Secret")
        TWITTER_ACCESS_TOKEN_SECRET = config.get(
            "Credentials", "TWITTER_ACCESS_TOKEN_SECRET"
        )
        # BEARER_TOKEN = config.get("Credentials", "BEARER_TOKEN")
        TWITTER_CONSUMER_KEY = config.get("Credentials", "API_key")
        TWITTER_CONSUMER_SECRET = config.get("Credentials", "API_Key_Secret")
    except configparser.Error:
        print(configparser.Error)
        sys.exit(1)
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    print("Authenticated")
    return tweepy.API(auth)


def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(filename=image_path, status=message)
    else:
        api.update_status(status=message)
    print(f"Tweeted: {message}")


if __name__ == "__main__":
    api = api()
    tweet(api, "Finally got ahold of a Windows computer", "meme.png")
