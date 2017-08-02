"""
Tweet Lightning image using Processing Python Mode
"""
add_library('simpletweet')
from twitter_credentials import *
from raio import *

tw = False
tweet_text = "Tweeted from #Processing #Python Mode"
pspeed = 0

def setup():
    global simpletweet
    size(500, 500)
    frameRate(0.5)
    simpletweet = SimpleTweet(this)
    # Oauth stuff
    simpletweet.setOAuthConsumerKey(OACK)
    simpletweet.setOAuthConsumerSecret(OACS)
    simpletweet.setOAuthAccessToken(OAAT)
    simpletweet.setOAuthAccessTokenSecret(OATS)


def draw():
    background(0)
    strokeCap(ROUND)
    strokeWeight(3)
    x = mouseX
    y = mouseY
    raio(width/2, 0, 10, 1)    

def keyPressed():
    if key == 't':
        println("Trying to tweet...")
        tweet = simpletweet.tweetImage(get(),tweet_text)
        println("Posted " + tweet)
    
    if key == 'c':
        background(0)
    
