"""
Árvore do Circuito SESC - Alexandre B A Villares
http://estudiohacker.io 
"""
add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;

from inputs import *

def setup():
    global input
    size(600, 600)
    colorMode(HSB)
    # escolhe a porta do Arduino ou reverte para sliders
    input = Input(Arduino)

def draw():
    global a, b, c, d
    background(0)
    frameRate(30)
    strokeWeight(2)

    a = map(input.analog(1), 0, 1023, 0, HALF_PI)  # ângulo
    b = map(input.analog(2), 0, 1023, 0, 10)      # randomização do tamanho do galho
    c = map(input.analog(3), 0, 1023, -2, 2)      # randomização do ângulo
    d = map(input.analog(4), 0, 1023, 0, 10)      # profundidade da recursão

    randomSeed(int(d * 10))
    with pushMatrix():
        translate(width / 2, height / 2)
        branch(d, a, width / 25 + (width / 75) * b)

    # Desenha e lê sliders se necessário
    input.update()

def branch(gen, theta, branch_size):
    strokeWeight(gen)
    cor = (map(gen, 0, d, 255, 0) + frameCount) % 256
    stroke(cor, 255, 255)
    # All recursive functions must have an exit condition!!!!
    if gen > 1:  # and branch_size > 1:
        with pushMatrix():
            h = branch_size * (1 - random(b / 3, b) / 15)
            rotate(theta + c * random(1))  # Rotate by theta
            line(0, 0, 0, -h)  # Draw the branch
            translate(0, -h)  # Move to the end of the branch
            # Ok, now call myself to draw two branches!!
            with pushStyle():
                branch(gen - 1, theta, h)
        with pushMatrix():
            h = branch_size * (1 - random(b / 3, b) / 15)
            rotate(-theta + c * random(1))
            line(0, 0, 0, -h)
            translate(0, -h)
            with pushStyle():
                branch(gen - 1, theta, h)

def keyPressed():
    if key == 'p':
        saveFrame("lousa-02-####.png")
    if key == 'h':
        input.help()
        
    input.keyPressed()

def keyReleased():
    input.keyReleased()
