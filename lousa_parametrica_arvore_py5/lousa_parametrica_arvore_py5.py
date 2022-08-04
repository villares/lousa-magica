"""
Alexandre B A Villares
Árvore do Circuito SESC 2018 - v2022_08_02
https://abav.lugaralgum.com/lousa-magica

Para executar é necessário:
py5 (sketch_runner ou imported mode no Thonny IDE) e PyFirmata 
"""

def setup():
    global arduino
    size(600, 600)
    color_mode(HSB)
    arduino = get_arduino(0) # Or try port name like 'COM3' or '/dev/ttyUSB0' 
 
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
    Processing's Firmata library interface (readings are never
    None, and analog pins return a value between 0 and 1023).
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
    arduino.analog_read = (lambda a: round(arduino.analog[a].read() * 1023)
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