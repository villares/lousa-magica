----

# Versão com Processing modo Java

1. Instale o Processing IDE baixando de https://processing.org. Inicialmente este projeto foi testado apenas com a versão 3.5.4;

2. Abra o Processing IDE e pelo menu `Sketch > Import Library... > Add Library...` baixe e instale a biblioteca **Arduino (Firmata)**;

3. Copie o código deste repositório e **altere o número da porta serial/USB adequadamente!** 

    - [LousaMagica_java.pde](LousaMagica_java/LousaMagica_java.pde) - desenho com potenciômetros 
    - [lousa_parametrica_arvore_java.pde](lousa_parametrica_arvore_java/lousa_parametrica_arvore_java.pde) - árvore recursiva

    > Problemas conhecidos:
    > - Confira a linha `int numPorta = 0;  // Precisa mudar!` e mude conforme a portas indicadas no console.;
    > - No Linux, confirme a permissão de acesso à porta USB/serial (mencionados no final do item 2 da página inicial de montagem do harware).

