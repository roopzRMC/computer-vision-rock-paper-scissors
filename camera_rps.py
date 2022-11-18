# %%
import cv2
from keras.models import load_model
import numpy as np
import time

label_list = ['rock', 'paper', 'scissors', 'nothing']

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
# %%
get_prediction(5)
# %%