# Image-Recognition-Based-Passcode-Lock-Contactless-
A Deep Learning based project which is used to reduce contact with the surfaces.<br>
## Working Methodology
•	Image Recognition: - The first step is to detect the hand gesture and classify it whether it is 0,1,2,3,4 or 5.<br>
•	Transfer Data: - After predicting the digit, the output is sent to the Arduino and it get displayed on the LCD screen.<br>
•	Passcode check: - The first two steps are repeated 4 times as the passcode is of 4 digits and after that passcode is verified with the given passcode and accordingly other components will work.<br>
## Software Part of the project: -
•	Programming Language: Python, Embedded C<br>
•	Arduino IDE is used for the coding of Arduino<br>
## Electronic component used are: - 
•	Arduino UNO<br>
•	Servo motor<br>
•	16x2 LCD Screen<br>
•	I2C Module<br>
# How to do?
## Installation
Make sure that you have Python3 and Arduino IDE installed in your system.
## Copying the file
Copy all the files in the same folder.
## Train the model
Using gesture_train.py code and image data, you can train the model. Also you can add more images to the data and can then train the model.<br>
Also, the trained model and its weights are uploaded so one can skip this process also.
## Connections
Connect all the electronics components according to the code(or you can modify also).
## Upload
Then upload arduino_detect.ino code in the arduino.
## Final step
Run gesture_detect.py and make sure that you connected arduino to laptop as here laptop's camera is used to detect live images.
# You can also check out the demonstration of the project here :-
[Click Here](https://www.youtube.com/watch?v=v-XZw58QjSE&ab_channel=UTCARSHAGRAWAL)
