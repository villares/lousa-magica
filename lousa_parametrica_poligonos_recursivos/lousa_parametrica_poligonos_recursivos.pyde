"""
Polígonos recursivos - Alexandre B A Villares - http://estudiohacker.io
Estudo para o Circuito Sesc 2018 (não apresentado)

Tecle 'h' para ajuda...
"""

from __future__ import division
add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*

from inputs import *

def setup():
    global input
    size(600, 600)
    frameRate(10)
    colorMode(HSB)  # makes it easy to cycle colors through Hues...
    noFill()
    # escolhe a porta do Arduino ou reverte para sliders
    input = Input(Arduino)

def draw():
    background(0)

    I = map(input.analog(1), 0, 1023, PI / 6, TWO_PI / 3) # ângulo
    J_upper = 2 + I * 1.5  # change J's upper limit...
    J = map(input.analog(2), 0, 1023, 1, J_upper)  # 1 to 3 + I * 1.5
    K = map(input.analog(3), 0, 1023, 0, 255)  # saturação
    L = map(input.analog(4), 0, 1023, 0, TWO_PI)  # 0 to TWO_PI # giro

    poly_shape(width / 2, height / 2, I, J, K, L)

    # Desenha e lê sliders se necessário
    input.update()

def poly_shape(x, y, angle, D, sat, rotation):
    stroke((frameCount / 2 * D) % 256, sat, 255, 100)
    strokeWeight(D * 10)
    with pushMatrix():
        translate(x, y)
        rotate(rotation)
        radius = D * 40
        # create a polygon on a ps PShape object
        ps = createShape()
        ps.beginShape()
        a = 0
        while a < TWO_PI:
            sx = cos(a) * radius
            sy = sin(a) * radius
            ps.vertex(sx, sy)
            a += angle
        ps.endShape(CLOSE)  # end of PShape creation
        shape(ps, 0, 0)  # Draw the PShape
        if D > 1:  # if the recursion 'distance'/'depth' allows...
            for i in range(ps.getVertexCount()):
                # for each vertex
                pv = ps.getVertex(i)  # gets vertex as a PVector
                # recusively call poly_shape with a smaller D
                poly_shape(pv.x, pv.y, angle, D - 1, sat, rotation)

def keyPressed():
    if key == 'p':
        saveFrame("lousa-03-####.png")
    if key == 'h':
        input.help()

    input.keyPressed()

def keyReleased():
    input.keyReleased()
