----

# Lousa mágica & Lousa paramétrica

Ferramentas de desenhar com potenciômetros ([veja o repositório no GitHub!](https://github.com/villares/lousa-magica/))

> [![Vídeo da lousa mágica](https://img.youtube.com/vi/D5Ha1bhqBuQ/0.jpg)](https://www.youtube.com/watch?v=D5Ha1bhqBuQ)
> <br />Vídeo da Lousa mágina no Sesc 24 de maio - crédito: [João Adriano Freitas](https://github.com/jaafreitas)

#### Breve histórico

* A *Lousa mágica* foi apresentada inicialmente pelo [Estúdio Hacker](http://estudiohacker.io) na inauguração do Sesc 24 de Maio, em agosto de 2017 (vídeo acima), com 6 potenciômetros, permitia desenhar e apagar o desenho tombando a caixa de controle. Também era possível (por conta de uma biblioteca) postar *tweets* com o desenho.
* No Estúdio Hacker Day em 7 de setembro de 2017, também no Sesc 24 de maio, foi realizada atividade em que os participantes montavam uma versão da *Lousa mágica* com 4 potenciômetros em uma protoboard.
* Para o Circuito Sesc de Artes 2018 foram feitas montagens com 4 potenciômetros com uma variante do software da *Lousa mágica* e uma versão nova chamada *Lousa paramétrica* com um desenho paramétrico recursivo de uma árvore.
* Diversos desenhos do projeto [*sketch-a-day*](https://villares.github.com/sketch-a-day) podem ser usados com a mesma montagem.
* `TO DO: links de outros desenhos 'ajustáveis'`

#### Lista de materiais

* Arduino (ou variante) com pelo menos 4 portas analógicas;
* Cabo USB para ligar o Arduino ao computador;
* 4 a 6 potenciômetros lineares (tipo 'B") de 10kΩ (com 2 ou 3 dá mas tem menos graça);
* Protoboard e jumpers;
* Computador com monitor (ou laptop) Linux, Mac ou Windows. Para impressionar as visitas use uma TV grande ou um projetor.
* Opcionais: botão instantâneo ou interruptor de mercúrio (pode ser usado apenas o teclado do computador) e resistor 10kΩ (caso seja usado um botão/ nterruptor conectado a um pino diferente do D13);

#### Instruções par montagem

![montagem](assets/montagem-lousa-magica.png)

0. Baixe e instale o IDE do [Arduino](http://arduino.cc) e o IDE do [Processing](http://processing.org);

1. Conecte o seu Arduino/placa ao computador e localize nos exemplos do Arduino IDE o *sketch* **Firmata All Inputs**, selecione no menu *Tools*/Ferramentas o modelo da sua placa e a porta serial em que está conectada ao computador. Faça o *Upload* do *sketch* para a placa.;

2. Abra o Processing e pelo próprio IDE baixe e instale o [Modo Python](https://github.com/villares/villares.github.io/blob/master/como-instalar-o-processing-modo-python/index.md) assim como a biblioteca Arduino (Firmata);

3. Faça a montagem dos potenciômetros conforme a imagem:

   4.1 Conecte os terminais laterias de cada potenciômetro aos pinos `5V` e `GND`,

   4.2 Conecte os terminais centrais deles aos pinos analógicos do Arduino: `A1`, `A2`, `A3` e `A4`;

4. O interruptor (ou botão) para apagar o desenho da *Lousa mágica* deve ter um terminal conectado ao pino `Digital 13` e o outro à alimentação `5V`;
> [Se não for usar o pino `D13`,  conecte simultaneamente o terminal do pino escolhido ao resistor de 10kΩ (é o chamado resistor  *pull-down*, e deve então ser conectado ao `GND`). O pino `D13` já tem um *pull-down* embutido]

5. Copie o código [`LousaMagica.pyde`](LousaMagica/LousaMagica.pyde) deste repositório e altere o número da porta serial/USB adequadamente (procure testar usando os números das portas que aparecem no console do Processing);

6. Explore as outras versões no repositório  [`github.com/villares/lousa-magica`](https://github.com/villares/lousa-magica/):

  * *Lousa mágica*: 
    - [versão com apenas 2 potenciômetros](https://github.com/villares/tree/master/lousa-magica/LousaMagica2pots)
    - [versão em Processing Modo Java](https://github.com/villares/lousa-magica/tree/master/LousaMagica_java)
    - [versão Circuito Sesc de Artes 2018](https://github.com/villares/lousa-magica/tree/master//lousa_magica_versao_circuito_sesc)

  * *Lousa paramétrica*:  
    - [*Árvore recursiva* (Circuito Sesc de Artes 2018)](https://github.com/villares/lousa-magica/tree/master/lousa_parametrica_arvore_circuito_sesc)
    - [*Grafos*](https://github.com/villares/lousa-magica/tree/master/lousa_parametrica_grafos)
    - [*Polígonos recursivos*](https://github.com/villares/lousa-magica/tree/master/lousa_parametrica_poligonos_recursivos)
    - Procure mais *sketches* no repositório [`villares.github.com/sketch-a-day`](https://villares.github.com/sketch-a-day)

#### Exemplo de montagem com Arduino Nano

![montagem](assets/montagem2.png)

#### Suguestões para uma montagem definitiva

* Alicate;
* Solda;
* Interruptor de mercúrio (no lugar do botão para apagar o desenho da *Lousa mágica*).
* Caixinha com frente transparente, furada para os potenciômetros.

#### Mais ideias

* Pong com potenciômetros, versão Dojo: [`github.com/arteprog/cursos/tree/master/DOJO-pong-com-pot`](https://github.com/arteprog/cursos/tree/master/DOJO-pong-com-pot)

* Versão "sem fio" feita pelo [João Adriano Freitas](https://github.com/jaafreitas): [`github.com/jaafreitas/LousaMagica`](https://github.com/jaafreitas/LousaMagica)

----

Alexandre B A Villares ([abav.lugaralgum.com](https://abav.lugaralgum.com)), [CC-BY-NC-SA-4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/)
