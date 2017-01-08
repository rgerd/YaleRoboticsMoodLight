# YaleRoboticsMoodLight
The back-end for a mood light that expresses the mood of the internet!


## Required installs
  * [python3](https://www.python.org/downloads/)
    - Ensure you have python3 on your computer by running `python3` in the shell. It should give you a command prompt that you can quit with `ctrl+D`

## Recommended installs
  * [Github Desktop](https://desktop.github.com/)
    - Makes git super easy
  * [postman](https://www.getpostman.com/)
    - Tests the API

## Optional installs
  * [ngrok](https://ngrok.com/)
    - Exposes the server to the public

## Reading
  * [Twitter sentiment analysis using Python and NLTK] (http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/)
  * [Flask Documentation] (http://flask.pocoo.org/docs/0.12/)
  * [main.py] (https://github.com/rgerd/YaleRoboticsMoodLight/blob/master/main.py)
  * [Makefile] (https://github.com/rgerd/YaleRoboticsMoodLight/blob/master/Makefile)
  * [test (command script)] (https://github.com/rgerd/YaleRoboticsMoodLight/blob/master/test)
  * [Everything in util] (https://github.com/rgerd/YaleRoboticsMoodLight/tree/master/util)

## Getting started
  * Clone the repository to your computer
  * Add the confidential twitterconfig.py file to the config folder
  * Open up the shell, and navigate to the folder you just cloned
  * In the shell, run `make installation` (this installs all requirements for the server code to run)
  * To run the server, either run `make server` or `FLASK_APP=main.py flask run`
  * Now navigate to localhost:5000 to see the index page!
  * To test a specific function, run `./test` with one of `twitter` `emotion` or `color`
    * For example, `./test emotion` will run the `getEmotion` function in `/util/emotion.py` with the data in `example_tweets.py`
  
