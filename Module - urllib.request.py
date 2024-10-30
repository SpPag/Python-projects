"""
Example of its use as seen in a video by thenewboston.
"""
import random
import urllib.request


def download_web_image(url):
    name = str(random.randrange(1, 1000)) + ".jpg"
    urllib.request.urlretrieve(url, name)
    print(f"Saved image as {name}")


download_web_image("https://www.shutterstock.com/shutterstock/photos/2321043999/display_1500/stock-vector-luffy-hat-and-straw-hat-one-piece-pirate-anime-face-wallpaper-2321043999.jpg")