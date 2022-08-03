----

# Lousa mágica & Lousa paramétrica 

#### [(English version here)](/README-EN.md)

Ferramentas de desenhar com potenciômetros ([veja o repositório no GitHub!](https://github.com/villares/lousa-magica/))

### Breve histórico

> [![Vídeo da lousa mágica](https://img.youtube.com/vi/D5Ha1bhqBuQ/0.jpg)](https://www.youtube.com/watch?v=D5Ha1bhqBuQ)
> <br />Vídeo da Lousa mágina no Sesc 24 de maio - crédito: [João Adriano Freitas](https://github.com/jaafreitas)

* A *Lousa mágica* foi apresentada inicialmente em conjunto com as atividades do [Estúdio Hacker](http://estudiohacker.io) na inauguração do Sesc 24 de Maio, em agosto de 2017 (vídeo acima). Usando 6 potenciômetros, permitia desenhar e o desenho podia ser apagado tombando a caixa de controle.

> ![tweet da inauguração do Sesc 24 de maio](https://user-images.githubusercontent.com/3694604/182716588-bd2c7421-f3fa-45b2-b355-ad4d7b6ee68f.png)
> Também era possível postar automaticamente o desenho em um *tweet* (usando uma biblioteca que acessava a API do Twitter e as credencias da conta do Estúdio Hacker).

* No Estúdio Hacker Day em 7 de setembro de 2017, também no Sesc 24 de maio, foi realizada atividade em que os participantes montavam uma versão da *Lousa mágica* com 4 potenciômetros em uma protoboard.

* Para o Circuito Sesc de Artes 2018 foram feitas montagens com 4 potenciômetros com uma variante do software da *Lousa mágica* e uma versão nova chamada *Lousa paramétrica* com um desenho paramétrico recursivo de uma árvore.

![Amostra de imagens produzidas](https://user-images.githubusercontent.com/3694604/182716439-e7de967b-ac41-45a5-b437-0427757c7be2.png)

* Diversos desenhos do projeto [*sketch-a-day*](https://villares.github.com/sketch-a-day) foram feitos para ser usados com a mesma montagem.

* A partir de 2020 o Processing modo Python passou a ter problemas em carregar a biblioteca *Serial* que é necessária para a comunicação com *Firmata* tornando difícil a utilização deste projeto.

* Em 2022 foi acrescentada uma versão para uso com [Thonny IDE e a biblioteca py5](https://abav.lugaralgum.com/como-instalar-py5/)

* `TO DO: links de outros desenhos 'paramétricos' feitos para modificar com potenciômetros`

### Instruções de montagem

#### Lista de materiais

* Arduino (ou variante) com pelo menos 4 portas analógicas;
* Cabo USB para ligar o Arduino ao computador;
* 4 a 6 potenciômetros lineares (tipo "B") de 10kΩ (com 2 ou 3 dá mas tem menos graça);
* Protoboard e jumpers;
* Computador com monitor (ou laptop) Linux, Mac ou Windows. Para impressionar as visitas use uma TV grande ou um projetor.
* Opcional: Botão instantâneo ou interruptor de mercúrio (pode ser usado apenas o teclado do computador) e resistor 10kΩ (caso seja usado um botão/interruptor conectado a um pino diferente do `D13`);

![montagem](assets/montagem-lousa-magica.png)

#### Passo a passo

1. Baixe e instale o IDE do [Arduino](http://arduino.cc);

2. Conecte o seu Arduino/placa ao computador, abra o Arduino IDE, localize e abra pelo menu `File > Examples > Firmata` o *sketch* chamado **Firmata All Inputs**, em seguida selecione no menu `Tools > Board:` o modelo da sua placa, e em `Tools > Port` a porta USB/serial em que a placa está conectada ao computador. Por fim use o botão `➔` para fazer o *upload* do *sketch* para a placa.;

    > Problemas conhecidos:
    > - Alguns clones de Arduino precisam de um driver USB especial: [How to Install CH340 Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/all#drivers-if-you-need-them)
    > - No Linux, você pode estar sem permissão de acesso à porta USB/serial, o que pode ser corrigido
    > abrindo uma janela de terminal e digitando na linha de comando `sudo usermod -a -G dialout <seu nome de usuário do linux aqui>`
    > ou, caso o anterior não resolva, `sudo chmod a+rw /dev/ttyACM0`  (troque `ttyACM0` pelo nome da sua porta, como por exemplo `ttyUSB0`) 

3. Faça a conexão dos potenciômetros ao seu Arduino/placa conforme a imagem:

    3.1 Conecte os terminais laterias de cada potenciômetro aos pinos `5V` e `GND`,

    3.2 Conecte os terminais centrais deles aos pinos analógicos do Arduino: `A1`, `A2`, `A3` e `A4`;
    4.
4. Opcionalmente, se for usar um interruptor (ou botão) para apagar o desenho da *Lousa mágica*, este deve ter um terminal conectado ao pino `Digital 13` e o outro à alimentação `5V`;

    > Se não for usar o pino `D13`,  conecte simultaneamente o terminal do pino escolhido ao resistor de 10kΩ (é o chamado resistor  *pull-down*, e deve então ser conectado ao `GND`). O pino `D13` já tem um *pull-down* embutido

5. Veja as intruções para alguma das variantes da parte do software que desenha na tela:

    A. [Versão inicial com Processing modo Python](Processing-modo-Python.md) (não está funcionando atualmente)
    
    B. [Versão com Processing modo Java](Processing-modo-Java.md)       
    
    C. [Versão com Thonny IDE, py5 e pyfirmata](Thonny-py5.md)
    
#### Exemplo de montagem com Arduino Nano

![montagem](assets/montagem2.png)

#### Suguestões para uma montagem definitiva

* Ferramentas: Alicate e solda;
* Use um interruptor de mercúrio no `D13` em lugar do botão para apagar o desenho da *Lousa mágica*.
* Monte em uma caixinha com frente transparente, faça furos para os potenciômetros.

#### Outras ideias

* Pong com potenciômetros, versão Dojo: [`github.com/arteprog/cursos/tree/master/DOJO-pong-com-pot`](https://github.com/arteprog/cursos/tree/master/DOJO-pong-com-pot) [REVISAR!]
* Versão "sem fio" feita pelo [João Adriano Freitas](https://github.com/jaafreitas): [`github.com/jaafreitas/LousaMagica`](https://github.com/jaafreitas/LousaMagica)

----

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/villares/lousa-magica/">lousa-magica</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://abav.lugaralgum.com">Alexandre B A Villares</a> é um trabalho licenciado sob <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>

Exceto se indicado/atribuído de outra forma em um arquivo ou trecho de código. Entre em contato para questões de licenciamento.
