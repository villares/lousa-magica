----

# Lousa mágica & lousa paramétrica

Um brinquedo para desenhar com potenciômetros ([repositório no GitHub!](https://github.com/villares/lousa-magica/))

> [![Vídeo da lousa mágica](https://img.youtube.com/vi/D5Ha1bhqBuQ/0.jpg)](https://www.youtube.com/watch?v=D5Ha1bhqBuQ)
> <br />vídeo - crédito: [João Adriano Freitas](https://github.com/jaafreitas)

#### Breve histórico

* A *Lousa mágica* foi apresentada inicialmente na inauguração do Sesc 24 de Maio, em agosto de 2017 (vídeo acima), com 6 potenciômetros e uma biblioteca para enviar Tweets.
* No Estúdio Hacker Day de 7 de setembro de 2017 no Sesc 24 de maio foi montada pelos participantes numa protoboard com 4 potenciômetros.
* Para o Circuito Sesc de Artes 2018 foram feitas montagens com 4 potenciômetros com uma variante do software da *Lousa mágica* e uma versão nova chamada *Lousa paramétrica* com um desenho paramétrico recursivo.
* Diversos desenhos do projeto [*sketch-a-day*](https://villares.github.com/sketch-a-day) podem ser usados com a mesma montagem.

#### Lista de materiais
* Arduino (ou variante com pelo menos 4 portas analógicas);
* Cabo USB para ligar o Arduino ao computador;
* Potenciômetros lineares, 5kΩ ou 10kΩ, de 4 a 6 (com 2 ou 3 dá mas tem menos graça);
* Protoboard e jumpers;
* Interruptor/botão instantâneo (opcional, pode ser usado o teclado do computador);
* Resistor 10kΩ (opcional, para estabilizar o interruptor se não for usado o pino 13, dispensar também se for usar só o teclado do computador);
* Computador com monitor (ou laptop) Linux, Mac ou Windows. Para impressionar as visitas use uma TV grande ou um projetor.

#### Passos
0. Baixe o IDE do [Arduino](http://arduino.cc) e o IDE do [Processing](http://processing.org);
1. Conecte o Arduino ao computador e pelo Arduino IDE suba o *sketch* **Firmata All Inputs** que está nos exemplos;
2. Abra o Processing, pelo próprio IDE [instale o Modo Python](https://github.com/villares/villares.github.io/blob/master/como-instalar-o-processing-modo-python/index.md) e baixe a biblioteca Arduino (Firmata);
3. Faça a montagem dos potenciômetros:
   4.1 os terminais laterias conectados a 5V e GND,
   4.2 os terminais centrais conectados aos pinos analógicos do Arduino.
4. O interruptor (ou botão) deve ter um terminal conectado ao pino digital 13 e o outro à alimentação 5V. [Se não for usar o pino 13, simultâneamente conecte o terminal do pino escolhido ao resistor *pull-down* que por sua vez conecta ao GND)]
5. Copie o código [`LousaMagica.pyde`](LousaMagica/LousaMagica.pyde) deste repositório e altere o número da porta serial/USB (tem também uma versão do mesmo código com apenas 2 potenciômetros, e outra em Processing Java Mode no [repositório](https://github.com/villares/lousa-magica/));

#### Para uma montagem definitiva
* Alicate;
* Solda;
* Interruptor de mercúrio (para substituir o botão que permite apagar o desenho).
* Caixinha com frente transparente, furada para os potenciômetros.

#### Mais ideias

* Pong com potenciômetros, versão Dojo: https://github.com/arteprog/cursos/tree/master/DOJO-pong-com-pot
* Versão "sem fio" feita pelo [João Adriano Freitas](https://github.com/jaafreitas): https://github.com/jaafreitas/LousaMagica

----

