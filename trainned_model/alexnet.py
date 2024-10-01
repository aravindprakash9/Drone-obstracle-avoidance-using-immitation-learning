import tensorflow as tf
from tensorflow.keras import layers, models

def alexnet2(width, height, lr, output=3):
    model = models.Sequential()

    model.add(layers.Conv2D(96, (11, 11), strides=(4, 4), activation='relu', padding='same', input_shape=(width, height, 1)))
    model.add(layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same'))
    model.add(layers.BatchNormalization())

    model.add(layers.Conv2D(256, (5, 5), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same'))
    model.add(layers.BatchNormalization())

    model.add(layers.Conv2D(384, (3, 3), activation='relu', padding='same'))
    model.add(layers.Conv2D(384, (3, 3), activation='relu', padding='same'))
    model.add(layers.Conv2D(256, (3, 3), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same'))
    model.add(layers.BatchNormalization())

    model.add(layers.Flatten())
    model.add(layers.Dense(4096, activation='tanh'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(4096, activation='tanh'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(4096, activation='tanh'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(output, activation='softmax'))

    model.compile(optimizer=tf.keras.optimizers.SGD(lr=lr, momentum=0.9),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model
