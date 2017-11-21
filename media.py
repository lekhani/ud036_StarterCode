import webbrowser
import os
import time


class Movie():
    """ This class saved information on movies"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
        
    def show_trailer(self):
# chrome_path is to explicitly use Google Chrome as web browser     
         chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
         webbrowser.get(chrome_path).open(self.trailer_youtube_url)
#comment above two lines and uncomment below 1 line to use system default browser
#        webbrowser.open(self.trailer_youtube_url)
# time.sleep(<sec>) used for waiting certain seconds before executing next command       
#         time.sleep(10)
#         os.system("taskkill /im chrome.exe /f")

