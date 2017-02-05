import os.path

# Hello

from util.parse import parseRequest
from util.twitter import getTwitterData
from util.emotion import getEmotion
from util.color import emotionToColor
from util.file import writeToFile

from flask import Flask, render_template, request
app = Flask(__name__)

# Returns the index page that shows the UI for interacting with the server
@app.route("/")
def showIndex():
    return render_template('index.html', moo='moo')

# Processes the data that came from the user
@app.route("/process", methods=['POST'])
def processData():
    dictionary = parseRequest(request.form['request'])
    twitterData = getTwitterData(dictionary)
    emotion = getEmotion(twitterData)
    color = emotionToColor(emotion)
    writeToFile(dictionary, color)
    # storeColor(color)
    return str(color)

if __name__ == "__main__":
  app.run()
