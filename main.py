import tweepy
import configparser
import os

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
    meme_folder = "memeFolder"
    meme_files = os.listdir(meme_folder)
    media_path = os.path.join(meme_folder, meme_files[0])
    tweet_text = ""
    media = api.media_upload(media_path)
    text = ""
    # Get the media ID from the uploaded media
    media_id = media.media_id
    client.create_tweet(
        text=text,
        media_ids=[media_id],
    )
    os.remove(media_path)
# TODO: automate web scrapping,
