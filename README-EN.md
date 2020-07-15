----

# Lousa mágica & Lousa paramétrica
#### ([versão em Português](README.md))

Tools for drawing with potentiometers ([take a look at the GitHub repo!](https://github.com/villares/lousa-magica/))

*Lousa mágica* is something like "magic blackboard", it was the name in Portuguese of the "Etch A Sketch" drawing toy that inspired this project. Then *Lousa paramétrica* would mean something like "parametric drawing board".

> [![Magic Drawing Board video - Lousa Mágica](https://img.youtube.com/vi/D5Ha1bhqBuQ/0.jpg)](https://www.youtube.com/watch?v=D5Ha1bhqBuQ)
> <br />Lousa mágica video at Sesc 24 de maio - credits: [João Adriano Freitas](https://github.com/jaafreitas)

#### Brief history

* *Lousa mágica* was inititally presented as part of [Estúdio Hacker](http://estudiohacker.io) activities at the inauguration of [Sesc 24 de Maio](https://www.sescsp.org.br/unidades/36_24+DE+MAIO/#/uaba=programacao#/fdata=id%3D36), on August 2017 (video above). It used 6 potentiometers for drawing and drawings could be erased by tilting the control box. It was also possible to post *tweets* with the drawing content (using a Twitter API library).
* On Estúdio Hacker Day  (September 7th, 2017), also at Sesc 24 de maio, a workshop was held where the participants set up a version of *Lousa mágica* with 4 potentiometers in a protoboard.
* Setups with 4 potentiometers using a variation of the *Lousa mágica* software and a new version called *Lousa paramétrica* with a recursive parametric drawing of a tree were displayed at the [Sesc Art Circuit 2018](https://circuito.sescsp.org.br/).
* Several [*sketch-a-day* project](https://villares.github.com/sketch-a-day) drawings can be used with the same setup.
* `TO DO: more 'usable' drawings links`

#### Materials

* Arduino (or similar board) with at least 4 analog pins;
* USB cable to link up the Arduino to the computer;
* 4 to 6 linear  10kΩ potentiometers (type "B") (you can use 2 or 3 but it's not as cool);
* Protoboard and jumpers;
* Computer and monitor (or a laptop) running Linux, Mac or Windows. Use a big TV or a projector for bigger impact on guests!
* Optional: button or mercury tilt switch (the computer keyboard may be used instead) and 10kΩ resistor  (if it's a button/switch connected to a pin other than `D13`);

#### Setup instructions

![setup](assets/montagem-lousa-magica.png)

1. Download and install the [Arduino IDE](http://arduino.cc) and the [Processing IDE](http://processing.org);

2. Connect your Arduino/board to your computer, open the Arduino IDE, and in the menu `File > Examples > Firmata` look for the *sketch* called **Firmata All Inputs**. Next, select your board's model in `Tools > Board:` , and in `Tools > Port`, the USB/serial port the board is connected to. Lastly, click the `➔` button to upload the sketch to the board;

    > Known problems:
    > - Some Arduino clones need a special USB driver: [How to Install CH340 Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/all#drivers-if-you-need-them)
    > - If you use Linux, you might not have permission to access the USB/serial port, that can be corrected by typing `sudo usermod -a -G dialout <your username>` in your shell prompt.

3. Open the Processing IDE and download the **Arduino (Firmata)** library in `Sketch > Import Library... > Add Library...`. We suggest you select **Python mode** on top right corner menu of the IDE instead of the default `Java` ([detailed instructions here](https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/index-EN.html));

4. Connect each potentiometer to your Arduino/board according to the image:

    4.1 Connect the side terminals of each potentiometer to the `5V` e `GND` pins,

    4.2 Connect the central terminals to the board's analog pins: `A1`, `A2`, `A3` e `A4`;

5. Optionally, if you chose to use a button/switch to erase the drawing in *Lousa mágica*, it must be connected to the `Digital 13` pin and `5V` pin;

    > If not using the `D13` pin,  connect the chosen pin terminal to the 10kΩ resistor  (so called *pull-down* resistor) and to the `GND` pin simultaneously. The `D13` has a built-in *pull-down*

6. Copy the code [`LousaMagica.pyde`](LousaMagica/LousaMagica.pyde) from this repo and  **alter the number of your serial/USB accordingly!** Test using the number of ports that appear in the Processing console, starting from the top of the list: `NUM_PORTA = 0`.;

    > Known problems
    > - Linux: confirm you have access to the USB/serial port (as mentioned in item 2).
    > - 64-bits Windows: Processing might download the incorrect version (32 bits) of the serial library. You can solve this by deleting or renaming the file in `C:\Program Files\processing-3.X.X\modes\java\libraries\serial\library\windows32\jSSC-2.8.dll` as documented in [issue 227](https://github.com/jdf/Processing.py-Bugs/issues/227).

#### Explore other versions in the repo  [`github.com/villares/lousa-magica`](https://github.com/villares/lousa-magica/):

  * *Lousa mágica*:
    - [2 potentiometers version](https://github.com/villares/lousa-magica/tree/master/LousaMagica2pots)
    - [Processing Java mode](https://github.com/villares/lousa-magica/tree/master/LousaMagica_java)
    - [Sesc Art Circuit 2018 version](https://github.com/villares/lousa-magica/tree/master//lousa_magica_versao_circuito_sesc)

  * *Lousa paramétrica*:  
    - [*Recursive tree* (Sesc Art Circuit 2018)](https://github.com/villares/lousa-magica/tree/master/lousa_parametrica_arvore_circuito_sesc)
    - [*Graphs*](https://github.com/villares/lousa-magica/tree/master/lousa_parametrica_grafos)
    - [*Recursive polygons version*](https://github.com/villares/lousa-magica/tree/master/lousa_parametrica_poligonos_recursivos)
    - Look for more *sketches* in the repo [`villares.github.com/sketch-a-day`](https://villares.github.com/sketch-a-day)

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
