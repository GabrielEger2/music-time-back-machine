import sys

from ui_main import Ui_MainWindow
from ui_main import Ui_ErrorMassage
from ui_main import Ui_HowToConfigure
from ui_main import Ui_HowAddSpotify
from PySide6.QtWidgets import QApplication, QMainWindow
from bs4 import BeautifulSoup
import requests
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime


with open('AppInfo.json') as f:
    data = json.load(f)
    client_id = data['AppInfo']['ID']
    client_secret = data['AppInfo']['secret']
    website_url = data['AppInfo']['website']

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calendar_wd.selectionChanged.connect(self.calendar_date)
        self.ui.actionHow_to_Configure.triggered.connect(self.show_how_configure)
        self.ui.actionAdd_Spotify_Account.triggered.connect(self.show_how_add_spotify)
        self.ui.actionExit.triggered.connect(self.close_window)

    def calendar_date(self):
        if len(client_id) == 0 or len(client_secret) == 0 or len(website_url) == 0:
            self.show_how_configure()
            window.close()
        else:
            lock = 0
            songs_names = []
            date_selected = self.ui.calendar_wd.selectedDate()
            date = str(date_selected.toPython())
            if int(date[:4]) > 1899:
                try:
                        request = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
                        bs = BeautifulSoup(request.text, "html.parser")
                        fist_song = bs.find('h3', attrs={'class': 'c-title a-font-primary-bold-l a-font-primary-bold-m@mobile-max lrv-u-color-black u-color-white@mobile-max lrv-u-margin-r-150'})
                        songs = bs.find_all('h3', attrs={'class': 'c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only'})
                        first_song_name = fist_song.getText()
                        for song in songs:
                            songs_names.append(song.getText())
                        songs_names.insert(0, first_song_name)
                        lock = 1
                except:
                    self.show_error_massage(f"Please select a valid date: 1900/01/01 - "
                                            f"{str(str(datetime.today().year) + '-' + str(datetime.today().month) + '-' + str(datetime.today().day)).replace('-', '/')}")
            else:
                self.show_error_massage(f"Please select a valid date: 1900/01/01 - "
                                        f"{str(str(datetime.today().year) + '-' + str(datetime.today().month) + '-' + str(datetime.today().day)).replace('-', '/')}")

            if lock == 1:
                window.close()
                sp = spotipy.Spotify(
                    auth_manager = SpotifyOAuth(
                        scope = "playlist-modify-private",
                        redirect_uri = website_url,
                        client_id = client_id,
                        client_secret = client_secret,
                        show_dialog = True,
                        cache_path = "token.txt"
                    )
                )
                print("Creating Playlist... Please Don't Turn Off This Program")
                id = sp.current_user()["id"]
                uris = []
                song_number = 0
                for song in songs_names:
                    result = sp.search(q=f"track:{song}", type="track")
                    song_number += 1
                    print(f"#{song_number} song added")
                    try:
                        uri = result["tracks"]["items"][0]["uri"]
                        uris.append(uri)
                    except IndexError:
                        print(f"#{song_number} doesn't exist in Spotify. Skipped.")
                playlist = sp.user_playlist_create(user=id, name=f"Music Time Back Machine {date.replace('-', '/')}", public=False)
                print("Process Finished, Playlist Created")
                sp.playlist_add_items(playlist_id=playlist["id"], items=uris)

    def show_error_massage(self, massage):
        self.window = QMainWindow()
        self.error = Ui_ErrorMassage()
        self.error.setupUi(self.window)
        self.window.show()
        self.error.lb_em.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">{massage}</span></p></body></html>")

    def show_how_configure(self):
        self.configwindow = QMainWindow()
        self.configure = Ui_HowToConfigure()
        self.configure.setupUi(self.configwindow)
        self.configwindow.show()
        self.configure.add_info_bt.clicked.connect(self.add_info)

    def add_info(self):
        self.configwindow.close()
        client_id = str(self.configure.ID_et.text())
        client_secret = str(self.configure.US_et.text())
        website_url = str(self.configure.Website_et.text())
        new_info = {
            "AppInfo": {
                "website": website_url,
                "ID": client_id,
                "secret": client_secret
                       }
                   }
        if len(website_url) == 0 or len(client_secret) == 0 or len(client_id) == 0:
            Window.show_error_massage(self, "Please make sure you haven't left any fild empty")
        else:
            try:
                with open('Passwords.json', 'r') as f:
                    data = json.load(f)
                    data.update(new_info)
                with open('AppInfo.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4)
            except:
                with open('AppInfo.json', 'w', encoding='utf-8') as f:
                    json.dump(new_info, f, indent=4)

    def show_how_add_spotify(self):
        self.window = QMainWindow()
        self.configure = Ui_HowAddSpotify()
        self.configure.setupUi(self.window)
        self.window.show()

    def close_window(self):
        self.close()

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())