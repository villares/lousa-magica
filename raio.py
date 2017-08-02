# -*- coding: utf-8 -*-
# Recursive lightning
# Raio recursivo

def raio(x_start, y_start, num, s):
    w = 100
    y_step = 45
    r_range = 20
    with pushMatrix():
        translate(x_start, y_start)
        scale(s, s)
        ps = createShape()
        ps.beginShape()
        ps.stroke(255)
        ps.noFill()
        ps.vertex(0, 0)
        for i in range(num):
            x = w/2 + random(-r_range*2, r_range*2)
            y = i*y_step + random(-r_range, r_range)
            if i % 2: x = -x
            ps.vertex(x, y)
        ps.endShape()
        shape(ps, 0, 0)
        if (num>3): # enquando for maior que 3 vértices
            for i in range(ps.getVertexCount()-2): # só antes dos últimos
                v = ps.getVertex(i)
                raio(v.x, v.y, num-3, 0.5) # recursivo 3 vértices mais curto!
