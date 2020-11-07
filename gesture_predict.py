#Importing required libraries
import numpy as np
from keras.models import model_from_json
import operator
import cv2
import sys, os
import serial
import time

#Initializing the serial port
port = serial.Serial('COM3', 9600)

#Loading the trained model
json_file = open("model-bw.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)

loaded_model.load_weights("model-bw.h5")
print("loaded model from disk")
#Initializing the passcode
passcode = "3512"
#Initializing some variables
a = ""
pred = ""

#Capturing live video from the front camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    #creating region of interest
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1] - 10
    y2 = int(0.65*frame.shape[1])

    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0), 1)
    roi = frame[y1:y2, x1:x2]
    cv2.imshow("frame", frame)

    #According to the dataset, the region of interest part is converted
    roi = cv2.resize(roi, (64,64))
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("test", test_image)
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:
        break
    elif interrupt & 0xFF == ord('n'):
        #The converted part of region of interest which is the test_image here is applied to the model to make predictions
        result = loaded_model.predict(test_image.reshape(1,64,64,1))
        prediction = {'0': result[0][0],
                      '1': result[0][1],
                      '2': result[0][2],
                      '3': result[0][3],
                      '4': result[0][4],
                      '5': result[0][5],
                    'NAN': result[0][6]}

        prediction = sorted(prediction.items(), key = operator.itemgetter(1), reverse = True)

        #Now we store the predicted data and send it to the arduino
        pred = prediction[0][0]
        a = a + pred
        a = a.replace('NAN','')
        port.write(str.encode(pred))
        print(a)

        #Passcode check
        if len(a) == 4:
            time.sleep(3)
            if a == passcode:
                print('OPEN')
                print(a)
                port.write(str.encode('6'))
                cap.release()
                cv2.destroyAllWindows()
            else:
                print('WRONG')
                print(a)
                port.write(str.encode('7'))
                cap.release()
                cv2.destroyAllWindows()
