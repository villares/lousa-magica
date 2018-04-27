# Licença GPL3 - mas atribuição é apreciada!
"""
Desenho com potenciômetros 
    Alexandre Villares http://abav.lugaralgum.com
    arteprog - arte e programação http://arteprog.space
    Apresentada originalmente na inauguraço do SESC 24 de maio com Estúdio Hacker
    http://estudiohacker.io
    http://twitter.com/estudiohacker
"""

# Arduino + Firmata All Inputs: foram usados potenciômetros e um interruptor de mercúrio
add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;

for num, porta in enumerate(Arduino.list()):  # Enumera portas seriais
    println(str(num)+":"+porta)               # Mostra no console
NUM_PORTA = 3  # Precisa mudar! Confira a lista no console
    
def setup():
    global arduino
    size(700, 700)  # ajuste aqui o tamanho da área de desenho!
    colorMode(HSB)  # para usar HSB em vez de RGB!
    frameRate(30)
    noStroke()
    arduino = Arduino(this, Arduino.list()[NUM_PORTA], 57600)

def draw():
    pot_1 = arduino.analogRead(1) # pino A1 (Analógico 1)
    pot_2 = arduino.analogRead(2)
    pot_3 = arduino.analogRead(3)  
    pot_4 = arduino.analogRead(3)
    tilt = arduino.digitalRead(13) # pino 13 (Digital 13)
    if tilt or keyPressed:
        background(0) # limpa o canvas com preto
    X = map(pot_1, 0, 1023, 0, width)
    Y = map(pot_4, 0, 1023, 0, height)
    tam = pot_2 / 10 # Tamanho
    sat = pot_3 / 4  # Saturação
    opa = 255 # Opacidade/Alpha
    F = frameCount
    fill(F % 255, sat, 255, opa)  # Note modo HSB no setup! (Matiz, Saturação, Brilho, Alfa)
    ellipse(X, Y, tam, tam)
    #println(pot_1, pot_2, pot_3, pot_4, tilt)
