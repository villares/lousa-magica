"""
Alexandre B A Villares
Lousa-mágica - desenho com potenciômetros v2022_08_02
http://abav.lugaralgum.com/lousa-magica

Para executar é necessário:
py5 (sketch_runner ou imported mode no Thonny IDE) e PyFirmata 
"""

def setup():
    global arduino
    size(700, 700)   # ajuste aqui o tamanho da área de desenho!
    color_mode(HSB)  # para usar HSB em vez de RGB!
    frame_rate(30)
    no_stroke()
    background(0)
    arduino = get_arduino(0)  # Mude a porta aqui se necessário!   

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

def get_arduino(port=None):
    """
    This is a PyFirmata 'helper' that tries to connect to
    an Arduino compatible board.
    
    If port is None it tries to connect to the last port
    listed by pyserial's serial.tools.list_ports.comports().
    You can provide a string with the port name or an integer
    index to the port (as listed by pyserial and printed in
    the console if no port is provided)
    
    If successful it returns a pyfirmata Arduino object, but
    before that it starts a pyfirmata.util.Iterator, and adds
    to it analog_read() and digital_read() functions that mimic
    Processing's Firmata library interface.
    """
    from pyfirmata import Arduino, util
    from serial.tools import list_ports
    ports = [comport.device for comport in list_ports.comports()]
    if not ports:
        raise Exception('No board/Arduino port found')
    elif port is None:
        print('\n'.join(f'{i}: {p}' for i, p in enumerate(ports)))
        port = len(ports) - 1
    if isinstance(port, str):
        print(f'Trying to connect to port: {port}')
        arduino = Arduino(port)
    else:
        print(f'Trying to connect to port {port}: {ports[port]}')
        arduino = Arduino(ports[port])
    util.Iterator(arduino).start()
    for a in range(6):  # A0 A1 A2 A3 A4 A5
        arduino.analog[a].enable_reporting()
    arduino.analog_read = (lambda a: arduino.analog[a].read() * 1024
                           if arduino.analog[a].read() is not None
                           else 0)
    digital_pin_dict = {d: arduino.get_pin(f'd:{d}:i')
                        for d in range(2, 14)}
    for d in digital_pin_dict.keys():
        digital_pin_dict[d].enable_reporting()
    arduino.digital_read = (lambda d: digital_pin_dict[d].read()
                            if digital_pin_dict[d].read() is not None
                            else False)
    return arduino