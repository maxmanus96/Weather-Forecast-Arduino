float tempC;
#define LM35_PIN 0
 
void setupLM35() {
}
 
void readLM35() {
  //Serial.println("***********  LM35  *********");
  tempC = analogRead(LM35_PIN);           //read the value from the sensor
  tempC = (5.0 * tempC * 100.0)/1024.0;  //convert the analog data to temperature
  //Serial.print("Temp C: ");
  Serial.println(tempC);             //send the data to the computer
  delay(1000);                           //wait one second before sending new data
 
}
 
void setup()
{
  Serial.begin(9600);
  setupLM35();
}
 
void loop()
{
  readLM35();
  delay(3000);
}
