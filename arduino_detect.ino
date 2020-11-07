//Initializing
#define led1 6
#define led2 7
#define led3 8
int data;
int x=0;

//Including required libraries
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include <Servo.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
Servo servo1;

void setup()
{
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  lcd.begin();
  //Initially red and green lights will be off and yellow will be on
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, HIGH);
  digitalWrite(LED_BUILTIN, LOW);
  servo1.attach(9);
  servo1.write(180);
  // Turning on the blacklight and print a message.
  lcd.backlight();
  lcd.setCursor(2,0);
  lcd.print("Please Enter");
  lcd.setCursor(4,1);
  lcd.print("Passcode");
}

void loop()
{
  while(Serial.available()){
    //Reading the data which is sent by the python code
    data = Serial.read();
    //According the output of python code, the arduino's output is set
    if (x == 0){
      if (data == '0'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('0');
        lcd.setCursor(6,1);
        lcd.print("*");
        x = x+1;
      }
      else if (data == '1'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('1');
        lcd.setCursor(6,1);
        lcd.print("*");
        x = x+1;
      }
      else if (data == '2'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('2');
        lcd.setCursor(6,1);
        lcd.print("*");
        x = x+1;
    }
      else if (data == '3'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('3');
        lcd.setCursor(6,1);
        lcd.print("*");
        x = x+1;
    }
      else if (data == '4'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('4');
        lcd.setCursor(6,1);
        lcd.print("*");
        x = x+1;
    }
      else if (data == '5'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('5');
        lcd.setCursor(6,1);
        lcd.print("*");
        x = x+1;
    }
  }
    else if (x == 1){
      if (data == '0'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('0');
        lcd.setCursor(6,1);
        lcd.print("**");
        x = x+1;
      }
      else if (data == '1'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('1');
        lcd.setCursor(6,1);
        lcd.print("**");
        x = x+1;
      }
      else if (data == '2'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('2');
        lcd.setCursor(6,1);
        lcd.print("**");
        x = x+1;
    }
      else if (data == '3'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('3');
        lcd.setCursor(6,1);
        lcd.print("**");
        x = x+1;
    }
      else if (data == '4'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('4');
        lcd.setCursor(6,1);
        lcd.print("**");
        x = x+1;
    }
      else if (data == '5'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('5');
        lcd.setCursor(6,1);
        lcd.print("**");
        x = x+1;
    }
  }
  else if (x == 2){
      if (data == '0'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('0');
        lcd.setCursor(6,1);
        lcd.print("***");
        x = x+1;
      }
      else if (data == '1'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('1');
        lcd.setCursor(6,1);
        lcd.print("***");
        x = x+1;
      }
      else if (data == '2'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('2');
        lcd.setCursor(6,1);
        lcd.print("***");
        x = x+1;
    }
      else if (data == '3'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('3');
        lcd.setCursor(6,1);
        lcd.print("***");
        x = x+1;
    }
      else if (data == '4'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('4');
        lcd.setCursor(6,1);
        lcd.print("***");
        x = x+1;
    }
      else if (data == '5'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('5');
        lcd.setCursor(6,1);
        lcd.print("***");
        x = x+1;
    }
  }
    else if (x == 3) {
      if (data == '0'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('0');
        lcd.setCursor(6,1);
        lcd.print("****");
        x = x+1;
      }
      else if (data == '1'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('1');
        lcd.setCursor(6,1);
        lcd.print("****");
        x = x+1;
      }
      else if (data == '2'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('2');
        lcd.setCursor(6,1);
        lcd.print("****");
        x = x+1;
    }
      else if (data == '3'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('3');
        lcd.setCursor(6,1);
        lcd.print("****");
        x = x+1;
    }
      else if (data == '4'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('4');
        lcd.setCursor(6,1);
        lcd.print("****");
        x = x+1;
    }
      else if (data == '5'){
        lcd.clear();
        lcd.setCursor(6,0);
        lcd.print('5');
        lcd.setCursor(6,1);
        lcd.print("****");
        x = x+1;
    }
  }
  else if (x == 4){
    if (data == '6'){
      //Here green light will be on and servo will also work here 
      digitalWrite(led1, HIGH);
      digitalWrite(led2, LOW);
      digitalWrite(led3, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
      lcd.clear();
      lcd.print("Access Granted");
      //Servo will be given a high command for 3 seconds and after that it comes back to its original position
      servo1.write(90);
      delay(3000);
      servo1.write(180);
    }
    else if (data == '7'){
      //Here red light will be on and servo will not work here
      digitalWrite(led1, LOW);
      digitalWrite(led2, HIGH);
      digitalWrite(led3, LOW);
      digitalWrite(LED_BUILTIN, LOW);
      lcd.clear();
      lcd.print("Wrong Passcode");
    }
   }
  }
}
