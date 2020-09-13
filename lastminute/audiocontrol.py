import speech_recognition as sr
import os

from pymongo import MongoClient
from pymongo.collection import ObjectId
import bcrypt
import math
import json
import geocoder
import requests

import pyttsx3
engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

currvol = 50

os.system ("SetVol "+ str(currvol))


client = MongoClient("mongodb+srv://user:pwd@cluster0.x4ft0.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = client.get_database("data")
db.managers.update_one({"email":"vgjunk24@gmail.com"}, {"$set":{"songs":[]}})

g_genre = 2
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth = "BQCBB9VeZbymYFxYRLkydQ0uv5VgLXA60pnrhHJpIomlO1IIvtZGVs1-4bBU8fSUeffK1yFRMXu4l6JR1usVkf7HOTAVfFyhEoLqmvYbTzJw9XF5_St-2ED9F5of3UZYpDs8nHBoVhQBrevp3hVQ1NyNdPNbuHQ9ZaqxWh3iNZdxIixU15rjjg_E9b_bfHTddaf5m8ugdFfUNrnzhYwzG1Xy_QDOXk63Sa7OiRxsRdIZjP9SR7zkEqY1xoR8TwP3E0KU2c9wzBV_pihjgewijd0pVW0VUUHavzu_", auth_manager=SpotifyClientCredentials(client_id="fad87bdadeee4f18951a371b520b9cec", client_secret="1aae5a1dec8f4eca8a14ae055406acd6"))



# obtain audio from the microphone
r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Voice Interface Active!")
#     audio = r.listen(source)

# # recognize speech using Sphinx
# try:
#     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))


while True:
    # recognize speech using Google Speech Recognition
    with sr.Microphone() as source:
        print("Voice Interface Active!")
        audio = r.listen(source)
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = ""
        text = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + text)

        text = text.lower()

        print (text)

        if "volume" in text and "low" in text:
            engine.say("lowering volume")
            engine.runAndWait()
            if currvol >20:
                currvol = currvol - 20
            else:
                currvol = 0

            os.system ("SetVol "+ str(currvol))
            continue

        if "volume" in text and "high" in text:
            engine.say("raising volume")
            engine.runAndWait()
            currvol = currvol + 20
            os.system ("SetVol "+ str(currvol))
            continue

        if "volume" in text and "max" in text:
            engine.say("max volume")
            engine.runAndWait()
            currvol = 100
            os.system ("SetVol "+ str(currvol))
            continue

        if "volume" in text and "mid" in text:
            engine.say("medium volume")
            engine.runAndWait()
            currvol = 50
            os.system ("SetVol "+ str(currvol))
            continue
        
        if "volume" in text and "mute" in text:
            engine.say("muting")
            engine.runAndWait()
            currvol = 0
            os.system ("SetVol "+ str(currvol))
            continue

        if "next" in text:
            engine.say("playing next track")
            engine.runAndWait()
            spotify.next_track()
            continue


        if "play" in text:
            engine.say("playing track")
            engine.runAndWait()
            spotify.start_playback()
            continue

        if "pause" in text or "stop" in text:
            engine.say("playback halted")
            engine.runAndWait()
            spotify.pause_playback()
            continue

        if "quit" in text or "exit" in text:
            engine.say("exiting voice control interface")
            engine.runAndWait()
            break


        # control here



    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    

