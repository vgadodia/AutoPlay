
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QRadioButton, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore 
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from pymongo import MongoClient
from pymongo.collection import ObjectId
import bcrypt
import math
import json
import geocoder
import requests

client = MongoClient("mongodb+srv://user:pwd@cluster0.x4ft0.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = client.get_database("data")
db.managers.update_one({"email":"vgjunk24@gmail.com"}, {"$set":{"songs":[]}})

g_genre = 2
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth = "BQCBB9VeZbymYFxYRLkydQ0uv5VgLXA60pnrhHJpIomlO1IIvtZGVs1-4bBU8fSUeffK1yFRMXu4l6JR1usVkf7HOTAVfFyhEoLqmvYbTzJw9XF5_St-2ED9F5of3UZYpDs8nHBoVhQBrevp3hVQ1NyNdPNbuHQ9ZaqxWh3iNZdxIixU15rjjg_E9b_bfHTddaf5m8ugdFfUNrnzhYwzG1Xy_QDOXk63Sa7OiRxsRdIZjP9SR7zkEqY1xoR8TwP3E0KU2c9wzBV_pihjgewijd0pVW0VUUHavzu_", auth_manager=SpotifyClientCredentials(client_id="fad87bdadeee4f18951a371b520b9cec", client_secret="1aae5a1dec8f4eca8a14ae055406acd6"))

# https://accounts.spotify.com/authorize?response_type=code&client_id=fad87bdadeee4f18951a371b520b9cec&scope=ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing streaming app-remote-control user-read-email user-read-private playlist-read-collaborative playlist-modify-public playlist-read-private playlist-modify-private user-library-modify user-library-read user-top-read user-read-playback-position user-read-recently-played user-follow-read user-follow-modify
#print(spotify.pause_playback)

def get_genre(artist):
    k = spotify.artist(artist)["genres"]
    final = ""
    for i in k:
        final += i + " "
    final = final.lower()
    genres =[]
    if "hip" in final:
        genres.append("hip-hop")
    if "rock" in final or "metal" in final:
        genres.append("Rock")
    if "pop" in final:
        genres.append("Pop")
    if "dance" in final:
        genres.append("Dance")
    if "country" in final:
        genres.append("Country")
    return genres


def get_songs(id, genre):
    results = spotify.user_playlists(user = id)
    ids = []
    for i in results["items"]:
        ids.append(i["id"])
    songs = []
    artists = []
    for j in ids:
        
        for k in spotify.playlist(j)["tracks"]["items"]:
            songs.append(k["track"]["id"])
            artists.append(get_genre(k["track"]["album"]["artists"][0]["id"]))
    
    final = []
    for i in range(0, len(artists)):
        if genre in artists[i]:
            final.append(songs[i])
    
    return final

def get_final(email, genre, lat, lon):

    x = db.managers.find_one({"email":email})
    ff = x["songs"]
    final = []
    for i in db.users.find():
        # if math.sqrt(((i["lat"] - lat) ** 2) + ((i["lon"] - lon) ** 2)) * 1110 <= 1:
        if True:
            final += get_songs(i["spotify"], genre)
            db.users.update_one({"email":i["email"]}, {"$set":{"manager":email}})

    d = {"5HNCy40Ni5BZJFw1TKzRsC":0}
    for i in final:
        if i in x["songs"]:
            continue
        else:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

    finalfinal = "5HNCy40Ni5BZJFw1TKzRsC"

    for i in d:
        if d[finalfinal] < d[i]:
            finalfinal = i

    ff.append(finalfinal)
    db.managers.update_one({"email":email}, {"$set":{"songs":ff}})
    return finalfinal

# print(get_final("vgjunk24@gmail.com", "Rock", 17.3968, 78.4935))
# print(get_final("vgjunk24@gmail.com", "Rock", 28.063219, -80.62389))

class Worker(QObject):

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)

    countChanged = pyqtSignal(list)

    def do_work(self):
        global g_genre
        while True:

            try:
                all_g = ["Pop", "hip-hip", "Rock", "Pop", "Country", "Dance"]
                genre = all_g[g_genre]
                location = geocoder.ip('me').latlng
                song_id = get_final("vgjunk24@gmail.com", genre, location[0], location[1])
                song = spotify.track(song_id)
                print(song_id)
                spotify.add_to_queue(song_id)
                self.countChanged.emit([song["name"], song["album"]["artists"][0]["name"]])
            except:
                print(g_genre)
                self.countChanged.emit(["Song unavailable", "No Songs matched that genre."])
            QThread.sleep(10)
            


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5'
        self.width = 800
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, 800, 480)

        self.loginText = QLabel('<h1>Dashboard</h1>', self)
        self.loginText.move(330, 40)
        self.loginText.setFixedWidth(300)

        self.genreText = QLabel('<p>Genre:</p>', self)
        self.languageText = QLabel('<p>Language:</p>', self)

        self.genreText.move(300, 100)
        self.languageText.move(440, 100)

        self.button = QComboBox(self)
        self.button.move(270, 130)
        self.button.addItem("AI detect")
        self.button.addItem("hip-hop")
        self.button.addItem("Rock")
        self.button.addItem("Pop")
        self.button.addItem("Country")
        self.button.addItem("Dance")

        self.button2 = QComboBox(self)
        self.button2.move(425, 130)
        self.button2.addItem("English")
        self.button2.addItem("Spanish")
        self.button2.addItem("French")

        self.generate = QPushButton("Generate!", self)
        self.generate.move(350, 190)

        self.songName = QLabel('<h1>No Song Playing</h1>', self)
        self.songName.move(255, 280)
        self.songName.setFixedWidth(300)
        self.songName.setAlignment(QtCore.Qt.AlignCenter)

        self.singer = QLabel('<p>Hit Generate to start.</p>', self)
        self.singer.move(360, 310)
        self.singer.setFixedWidth(300)

        self.playpause = QPushButton("Play", self)
        self.playpause.move(300, 380)

        self.nexttrack = QPushButton("Next", self)
        self.nexttrack.move(400, 380)
    

        

        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.generate.clicked.connect(self.on_click)
        self.playpause.clicked.connect(self.play_pause)
        self.nexttrack.clicked.connect(self.nexttrack_function)
        self.worker.countChanged.connect(self.update_text)
        self.thread.started.connect(self.worker.do_work) # when thread starts, start worker
        

        self.show()
    
    def on_click(self):
        global g_genre
        g_genre = self.button.currentIndex()
        self.thread.start()
   
    def update_text(self, song):
        self.songName.setText("<h1>" + song[0] + "</h1>") 
        self.singer.setText(song[1])
    
    def nexttrack_function(self):
        spotify.next_track()
    
    def play_pause(self):
        if self.playpause.text() == "Play":
            self.playpause.setText("Pause")
            spotify.start_playback()
            #self.thread.start()
        else:
            self.playpause.setText("Play")
            spotify.pause_playback()
            #self.worker.disconnect()
            #self.thread.terminate()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(30, 30, 30))
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.Base, QColor(53, 53, 53))
    palette.setColor(QPalette.AlternateBase, QColor(30, 30, 30))
    palette.setColor(QPalette.ToolTipBase, QColor(0, 0, 0))
    palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
    palette.setColor(QPalette.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.BrightText, QColor(255, 255, 255))
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)
    ex = App()
    sys.exit(app.exec_())