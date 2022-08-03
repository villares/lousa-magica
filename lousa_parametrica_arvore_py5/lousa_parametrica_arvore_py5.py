"""
árvore do circuito SESC - alexandre B A villares
http://estudiohacker.io
"""

import pyfirmata


def setup():
    global arduino
    size(600, 600)
    color_mode(HSB)
    # escolhe a porta do Arduino ou reverte para sliders
    arduino = pyfirmata.Arduino('/dev/ttyUSB0')
    pyfirmata.util.Iterator(arduino).start()
    for i in range(1, 5):
        arduino.analog[i].enable_reporting()
    arduino.analog_read = (lambda p: arduino.analog[p].read() * 1024
                           if arduino.analog[p].read() is not None
                           else 0)
def draw():
    global a, b, c, d
    background(0)
    frame_rate(30)
    stroke_weight(2)

    a = remap(arduino.analog_read(1), 0, 1023, 0, HALF_PI)  # ângulo
    # randomização do tamanho do galho
    b = remap(arduino.analog_read(2), 0, 1023, 0, 10)
    c = remap(arduino.analog_read(3), 0, 1023, -2, 2)      # randomização do ângulo
    d = remap(arduino.analog_read(4), 0, 1023, 0, 10)      # profundidade da recursão

    random_seed(int(d * 10))
    with push_matrix():
        translate(width / 2, height / 2)
        branch(d, a, width / 25 + (width / 75) * b)

def branch(gen, theta, branch_size):
    stroke_weight(gen)
    try:
        cor = (remap(gen, 0, d, 255, 0) + frame_count) % 256
    except ZeroDivisionError:
        cor = 0
    stroke(cor, 255, 255)
    # All recursive functions must have an exit condition!!!!
    if gen > 1:  # and branch_size > 1:
        with push_matrix():
            h = branch_size * (1 - random(b / 3, b) / 15)
            rotate(theta + c * random(1))  # Rotate by theta
            line(0, 0, 0, -h)  # Draw the branch
            translate(0, -h)  # Move to the end of the branch
            # Ok, now call myself to draw two branches!!
            with push_style():
                branch(gen - 1, theta, h)
        with push_matrix():
            h = branch_size * (1 - random(b / 3, b) / 15)
            rotate(-theta + c * random(1))
            line(0, 0, 0, -h)
            translate(0, -h)
            with push_style():
                branch(gen - 1, theta, h)

def key_pressed():
    if key == 'p':
        save_frame("lousa-02-####.png")
