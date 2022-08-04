"""
This will hopefully switch between Arduino (Firmata) variable input and
nice sliders based on Peter Farell's Sliders htts://twitter.com/hackingmath
https://github.com/hackingmath/python-sliders http://farrellpolymath.com/


2020-03-14 Fix for Arduino no the first serial port (index 0)!
2022-08-03 Converting for use with py5 and pyFirmata
"""
from py5 import *
from pyfirmata import Arduino, util
from serial.tools import list_ports
from javax.swing import JOptionPane

comports = [comport.device for comport in list_ports.comports()]

class InputInterface:

    def __init__(self):
        self.select_source()
        if self.source is None:
            w, h = width(), height()
            # start, end, default
            A = Slider(0, 1023, 128)
            B = Slider(0, 1023, 128)
            C = Slider(0, 1023, 128)
            D = Slider(0, 1023, 128)
            A.position(40, h - 70)
            B.position(40, h - 30)
            C.position(w - 140, h - 70)
            D.position(w - 140, h - 30)
            self.sliders = {1: A, 2: B, 3: C, 4: D}

    def analog(self, pin):
        if self.source is not None:
            return self.source.analog_read(pin)
        else:
            return self.sliders[pin].val

    def update(self, is_mouse_pressed, mouse_x, mouse_y):
        if self.source is None:
            for pin, slider in self.sliders.items():
                slider.update(is_mouse_pressed, mouse_x, mouse_y)

    def key_pressed(self, key, key_code):
        if key == 'a':
            self.sliders[1].down = True
        if key == 'd':
            self.sliders[1].up = True
        if key == 's':
            self.sliders[2].down = True
        if key == 'w':
            self.sliders[2].up = True
        if key_code == LEFT:
            self.sliders[3].down = True
        if key_code == RIGHT:
            self.sliders[3].up = True
        if key_code == DOWN:
            self.sliders[4].down = True
        if key_code == UP:
            self.sliders[4].up = True

    def key_released(self, key, key_code):
        if key == 'a':
            self.sliders[1].down = False
        if key == 'd':
            self.sliders[1].up = False
        if key == 's':
            self.sliders[2].down = False
        if key == 'w':
            self.sliders[2].up = False
        if key_code == LEFT:
            self.sliders[3].down = False
        if key_code == RIGHT:
            self.sliders[3].up = False
        if key_code == DOWN:
            self.sliders[4].down = False
        if key_code == UP:
            self.sliders[4].up = False

    def digital(self, pin):
        space_pressed = is_key_pressed() and key() == ' '
        if self.source is not None:
            if pin == 13:
                return self.source.digital_read(13) or space_pressed
            else:
                return self.source.digital_read(pin)
        else:
            return space_pressed

    def select_source(self):
        port_list = comports[:]
        if not port_list:
            port_list.append(None)
        choice = option_pane("O seu Arduino está conectado?",
                                  "Escolha a porta ou pressione Cancel\npara usar 'sliders':",
                                  port_list,
                                  -1)  # index for default option
        if choice is not None:
            self.source = get_arduino(comports[choice])
        else:
            self.source = None
        # print(self.source) # for debug
        self.help()

    def help(self):
        if self.source is not None:
            message = """   Teclas:
            'h' para esta ajuda
            'p' para salvar uma imagem"""
        else:
            message = """    Teclas:
            'h' para esta ajuda
            'p' para salvar uma imagem
            'a' (-) ou 'd' (+) para o slider 1
            's' (-) ou 'w' (+) para o slider 2
             ←(-) ou  → (+) para o slider 3
             ↓  (-) ou  ↑  (+) para o slider 4"""
        ok = JOptionPane.showMessageDialog(None, message)


def option_pane(title, message, options, default=None, index_only=True):

    if default == None:
        default = options[0]
    elif index_only:
        default = options[default]

    selection = JOptionPane.showInputDialog(
        None, #frame,
        message,
        title,
        JOptionPane.INFORMATION_MESSAGE,
        None,  # for Java null
        options,
        default)  # must be in options, otherwise 1st is shown
    if selection:
        if index_only:
            return options.index(selection)
        else:
            return selection

class Slider:

    SLIDERS = []

    def __init__(self, low, high, default):
        '''slider has range from low to high
        and is set to default'''
        self.low = low
        self.high = high
        self.val = default
        self.clicked = False
        self.up, self.down = False, False
        Slider.SLIDERS.append(self)

    def position(self, x, y):
        '''slider's position on screen'''
        self.x = x
        self.y = y
        # the position of the rect you slide:
        self.rectx = self.x + remap(self.val, self.low, self.high, 0, 120)
        self.recty = self.y - 10

    def update(self, is_mouse_pressed, mouse_x, mouse_y):
        '''updates the slider'''
        push_style()
        rect_mode(CENTER)
        # black translucid rect behind slider
        fill(0, 100)
        no_stroke()
        rect(self.x + 60, self.y, 130, 20)
        # gray line behind slider
        stroke_weight(4)
        stroke(200)
        line(self.x, self.y, self.x + 120, self.y)
        # press mouse to move slider
        if (self.x < mouse_x < self.x + 120 and
                self.y < mouse_y < self.y + 20):
            fill(250)
            text_size(10)
            text(str(int(self.val)), self.rectx, self.recty + 35)
            if is_mouse_pressed:
                self.rectx = mouse_x
        # key usage
        if self.up:
            self.rectx += 1
        if self.down:
            self.rectx -= 1
        # constrain rectangle
        self.rectx = constrain(self.rectx, self.x, self.x + 120)
        # draw rectangle
        no_stroke()
        fill(255)
        rect(self.rectx, self.recty + 10, 10, 20)
        self.val = remap(self.rectx, self.x, self.x + 120, self.low, self.high)
        pop_style()



def get_arduino(port=None):
    try:
        arduino = Arduino(port)
    except:
        return None
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