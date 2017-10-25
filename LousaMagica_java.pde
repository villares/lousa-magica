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
int numPorta = 0;  // Precisa mudar!

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
  float X = arduino.analogRead(5)/2;  // pino A5 (analógico)
  float Y = arduino.analogRead(0)/2;
  float tam = arduino.analogRead(1)/10;  // Tamanho
  float sat = 255;  // Saturação
  float opa = 255;  // Opacidade/Alpha
  float F = frameCount;
  // Note modo HSB no setup! (Matiz, Saturação, Brilho, Alfa)
  fill(F % 255, sat, 255, opa);
  ellipse(X, Y, tam, tam);
  boolean tilt = (arduino.digitalRead(13) == arduino.HIGH);
  if (tilt) {
    background(0);  // limpa o canvas com preto
  }
}        
