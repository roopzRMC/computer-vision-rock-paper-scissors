
import cv2
from keras.models import load_model
import numpy as np
import time
import random

def get_prediction(t):
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    label_list = ['rock', 'paper', 'scissors', 'nothing']

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        obj_predicted = np.argmax(prediction)
        cv2.imshow('frame', frame)
        print(label_list[obj_predicted])
        t -= 1
            
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    print(f' you chose {label_list[obj_predicted]}')
    return label_list[obj_predicted]

def computer_play(choice_list):
    computer_choice = random.choice(choice_list)
    print(f' I chose {computer_choice}')
    return computer_choice


def play_the_game():
    user_wins = 0
    computer_wins = 0

    rps_list = ['rock', 'paper', 'scissors']

    while (user_wins < 3) and (computer_wins < 3):
        computer_choice = computer_play(rps_list)
        my_choice = get_prediction(5)

        #print(f'Computer plays {computer_choice}')
        #print(f'User plays {my_choice}')

        if computer_choice == my_choice:
            print('its a tie')
        elif computer_choice == 'rock' and my_choice == 'paper':
            print('user wins')
            user_wins +=1
        elif computer_choice == 'rock' and my_choice == 'scissors':
            print('computer wins')
            computer_wins +=1
        elif computer_choice == 'paper' and my_choice == 'scissors':
            print('user wins')
            user_wins +=1
        elif my_choice == 'rock' and computer_choice == 'paper':
            print('computer wins')
            computer_wins +=1
        elif my_choice == 'rock' and computer_choice == 'scissors':
            print('user wins')
            user_wins +=1
        elif my_choice == 'paper' and computer_choice == 'scissors':
            print('computer wins')
            computer_wins += 1
    else:
        if computer_wins > user_wins:
            print(f'computer wins with score {computer_wins} to {user_wins}')
        else:
            print(f'user wins with score {user_wins} to {computer_wins}')


play_the_game()