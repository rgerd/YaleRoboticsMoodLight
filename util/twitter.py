import sys
import json

# Returns a an array of the combined posts by the users in the request (`dict`),
# which are each filtered by the keywords in `dict`
# i.e.
# request = {
#   'nachos': ['realDonaldTrump'],
#   'burritos': ['HillaryClinton', 'BarackObama'],
#   'enchaladas': ['HillaryClinton'],
#   'cows': [],
#   '*': ['HillaryClinton', 'realDonaldTrump']
# }
# getTwitterData(request) returns:
# all tweets by donald trump that contain the word 'nachos'
# + all tweets by barack obama containing the word 'burritos'
# + all tweets by hillary clinton containing the word 'burritos'
# + all tweets by hillary clinton containing the word 'enchaladas'
# + all tweets by all users containing the word 'cows'
# + all tweets by hillary clinton
# + all tweets by donald trump

def getTwitterData(request):
	all_tweets = []
	for keyword, users in request.items():
		if not users:
			all_tweets.extend(getPostsByAll(keyword))
		else:
			for user in users:
				all_tweets.extend(getPostsByUser(user, keyword))
	return all_tweets


###############################################################################

# Returns an array of strings, each string being a public post by the user with
# the username `twitter_handle` containing the word `keyword`
# Example:
#   getPostsByUser("HillaryClinton", "-Hillary")
def getPostsByUser(twitter_handle, keyword):
    from config.twitterconfig import twitter_api
    timeline = twitter_api.GetUserTimeline(screen_name=twitter_handle, count=sys.maxsize)
    tweets = [s.text for s in timeline]
    #if keyword is a wild card, just treturn tweets, don't filter by keyword
    if keyword == '*':
    	return tweets
    else:
    	return filterTweetsByKeyword(tweets, keyword)

# Removes all tweets not containing a given `keyword`, returning an array
def filterTweetsByKeyword(tweets, keyword):
    return list(filter(lambda tweet: keyword in tweet, tweets))

# Returns an array of tweets (strings) from all users, each containing the
# `keyword` specified
def getPostsByAll(keyword):
    from config.twitterconfig import twitter_api
    return twitter_api.GetSearch(keyword, count=sys.maxsize, lang="en")
