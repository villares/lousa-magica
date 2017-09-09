# Lousa mágica

Um brinquedo para desenhar com potenciômetros

#### Lista de materiais

* Arduino (ou variante com pelo menos 4 portas analógicas);
* Cabo USB para ligar o Arduino ao computador;
* Potenciômetros (de 4 a 6 - com 2 dá mas tem menos graça);
* Protoboard e jumpers;
* Interruptor de mercúrio (opcional);
* Resistor 10kΩ (se for usar o interruptor acima);
* Computador com monitor (ou laptop) Linux, Mac ou Windows.

#### Passos
0. Baixe o IDE do [Arduino](http://arduino.cc) e o IDE do [Processing](http://processing.org);
1. Suba no Arduino o sketch Firmata All Inputs, que já vem nos exemplos da biblioteca Firmata no IDE;
2. Instale no IDE do Processing o Modo Python;
3. Copie o código `LousaMagica.pyde` deste repositório e altere o número da porta serial/USB;
4. Faça a montagem dos potenciômetros:
 4.1 os terminais laterias em 5V e GND,
 4.2 os terminais centrais nos pinos analógiocos do Arduino.
5. O interruptor de mercúrio é opcional e pode ser substituído por um botão intantâneo também, um terminal deve ser ligado no pino digital 13, assim como no resistor *pull-down*/aterrado, o outro na alimentação 5V. 

#### Para uma montagem definitiva
* Alicate;
* Solda;
* Caixinha com frente transparente , furada para os potenciômetros.
