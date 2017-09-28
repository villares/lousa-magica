# Licença GPL3 - mas atribuição é apreciada!
"""
Desenho com potenciômetros 
    Alexandre Villares http://abav.lugaralgum.com
    arteprog - arte e programação http://arteprog.space
    Apresentado na inauguraço do SESC 24 de maio com Estúdio Hacker
    http://estudiohacker.io
    http://twitter.com/estudiohacker
"""

# Arduino + Firmata All Inputs: foram usados 6 potenciômetros e um interruptor de mercúrio + pull down
add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
SERIAL = 32  # Precisa mudar! Use println((Arduino.list())) para descobrir
# Twitter - credenciais no arquivo twitter_credentials.py
from twitter_credentials import OACK, OACS, OAAT, OATS
add_library('simpletweet')
tweet_text = u"Inauguração #sesc24demaio desenhando com potenciômetros, #Arduino, #Firmata e #Processing #Python Mode"

def setup():
    global simpletweet, arduino
    size(1024, 1024)
    colorMode(HSB)  # para usar HSB em vez de RGB!
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
    pot_branco = arduino.analogRead(5) # pino A5 (analógico)
    pot_amarelo = arduino.analogRead(4)
    pot_laranja = arduino.analogRead(3)
    pot_vermelho = arduino.analogRead(2)
    pot_verde = arduino.analogRead(1)
    pot_azul = arduino.analogRead(0)
    tilt = arduino.digitalRead(13) # pino 13 (digital)
    if tilt:
        background(0) # limpa o canvas com preto
    X = pot_branco
    Y = pot_azul
    tam = pot_verde / 10 # Tamanho
    sat = pot_laranja / 4 # Saturação
    opa = pot_amarelo / 4 # Opacidade/Alpha

    F = frameCount
    fill(F % 255, sat, 255, opa)  # Note modo HSB no setup! (Matiz, Saturação, Brilho, Alfa)
    ellipse(X, Y, tam, tam)
    #print(pot_branco, pot_amarelo, pot_laranja, pot_vermelho, pot_verde, pot_azul, tilt)

def keyPressed():
    if key == 't':
        println("Mandando um tweet...")
        tweet = simpletweet.tweetImage(get(), tweet_text) # depois de postar muitas imagens a conta foi bloqueada
        println("Postado em " + tweet)
