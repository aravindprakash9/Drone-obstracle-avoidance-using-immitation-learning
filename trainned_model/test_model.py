import numpy as np
# from grabscreen import grab_screen
from PIL import ImageGrab
import cv2
import time
# from directkeys import PressKey, ReleaseKey, I, J, K, L
from pynput.keyboard import Key, Controller
from tensorflow.keras.models import load_model
import random

WIDTH = 80
HEIGHT = 60
LR = 1e-3
EPOCHS = 80
MODEL_NAME = 'OBSAvoid-0.01-alexnetv2-60-epochs.model'

i = [1, 0, 0, 0]
j = [0, 1, 0, 0]
k = [0, 0, 1, 0]
l = [0, 0, 0, 1]
keyboard = Controller()

def straight():
    keyboard.press('i')
    keyboard.release('j')
    keyboard.release('k')
    keyboard.release('l')

def left():
    keyboard.press('j')
    keyboard.release('i')
    keyboard.release('k')
    keyboard.release('l')

def right():
    keyboard.press('l')
    keyboard.release('j')
    keyboard.release('k')
    keyboard.release('i')

def reverse():
    keyboard.press('k')
    keyboard.release('j')
    keyboard.release('i')
    keyboard.release('l')

# Load the pre-trained model
model = load_model(MODEL_NAME)

def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    paused = False
    while True:
        if not paused:
            # 800x600 windowed mode
            # screen = grab_screen(region=(0, 40, 800, 640))
            screen = np.array(ImageGrab.grab(bbox=(80, 170, 600, 550)))
            cv2.imshow("Image", screen)
            cv2.waitKey(1)
            # print('loop took {} seconds'.format(time.time() - last_time))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (WIDTH, HEIGHT))

            prediction = model.predict([screen.reshape(1, WIDTH, HEIGHT, 1)])[0]
            print(prediction)

            if np.argmax(prediction) == np.argmax(i):
                straight()
            elif np.argmax(prediction) == np.argmax(k):
                reverse()
            elif np.argmax(prediction) == np.argmax(j):
                left()
            elif np.argmax(prediction) == np.argmax(l):
                right()












        # keys = key_check()

        # # p pauses game and can get annoying.
        # if 'T' in keys:
        #     if paused:
        #         paused = False
        #         time.sleep(1)
        #     else:
        #         paused = True
        #         ReleaseKey(A)
        #         ReleaseKey(W)
        #         ReleaseKey(D)
        #         time.sleep(1)

main()
