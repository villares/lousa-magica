# Lousa mágica

Um brinquedo para desenhar com potenciômetros

[![Vídeo da lousa mágica](https://img.youtube.com/vi/D5Ha1bhqBuQ/0.jpg)](https://www.youtube.com/watch?v=D5Ha1bhqBuQ)

#### Lista de materiais
* Arduino (ou variante com pelo menos 4 portas analógicas);
* Cabo USB para ligar o Arduino ao computador;
* Potenciômetros lineares, 5kΩ ou 10kΩ, de 3 a 6 (com 2 dá mas tem menos graça);
* Protoboard e jumpers;
* Interruptor/botão instantâneo (opcional, pode ser usado o teclado do computador);
* Resistor 10kΩ (para o interruptor acima, dispensar se for usar o teclado do computador);
* Computador com monitor (ou laptop) Linux, Mac ou Windows. Para impressionar as visitas use uma TV grande ou um projetor.

#### Passos
0. Baixe o IDE do [Arduino](http://arduino.cc) e o IDE do [Processing](http://processing.org);
1. Conecte o Arduino ao computador e pelo Arduino IDE suba o *sketch* **Firmata All Inputs** que está nos exemplos;
2. Abra o Processing, pelo próprio IDE [instale o Modo Python](https://github.com/villares/villares.github.io/blob/master/como-instalar-o-processing-modo-python/index.md) e baixe a biblioteca Arduino (Firmata);
3. Copie o código `LousaMagica.pyde` deste repositório e altere o número da porta serial/USB;
4. Faça a montagem dos potenciômetros:
 4.1 os terminais laterias conectados a 5V e GND,
 4.2 os terminais centrais conectados aos pinos analógicos do Arduino.
5. O interruptor (ou botão) deve ter um terminal ligado ao pino digital 13 e simultâneamente ao resistor *pull-down* (conectado ao GND). O outro terminal deve ser ligado à alimentação 5V. 

#### Para uma montagem definitiva
* Alicate;
* Solda;
* Interruptor de mercúrio (para substituir o botão que permite apagar o desenho).
* Caixinha com frente transparente , furada para os potenciômetros.
