# Licença GPL3 - mas atribuição é apreciada!
"""
Alexandre B A Villares
desenho com potenciômetros
http://abav.lugaralgum.com/lousa-magica
"""

import pyfirmata

def setup():
    global arduino
    size(700, 700)   # ajuste aqui o tamanho da área de desenho!
    color_mode(HSB)  # para usar HSB em vez de RGB!
    frame_rate(30)
    no_stroke()
    background(0)
    arduino = pyfirmata.Arduino('/dev/ttyUSB0')
    pyfirmata.util.Iterator(arduino).start()
    for i in range(6):
        arduino.analog[i].enable_reporting()
    arduino.analog_read = (lambda p: arduino.analog[p].read() * 1024
                           if arduino.analog[p].read() is not None
                           else 0)
    digital_pins = {13: arduino.get_pin('d:13:i')}
    for pin in digital_pins.values():
        pin.enable_reporting()
    arduino.digital_read = lambda p: digital_pins[p].read()    

def draw():
    pot_1 = arduino.analog_read(1)  # pino A1 (Analógico 1)
    pot_2 = arduino.analog_read(2)
    pot_3 = arduino.analog_read(3)
    pot_4 = arduino.analog_read(4)
    tilt = arduino.digital_read(13) # pino 13 (Digital 13)
    if tilt or is_key_pressed:
        background(0)  # limpa o canvas com preto
    x = remap(pot_1, 0, 1023, 0, width)
    y = remap(pot_4, 0, 1023, 0, height)
    tam = pot_2 / 10  # Tamanho
    sat = pot_3 / 4  # Saturação
    opa = 255  # Opacidade/Alpha
    F = frame_count
    # Note modo HSB no setup! (Matiz, Saturação, Brilho, Alfa)
    fill(F % 256, sat, 255, opa)  
    ellipse(x, y, tam, tam)
    #println(pot_1, pot_2, pot_3, pot_4, tilt)
