/*
Árvore do Circuito SESC - Alexandre B A Villares
 http://estudiohacker.io 
 */

import processing.serial.*;
import cc.arduino.*;

Arduino arduino;
int numPorta = 0; 

float a, b, c;
int d;

void setup() {
  size(600, 600);
  colorMode(HSB);
  // escolhe a porta do Arduino ou reverte para sliders
  arduino = new Arduino(this, Arduino.list()[numPorta], 57600);
}
void draw() {
  background(0);
  frameRate(30);
  strokeWeight(2);

  a = map(arduino.analogRead(1), 0, 1023, 0, HALF_PI);  // ângulo
  b = map(arduino.analogRead(2), 0, 1023, 0, 10);      // randomização do tamanho do galho
  c = map(arduino.analogRead(3), 0, 1023, -2, 2);     // randomização do ângulo
  d = int(map(arduino.analogRead(4), 0, 1023, 1, 10));    // profundidade da recursão

  randomSeed(int(d * 10));
  pushMatrix();
  translate(width / 2, height / 2);
  branch(d, a, width / 25 + (width / 75) * b);
  popMatrix();
}

void branch(int gen, float theta, float branch_size) {
  float h;
  strokeWeight(gen);
  int cor = int(map(gen, 0, d, 255, 0) + frameCount) % 256;
  stroke(cor, 255, 255);
  // All recursive functions must have an exit condition!!!!
  if (gen > 1) {  // and branch_size > 1{
    pushMatrix();
    h = branch_size * (1 - random(b / 3, b) / 15);
    rotate(theta + c * random(1));  // Rotate by theta
    line(0, 0, 0, -h);  // Draw the branch
    translate(0, -h);  // Move to the end of the branch
    // Ok, now call myself to draw two branches!!
    pushStyle();        
    branch(gen - 1, theta, h);
    popStyle();
    popMatrix();
    pushMatrix();
    h = branch_size * (1 - random(b / 3, b) / 15);
    rotate(-theta + c * random(1));
    line(0, 0, 0, -h);
    translate(0, -h);
    pushStyle() ;
    branch(gen - 1, theta, h);
    popStyle();
    popMatrix();
  }
}
void keyPressed() {
  if (key == 'p') {
    saveFrame("lousa-02-////////.png");
  }
}
