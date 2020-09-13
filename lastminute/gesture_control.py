import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import spotipy
import sys
import os
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth = "BQCBB9VeZbymYFxYRLkydQ0uv5VgLXA60pnrhHJpIomlO1IIvtZGVs1-4bBU8fSUeffK1yFRMXu4l6JR1usVkf7HOTAVfFyhEoLqmvYbTzJw9XF5_St-2ED9F5of3UZYpDs8nHBoVhQBrevp3hVQ1NyNdPNbuHQ9ZaqxWh3iNZdxIixU15rjjg_E9b_bfHTddaf5m8ugdFfUNrnzhYwzG1Xy_QDOXk63Sa7OiRxsRdIZjP9SR7zkEqY1xoR8TwP3E0KU2c9wzBV_pihjgewijd0pVW0VUUHavzu_", auth_manager=SpotifyClientCredentials(client_id="fad87bdadeee4f18951a371b520b9cec", client_secret="1aae5a1dec8f4eca8a14ae055406acd6"))



np.set_printoptions(suppress=True)

model = tensorflow.keras.models.load_model('keras_model.h5')


# image = Image.open('test_photo.jpg')


vid = cv2.VideoCapture(0) 

classes = ["pause", "Play", "volume up", "Next Track", "volume down", "Medium Volume"]

while(True): 
      
    ret, frame = vid.read()
    image = cv2.resize(frame, (224, 224))
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # size = (224, 224)
    # image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = list(model.predict(data)[0])
    pred_index = prediction.index(max(prediction))

    print(classes[pred_index])
    print (("---------------------------------------------------------------"))

    if pred_index == 4:
        currvol = 0
        os.system ("SetVol "+ str(currvol))
    
    if pred_index == 2:
        currvol = 100
        os.system ("SetVol "+ str(currvol))

    if pred_index == 3:
        spotify.next_track()
    
    if pred_index == 1:
        spotify.start_playback()
    
    if pred_index == 0:
        spotify.pause_playback()
    
    if pred_index == 5:
        currvol = 50
        os.system ("SetVol "+ str(currvol))



    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
vid.release() 
cv2.destroyAllWindows() 