import json
from urllib.request import urlopen, Request
from urllib.parse import urlencode

# Returns a tuple, (emotion, magnitude), that represents the
# overall emotion calculated from an array of tweets, provided
# by getTwitterData in util/twitter.py. For now, the current emotion
# API only gives three emotions (pos, neg, neutral) with a magnitude
# from 0.0 to 1.0.
def getEmotion(twitterData):
    # YOUR CODE HERE
    return ('pos', 0.9) # (For example)


###############################################################################

# Returns an object from the simple emotion analysis api
# Example:
#   callSimpleEmotionApi('great')
# Returns:
#   {
#     'probability':
#     {
#         'pos': 0.6986498023830945,
#         'neg': 0.3013501976169055,
#         'neutral': 0.27119050546800266
#     },
#     'label': 'pos'
#   }
def callSimpleEmotionApi(text):
    url = "http://text-processing.com/api/sentiment/"
    details = urlencode({'text': text}).encode('UTF-8')
    request = Request(url, details)
    with urlopen(request) as stuff:
       responseJSON = (b"".join(stuff.readlines())).decode('utf-8')
    return json.loads(responseJSON)
