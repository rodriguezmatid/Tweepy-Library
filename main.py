import tweepy
import dotenv as _dotenv
import os as _os

_dotenv.load_dotenv()

# Authenticate to Twitter
# auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
# auth.set_access_token(config.access_token, config.access_secret)

TW_API_KEY = _os.environ["TWITTER_API_KEY"]
TW_API_SECRET = _os.environ["TWITTER_SECRET_KEY"]
TW_ACCESS_TOKEN = _os.environ["TWITTER_ACCESS_TOKEN"]
TW_ACCESS_SECRET = _os.environ["TWITTER_ACCESS_SECRET"]

auth = tweepy.OAuthHandler(TW_API_KEY, TW_API_SECRET)
auth.set_access_token(TW_ACCESS_TOKEN, TW_ACCESS_SECRET)

# client = tweepy.Client(consumer_key = TW_API_KEY, consumer_secret = TW_API_SECRET, access_token = TW_ACCESS_TOKEN, access_token_secret = TW_ACCESS_SECRET)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

########## Reading Tweets ##########
# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")

########## Twittear ##########
#api.update_status("Hamilton")

########## Information ##########
# user = api.get_user(screen_name='datactuary')
# print("User details:")
# print(user.name)
# print(user.description)
# print(user.location)
# print('')

########## Update profile description ##########
# api.update_profile(description="Actuary | Data | Analytics. Never bet against Bitcoin & Ethereum 🤖")

#print("Last 20 Followers:")
#for follower in user.followers():
#    print(follower.name)

########## Follows Someone ##########
#api.create_friendship(screen_name="realpython")

########## Tweets Liker ##########
# timeline = api.home_timeline(count=1)
# tweet = timeline[0]
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")
# print(f"Liking tweet of {tweet.user.name}")
# api.create_favorite(tweet.id)

########## Tweets Searcher ##########
matches = ["integration"]
for tweet in api.search_tweets(q="(metamask) -filter:replies", lang="en", count=15, result_type = "recent"):
    print("############# Data of the tweet #####################")
    print("User: " f"{tweet.user.screen_name}")
    print("Name: " f"{tweet.user.name}")
    print("ID: " f"{tweet.id}")
    print("Date: " f"{tweet.created_at}")
    print("Tweet: " f"{tweet.text}")
    print("")


api.update_status(status = 'Testeando', in_reply_to_status_id = 1562136539831930880 , auto_populate_reply_metadata=True)

########## Trends ##########
# trends_result = api.get_place_trends(1) #1 means World-wide
# for trend in trends_result[0]["trends"]:
#    print(trend["name"])

########## Blocked list ##########
# for block in api.get_blocks():
#     print(block.name)

########## Muted list ##########
# for muted in api.get_mutes():
#     print(muted.name)

####### Workflow #######
# Devolvemos último tweet
# Ese último tweet --> Tomamos su ID
# IF ID anterior == ID actual  --> No contestamos, else: contestamos.
# Esperamos 30 segundos y vuelve a correr el bot