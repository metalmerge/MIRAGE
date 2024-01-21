import tweepy
import configparser
import os
import random
from SubDownload import reddit_image_grabber
import time
from win10toast import ToastNotifier

config = configparser.ConfigParser()
config.read(r"C:\Users\ermak\OneDrive\Documents\MIRAGE\config.ini")
consumer_secret = config.get("Credentials", "consumer_secret")
consumer_key = config.get("Credentials", "consumer_key")
access_token = config.get("Credentials", "access_token")
access_token_secret = config.get("Credentials", "access_token_secret")
sender_email = config.get("Credentials", "sender_email")
password = config.get("Credentials", "password")
receiver_email = config.get("Credentials", "receiver_email")
body = "Go through the scraped meme images and then transfer the ones you like to the memeFolder."
subject = "Alert: There are less than 3 images in the memeFolder for the Twitter Bot"
# TODO: make a program to go through images and transfer them to the memeFolder
# TODO: fix email sending


def authenticate_twitter():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api


def upload_tweet_with_media(api, media_path):
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
    text = ""
    media = api.media_upload(media_path)
    media_id = media.media_id
    client.create_tweet(
        text=text,
        media_ids=[media_id],
    )


def main():
    try:
        reddit_image_grabber("week", 10)
        api = authenticate_twitter()

        meme_folder = r"C:\Users\ermak\OneDrive\Documents\MIRAGE\memeFolder"
        meme_files = [
            f
            for f in os.listdir(meme_folder)
            if f.endswith(
                (".png", ".jpg", ".jpeg", ".webp", ".PNG", ".JPG", ".JPEG", ".WEBP")
            )
        ]

        print(f"There are {len(meme_files)-1} images in the memeFolder.")

        if len(meme_files) < 3:
            print("Alert: There are less than 3 images in the memeFolder.")
            toaster = ToastNotifier()
            toaster.show_toast("ATDP", "Program Complete", duration=100)
            # import yagmail
            # try:
            #     yag = yagmail.SMTP(sender_email, password)
            #     yag.send(receiver_email, subject, body)
            # except Exception as e:
            #     print(f"An error occurred: {e}")

        media_path = os.path.join(meme_folder, random.choice(meme_files))

        upload_tweet_with_media(api, media_path)

        os.remove(media_path)
    except Exception as e:
        with open(r"C:\Users\ermak\OneDrive\Documents\MIRAGE\error.txt", "w") as file:
            file.write(str(e))


if __name__ == "__main__":
    main()
