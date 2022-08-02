# Versão inicial com Processing modo Python (não está funcionando)

**Atenção:** As instruções a seguir são apenas para registro histórico. No momento há relatos de que no IDE Processig 3.5.4 a biblioteca Serial da qual depende a biblioteca Arduino/Firmata não está funcionando, e
o modo Python também não está funcionando no IDE Processing 4.0. 

----
 
1. Instale o Processing IDE versão 3.5.4 e instale o **modo Python** pelo menu de seleção de modos no canto superior direito do IDE, que inicialmente marca `Java` ([instruções detalhadas](https://github.com/villares/villares.github.io/blob/master/como-instalar-o-processing-modo-python/index.md));

2. Abra o Processing IDE e pelo menu `Sketch > Import Library... > Add Library...` baixe e instale a biblioteca **Arduino (Firmata)**.

3. Copie o código [`LousaMagica.pyde`](LousaMagica/LousaMagica.pyde) deste repositório e **altere o número da porta serial/USB adequadamente!**
Procure testar usando os números das portas que aparecem no console do Processing, começando pela primeira da lista: `NUM_PORTA = 0`.;

    > Problemas conhecidos:
    > - No Linux, confirme a permissão de acesso à porta USB/serial (mencionados no final do item 2).
    > - No Windows 64-bits o Processing modo Python pode tentar carregar a versão errada, de 32-bits, da biblioteca de comunicação serial. É possivel contornar o problema apagando ou renomeando o arquivo `C:\Program Files\processing-3.X.X\modes\java\libraries\serial\library\windows32\jSSC-2.8.dll` como documentado em [issue 227](https://github.com/jdf/Processing.py-Bugs/issues/227).

#### Explore as outras versões no repositório  [`github.com/villares/lousa-magica`](https://github.com/villares/lousa-magica/):

  * *Lousa mágica*: 
    - [versão com apenas 2 potenciômetros](https://github.com/villares/lousa-magica/tree/master/LousaMagica2pots)
    - [versão Circuito Sesc de Artes 2018](https://github.com/villares/lousa-magica/tree/master//lousa_magica_versao_circuito_sesc)

  * *Lousa paramétrica*:  
    - [*Árvore recursiva* (Circuito Sesc de Artes 2018)](https://github.com/villares/lousa-magica/tree/master/lousa_parametrica_arvore_circuito_sesc)
    - [*Grafos*](https://github.com/villares/lousa-magica/tree/master/lousa_parametrica_grafos)
    - [*Polígonos recursivos*](https://github.com/villares/lousa-magica/tree/master/lousa_parametrica_poligonos_recursivos)
    - Procure mais *sketches* no repositório [`villares.github.com/sketch-a-day`](https://villares.github.com/sketch-a-day)

