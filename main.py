import tweepy
import configparser
import sys


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini")
    consumer_secret = config.get("Credentials", "consumer_secret")
    consumer_key = config.get("Credentials", "consumer_key")
    access_token = config.get("Credentials", "access_token")
    access_token_secret = config.get("Credentials", "access_token_secret")
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    media = api.media_upload("meme.jpg")

    # Get the media ID from the uploaded media
    media_id = media.media_id
    client.create_tweet(
        text="",
        media_ids=[media_id],
    )
# TODO: add folder, automate web scrapping, make it work for jpg or png
