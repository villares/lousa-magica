""" Desenho com potenciômetros """

# Arduino / Firmata
add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
SERIAL = 32  # CHANGE, use println((Arduino.list())) to find out
# Twitter
from twitter_credentials import OACK, OACS, OAAT, OATS
add_library('simpletweet')
tweet_text = u"Inauguração #sesc24demaio desenhando com potenciômetros, #Arduino, #Firmata e #Processing #Python Mode"

def setup():
    global simpletweet, arduino
    size(1024, 1024)
    colorMode(HSB)  # Not using RGB mode this time ;)
    frameRate(30)
    noStroke()
    background(0)
    arduino = Arduino(this, Arduino.list()[SERIAL], 57600)
    simpletweet = SimpleTweet(this)
    simpletweet.setOAuthConsumerKey(OACK)
    simpletweet.setOAuthConsumerSecret(OACS)
    simpletweet.setOAuthAccessToken(OAAT)
    simpletweet.setOAuthAccessTokenSecret(OATS)


def draw():
    branco = arduino.analogRead(5)
    amarelo = arduino.analogRead(4)
    laranja = arduino.analogRead(3)
    vermelho = arduino.analogRead(2)
    verde = arduino.analogRead(1)
    azul = arduino.analogRead(0)
    tilt = arduino.digitalRead(13)
    if tilt:
        background(0)
    X = branco
    Y = azul
    T = verde / 10 # Tamanho
    S = laranja / 4 # Saturação
    F = frameCount
    fill(F % 255, S, 255)  # notice HSB mode on setup!
    ellipse(X, Y, T, T)
    print(branco, amarelo, laranja, vermelho, verde, azul, tilt)

def keyPressed():
    if key == 't':
        println("Mandando um tweet...")
        tweet = simpletweet.tweetImage(get(), tweet_text)
        println("Postado em " + tweet)
