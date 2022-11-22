
import cv2
from keras.models import load_model
import numpy as np
import time
import random

class RockPaperScissors:

    def __init__(self):
        self.label_list = ['rock', 'paper', 'scissors', 'nothing']


    def get_prediction(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        self.user_trigger = input('press s to start')

        t=3

        while self.user_trigger != 's':
            print('please try again')
            self.user_trigger = input('press s to start')
        else:
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
                self.my_choice = self.label_list[obj_predicted]
                print(f'{self.my_choice}')
                t -= 1
                
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        print(f' you chose {self.my_choice}')
        return self.my_choice

    def computer_play(self,choice_list):
        self.computer_choice = random.choice(choice_list)
        print(f' I chose {self.computer_choice}')
        return self.computer_choice


    def play_the_game(self):
        self.user_wins = 0
        self.computer_wins = 0

        rps_list = ['rock', 'paper', 'scissors']

        while (self.user_wins < 3) and (self.computer_wins < 3):
            
            self.my_choice = self.get_prediction()
            self.computer_choice = self.computer_play(rps_list)

            print(f'\n Computer plays {self.computer_choice}')
            print(f'\n User plays {self.my_choice}')

            if self.computer_choice == self.my_choice:
                print('its a tie')
            elif self.computer_choice == 'rock' and self.my_choice == 'paper':
                print('user wins')
                self.user_wins +=1
            elif self.computer_choice == 'rock' and self.my_choice == 'scissors':
                print('computer wins')
                self.computer_wins +=1
            elif self.computer_choice == 'paper' and self.my_choice == 'scissors':
                print('user wins')
                self.user_wins +=1
            elif self.my_choice == 'rock' and self.computer_choice == 'paper':
                print('computer wins')
                self.computer_wins +=1
            elif self.my_choice == 'rock' and self.computer_choice == 'scissors':
                print('user wins')
                self.user_wins +=1
            elif self.my_choice == 'paper' and self.computer_choice == 'scissors':
                print('computer wins')
                self.computer_wins += 1
        else:
            if self.computer_wins > self.user_wins:
                print(f'computer wins with score {self.computer_wins} to {self.user_wins}')
            else:
                print(f'user wins with score {self.user_wins} to {self.computer_wins}')


mygame = RockPaperScissors()
mygame.play_the_game()
# %%
