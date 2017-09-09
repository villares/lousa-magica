# Lousa mágica

Um brinquedo para desenhar com potenciômetros

#### Lista de materiais
* Arduino (ou variante com pelo menos 4 portas analógicas);
* Cabo USB para ligar o Arduino ao computador;
* Potenciômetros lineares, 5kΩ ou 10kΩ, de 3 a 6 (com 2 dá mas tem menos graça);
* Protoboard e jumpers;
* Interruptor de mercúrio (opcional, pode ser usado um botão comum, ou o teclado do computador);
* Resistor 10kΩ (para o interruptor acima, dispensar se for usar o teclado do computador);
* Computador com monitor (ou laptop) Linux, Mac ou Windows. Para impressionar as visitas use uma TV grande ou um projetor.

#### Passos
0. Baixe o IDE do [Arduino](http://arduino.cc) e o IDE do [Processing](http://processing.org);
1. Suba no Arduino o *sketch* **Firmata All Inputs**, que já vem nos exemplos da biblioteca Firmata no IDE;
2. Instale no IDE do Processing o Modo Python;
3. Copie o código `LousaMagica.pyde` deste repositório e altere o número da porta serial/USB;
4. Faça a montagem dos potenciômetros:
 4.1 os terminais laterias conectados a 5V e GND,
 4.2 os terminais centrais conectados aos pinos analógiocos do Arduino.
5. O interruptor de mercúrio (ou botão intantâneo) deve ter um terminal ligado ao pino digital 13 e simultâneamente ao resistor *pull-down* (conectado ao GND). O outro terminal deve ser ligado à alimentação 5V. 

#### Para uma montagem definitiva
* Alicate;
* Solda;
* Caixinha com frente transparente , furada para os potenciômetros.
