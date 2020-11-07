#Importing required libraries
import keras
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator

#Initializing a sequential model
#Model Architecture:- (Convolution2D -> MaxPooling2D)*4 -> Flatten -> Dense -> Out
model = Sequential()

model.add(Convolution2D(32, (5,5), input_shape=(64,64,1), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Convolution2D(32, (5,5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Convolution2D(32, (3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Convolution2D(32, (3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(Dense(7, activation='softmax'))

#Compiling the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#Data Augmentation
train_datagen = ImageDataGenerator(
        rescale = 1./255,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('data/train',
                                                  target_size = (64,64),
                                                  batch_size = 5,
                                                  color_mode = 'grayscale',
                                                  class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('data/test',
                                             target_size = (64,64),
                                             batch_size = 5,
                                             color_mode = 'grayscale',
                                             class_mode = 'categorical')

#Training the model
model.fit_generator(training_set,
                    epochs = 20,
                    validation_data = test_set)

#Saving model and its weight
model_json = model.to_json()
with open("model-bw.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights('model-bw.h5')
