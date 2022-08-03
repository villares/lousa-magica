/* Licença GPL3 - mas atribuição é apreciada!
   Desenho com potenciômetros 
   Arduino + Firmata All Inputs + Potenciômetros  
 Alexandre Villares http://abav.lugaralgum.com
 arteprog - arte e programação http://arteprog.space
 Apresentada originalmente na inauguraço do SESC 24 de maio com Estúdio Hacker
 http://estudiohacker.io
 http://twitter.com/estudiohacker
 */

import processing.serial.*;
import cc.arduino.*;

Arduino arduino;
int numPorta = 32;  // Precisa mudar!

void setup() {
  size(512, 512);
  colorMode(HSB);  // para usar HSB em vez de RGB!
  frameRate(30);
  noStroke();
  background(0);
  println(Arduino.list());
  arduino = new Arduino(this, Arduino.list()[numPorta], 57600);
}

void draw() {
  float X = map(arduino.analogRead(1), 0, 1023, 0, width);
  float Y = map(arduino.analogRead(4), 0, 1023, 0, height);
  float tam = arduino.analogRead(2)/10;  // Tamanho
  float sat = arduino.analogRead(3)/4;   // Saturação
  float opa = 255;  // Opacidade/Alpha
  float F = frameCount;
  // Note modo HSB no setup! (Hue/Matiz, Saturação, Brilho, Alfa)
  fill(F % 256, sat, 255, opa);  // Matiz muda com o resto da divisão de frameCount por 256
  ellipse(X, Y, tam, tam);
  boolean tilt = (arduino.digitalRead(13) == arduino.HIGH);
  if (tilt || keyPressed) {
    background(0);  // limpa a área de desenho com fundo preto
  }
}        
