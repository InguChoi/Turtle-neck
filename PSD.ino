int psd = A0;
int dis = 0;

void setup() 
{
  // put your setup code here, to run once:
    Serial.begin(9600);
    pinMode (psd, INPUT); 
  
}

void loop() {
  // put your main code here, to run repeatedly:
    int psdValue = analogRead(psd);
    int volt = map(psdValue, 0, 1023, 0, 5000);
    dis = (21.61/(volt-0.1696))*1000;
    Serial.println(dis);

    if(dis < 20)
    {
        Serial.println(1);
        delay(100);
      }    
}
