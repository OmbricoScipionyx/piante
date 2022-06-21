 void setup() {

  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);

}

void loop() {

  // read the input on analog pin 0 and 1:
  int monstera = analogRead(A0);
  int fagiolo = analogRead(A1);

  // print out the value you read:
  Serial.print(monstera);
  Serial.print(" ");
  Serial.println(fagiolo);

  // delay in between reads for stability
  delay(5000);

}
