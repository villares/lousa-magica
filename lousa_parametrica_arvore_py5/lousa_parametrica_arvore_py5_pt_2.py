"""
Alexandre B A Villares - http://abav.lugaralgum.com/lousa-magica
Árvore Recursiva - Circuito SESC de arte 2018
v2023-06-10 - Versão com py5 e código em um arquivo só.
v2023-11-08 - Versão 2 pots.

Para executar é necessário:
No computador, bibliotecas py5 e PyFirmata, Thonny IDE
com o thonny-py5mode ativando o *imported mode*.
No Arduino, ligado em uma porta USB, o código FirmataAllImputs carregado
e conexão das portas analógias A1 e A2 a 2 potenciômetros.
"""

def setup():
    global arduino
    size(700, 700)
    color_mode(HSB)
    arduino = get_arduino()
    if arduino is None:
        print('Não consegui conectar ao Arduino.')
        exit_sketch()
 
def draw():
    global a, b, c, d
    background(0)
    frame_rate(30)
    stroke_weight(2)

    a = remap(arduino.analog_read(1), 0, 1023, 0, HALF_PI)  # ângulo
    # randomização do tamanho do galho
    b = remap(arduino.analog_read(2), 0, 1023, 0, 10)
    c = 0 #remap(arduino.analog_read(3), 0, 1023, -2, 2)      # randomização do ângulo
    d = 10 #remap(arduino.analog_read(4), 0, 1023, 0, 10)      # profundidade da recursão

    random_seed(int(d * 10))
    with push_matrix():
        translate(width / 2, height / 2)
        galho(d, a, width / 25 + (width / 75) * b)

def galho(gen, theta, galho_size):
    stroke_weight(gen)
    cor = (remap(gen, 0, d, 255, 0) + frame_count) % 256
    stroke(cor, 255, 255)
    # All recursive functions must have an exit condition!!!!
    if gen > 1:  # and galho_size > 1:
        with push_matrix():
            h = galho_size * (1 - random(b / 3, b) / 15)
            rotate(theta + c * random(1))  # Rotate by theta
            line(0, 0, 0, -h)  # Draw the galho
            translate(0, -h)  # Move to the end of the galho
            # Ok, now call myself to draw two galhoes!!
            with push_style():
                galho(gen - 1, theta, h)
        with push_matrix():
            h = galho_size * (1 - random(b / 3, b) / 15)
            rotate(-theta + c * random(1))
            line(0, 0, 0, -h)
            translate(0, -h)
            with push_style():
                galho(gen - 1, theta, h)

def key_pressed():
    if key == 'p':
        save_frame("imagem####.png")

def get_arduino(port=None):
    """Função ajudante para conectar em um Arduino usando PyFirmata."""   
    from pyfirmata import Arduino, util
    from serial.tools import list_ports
    
    comports = [comport.device for comport in list_ports.comports()]
    if not comports:
        print('Nenhoma porta de conexão encontrada.')
        return None
    elif isinstance(port, str) and port not in comports:
        print(f'Port "{port}" não encontrada.')
        return None
    elif isinstance(port, int):
        if port >= len(comports):
            print(f'Port [{port}] não encontrada.')
            return None
        else:
            port = comports[port]
    elif len(comports) == 1:
        port = comports[0]
    elif port is None:
        port = option_pane(
            'Em qual entrada está o seu Arduino?',
            'Selecione a porta USB:',
            comports,
            -1)  # index for default option
        if port is None:
            print('Nenhuma porta selecionada.')
            return None
    try:
        print(f'Conectando na porta {port}...')
        arduino = Arduino(port)
        util.Iterator(arduino).start()
    except Exception as e:
        print(repr(e))
        return None
    # Prepare analog_read() for A0 A1 A2 A3 A4 A5
    for a in range(6):  
        arduino.analog[a].enable_reporting()
    arduino.analog_read = (lambda a: round(arduino.analog[a].read() * 1023)
                           if arduino.analog[a].read() is not None
                           else 0)
    # Prepare digital_read() for D2 to D13
    digital_pin_dict = {d: arduino.get_pin(f'd:{d}:i')
                        for d in range(2, 14)}
    for d in digital_pin_dict.keys():
        digital_pin_dict[d].enable_reporting()
    arduino.digital_read = (lambda d: digital_pin_dict[d].read()
                            if digital_pin_dict[d].read() is not None
                            else False)
    return arduino


def option_pane(title, message, options, default=None, index_only=False):
    """Java swing JOptionPane input dialog with drop down options."""
    from javax.swing import JOptionPane
    
    if default is None:
        default = options[0]
    elif index_only:
        default = options[default]

    selection = JOptionPane.showInputDialog(
        None,     # frame
        message,
        title,
        JOptionPane.INFORMATION_MESSAGE,
        None,     # for Java null
        options,
        default)  # must be in options, otherwise first is shown
    if selection:
        if index_only:
            return options.index(selection)
        else:
            # Trouble: selection can be java.lang.String
            return str(selection) if selection else None
