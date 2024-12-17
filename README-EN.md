----

# Lousa mágica & Lousa paramétrica

#### ([versão em Português](README.md))

Tools for drawing with potentiometers ([take a look at the GitHub repo!](https://github.com/villares/lousa-magica/))

*Lousa mágica* is something like "magic blackboard", it was the name in Portuguese of the "Etch A Sketch" drawing toy that inspired this project. Then *Lousa paramétrica* would mean something like "parametric drawing board".

### Brief history

> [![Magic Drawing Board video - Lousa Mágica](https://img.youtube.com/vi/D5Ha1bhqBuQ/0.jpg)](https://www.youtube.com/watch?v=D5Ha1bhqBuQ)
> <br />Lousa mágica video at Sesc 24 de maio - credits: [João Adriano Freitas](https://github.com/jaafreitas)

* *Lousa mágica* was inititally presented as part of [Estúdio Hacker](http://estudiohacker.io) activities at the inauguration of [Sesc 24 de Maio](https://www.sescsp.org.br/unidades/36_24+DE+MAIO/#/uaba=programacao#/fdata=id%3D36), on August 2017 (video above). It used 6 potentiometers for drawing and drawings could be erased by tilting the control box. 

> ![tweet from Sesc 24 de maio inauguration](https://user-images.githubusercontent.com/3694604/182716588-bd2c7421-f3fa-45b2-b355-ad4d7b6ee68f.png)
> It was also possible to post *tweets* with the drawing content (using a Twitter API library).

* On Estúdio Hacker Day  (September 7th, 2017), also at Sesc 24 de maio, a workshop was held where the participants set up a version of *Lousa mágica* with 4 potentiometers in a breadboard.

* Setups with 4 potentiometers using a variation of the *Lousa mágica* software and a new version called *Lousa paramétrica* with a recursive parametric drawing of a tree were displayed at the [Sesc Art Circuit 2018](https://circuito.sescsp.org.br/).

![Sample of images created by participants](https://user-images.githubusercontent.com/3694604/182716439-e7de967b-ac41-45a5-b437-0427757c7be2.png)

* Several [*sketch-a-day* project](https://villares.github.com/sketch-a-day) drawings were made to be used with the same setup.

* `TO DO: Add links to other 'parametric' drawings that can be modified with pots`

### Setup instructions

#### Materials

* Arduino (or similar board) with at least 4 analog pins;
* USB cable to link up the Arduino to the computer;
* 4 to 6 linear  10kΩ potentiometers (type "B") (you can use 2 or 3 but it's not as cool);
* A breadboard and some jumpers;
* A computer with a display (or a laptop) running Linux, Mac or Windows. Use a big TV or a projector for bigger impact on guests!
* Optional: button or mercury tilt switch (the computer keyboard may be used instead) and 10kΩ resistor  (if it's a button/switch connected to a pin other than `D13`);

![setup](assets/montagem-lousa-magica.png)

1. Download and install the [Arduino IDE](http://arduino.cc);

2. Connect your Arduino/board to your computer, open the Arduino IDE, and in the menu `File > Examples > Firmata` look for the *sketch* called **Firmata All Inputs**. Next, select your board's model in `Tools > Board:` , and in `Tools > Port`, the USB/serial port the board is connected to. Lastly, click the `➔` button to upload the sketch to the board;

    > Known problems:
    > - Some Arduino clones need a special USB driver: [How to Install CH340 Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/all#drivers-if-you-need-them)
    > - If you use Linux, you might not have permission to access the USB/serial port, that can be corrected by typing `sudo usermod -a -G dialout <your username>` in your shell prompt.

3. Connect each potentiometer to your Arduino/board according to the image:

    4.1 Connect the side terminals of each potentiometer to the `5V` e `GND` pins,

    4.2 Connect the central terminals to the board's analog pins: `A1`, `A2`, `A3` e `A4`;

4. Optionally, if you chose to use a button/switch to erase the drawing in *Lousa mágica*, it must be connected to the `Digital 13` pin and `5V` pin;

    > If not using the `D13` pin,  connect the chosen pin terminal to the 10kΩ resistor  (so called *pull-down* resistor) and to the `GND` pin simultaneously. The `D13` has a built-in *pull-down*

5. Now the software part, for drawing in the screen:

    **5.A  To use with Thonny IDE, py5 and pyfirmata**
    - [Install Thonny and the thonny-py5mode plug-in](https://abav.lugaralgum.com/como-instalar-py5/index-EN.html#how-to-install-py5);
    - Inside Thonny IDE, select `Tools > Manage Packages...` and install **pyFirmata**;
    - Copy code from:
        - [LousaMagica_py5.py](LousaMagica_py5/LousaMagica_py5.py) - Drawing with pots 
        - [lousa_parametrica_arvore_py5.py](lousa_parametrica_arvore_py5/lousa_parametrica_arvore_py5.py) - Parametric recursive tree

    5.A  To use in the Processing IDE:
    - Open the Processing IDE and download the **Arduino (Firmata)** library in `Sketch > Import Library... > Add Library...`; 
    - Copy code from [sketches made for Processing Java Mode](Processing-modo-Java.md); 
    - [Sketches made for Processing Python Mode](Processing-modo-Python.md) (not currently working due to Python mode + Serial library issues).
            
#### Arduino Nano example

![setup](assets/montagem2.png)

#### Definitive setup suggestions

* Tools: pliers and soldering iron;
* Use a tilt switch (mercury switch) instead of a button on `D13` to erase drawings in *Lousa mágica*.
* Setup in a box with a transparent panel, with holes for the potentiometers.

#### Other ideas

* Pong with potentiometers, Dojo version: [`github.com/arteprog/cursos/tree/master/DOJO-pong-com-pot`](https://github.com/arteprog/cursos/tree/master/DOJO-pong-com-pot)
* "Wireless" version made by [João Adriano Freitas](https://github.com/jaafreitas): [`github.com/jaafreitas/LousaMagica`](https://github.com/jaafreitas/LousaMagica)

----

Alexandre B A Villares ([abav.lugaralgum.com](https://abav.lugaralgum.com)), [CC-BY-NC-SA-4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/)
Translated by Carolina Giorno
