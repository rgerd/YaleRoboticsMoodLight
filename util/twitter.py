import json
import sys
from config.twitterconfig import twitter_api

# Returns a an array of the combined posts by the users in the request (`dict`),
# which are each filtered by the keywords in `dict`
# i.e.
# dict = {
#   'nachos': ['theRealDonald'],
#   'burritos': ['HillaryClinton', 'BarackObama'],
#   'enchaladas': ['HillaryClinton'],
#   'cows': []
# }
# getTwitterData(dict) returns:
# all tweets by donald trump that contain the word 'nachos'
# + all tweets by barack obama containing the word 'burritos'
# + all tweets by hillary clinton containing the word 'burritos'
# + all tweets by hillary clinton containing the word 'enchaladas'
# + all tweets by all users containing the word 'cows'
def getTwitterData(dict):
    # YOUR CODE HERE
    return [ ]


###############################################################################

# Returns an array of strings, each string being a public post by the user with
# the username `twitter_handle` containing the word `keyword`
# Example:
#   getPostsByUser("HillaryClinton", "-Hillary")
def getPostsByUser(twitter_handle, keyword):
    timeline = twitter_api.GetUserTimeline(screen_name=twitter_handle, count=sys.maxsize)
    tweets = [s.text for s in timeline]
    return filterTweetsByKeyword(tweets, keyword)

# Removes all tweets not containing a given `keyword`, returning an array
def filterTweetsByKeyword(tweets, keyword):
    return list(filter(lambda tweet: keyword in tweet, tweets))

# Returns an array of tweets (strings) from all users, each containing the
# `keyword` specified
def getPostsByAll(keyword):
    return twitter_api.GetSearch(keyword, count=sys.maxsize, lang="en")
