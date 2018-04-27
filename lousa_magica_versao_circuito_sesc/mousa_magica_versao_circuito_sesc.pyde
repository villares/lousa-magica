# Licença GPL3 - mas atribuição é apreciada!
"""
Desenho com potenciômetros 
    Alexandre Villares http://abav.lugaralgum.com http://arteprog.space
    Apresentada originalmente na inauguração do SESC 24 de maio com Estúdio Hacker
    http://estudiohacker.io
"""

# Arduino + Firmata All Inputs: foram usados 4 potenciômetros e um interruptor de mercúrio
add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;

from inputs import *
    
def setup():
    global input
    size(700, 700)
    colorMode(HSB)  # para usar HSB em vez de RGB!
    frameRate(30)
    noStroke()
    background(0)
    # escolhe a porta do Arduino ou reverte para sliders
    input = Input(Arduino)

def draw():

    if input.digital(13):
        background(0) # limpa o canvas com preto
    X = map(input.analog(1), 0, 1023, 0, width)
    Y = map(input.analog(4), 0, 1023, 0, height)
    tam = input.analog(2) / 10 # Tamanho
    sat = input.analog(3) / 4 # Saturação

    F = frameCount
    fill(F % 255, sat, 255)  # Note modo HSB no setup! (Matiz, Saturação, Brilho, Alfa)
    ellipse(X, Y, tam, tam)
    
    # Desenha e lê sliders se necessário
    input.update()
    
def keyPressed():
    if key == 'p':
        saveFrame("lousa-01-####.png")
    if key == 'h':
        input.help()
        
    input.keyPressed()

def keyReleased():
    input.keyReleased()
