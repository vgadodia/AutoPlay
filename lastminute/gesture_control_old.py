import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import spotipy
import sys
import os
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth = "BQCrk2d5dbG5SYD8lTikUpgnID2QR-diQo2Lfooifc8rfqUYVP6E0fMycnY00CrCJWxXRTYCaRTjvu1RuefOoEcodszK_E_TUoJ7fhITiFWyZU6KhTVr2GChf3-33-CyUSbBC0BVZMsACVcmbzmuCPN2Ol_mg0kzT-6DNDk3zh-3vusZQnCNc5yw5dDymco9k3kkM21FpFrz5-fbsoVMH1lqpeMj9btlY9DT3R4gAKJGi8VUiRS-mO_gqpZp-ftjjrpD9jwMKyV9BDrh7eq0EYCoVYWbUBiXz7G_", auth_manager=SpotifyClientCredentials(client_id="fad87bdadeee4f18951a371b520b9cec", client_secret="1aae5a1dec8f4eca8a14ae055406acd6"))



np.set_printoptions(suppress=True)

model = tensorflow.keras.models.load_model('keras_model.h5')


# image = Image.open('test_photo.jpg')


vid = cv2.VideoCapture(0) 

while(True): 

    ret, frame = vid.read()
    image = cv2.resize(frame, (224, 224))
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # size = (224, 224)
    # image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    # print(prediction)
    print(prediction[0][0])
    print(prediction[0][1])
    print(prediction[0][2])
    print(prediction[0][3])
    print(prediction[0][4])
    print(prediction[0][5])
    print (("---------------------------------------------------------------"))

    if prediction[0][0] > 0.8:
        currvol = 0
        os.system ("SetVol "+ str(currvol))

    if prediction[0][1] > 0.8:
        currvol = 100
        os.system ("SetVol "+ str(currvol))

    if prediction[0][2] > 0.8:
        spotify.next_track()

    if prediction[0][3] > 0.8:
        spotify.start_playback()

    if prediction[0][4] > 0.8:
        spotify.pause_playback()

    if prediction[0][5] > 0.8:
        currvol = 50
        os.system ("SetVol "+ str(currvol))



    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
vid.release() 
cv2.destroyAllWindows()  