from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib

def get_data(nickname):
    nickname = urllib.parse.quote(nickname)
    html = urlopen("https://maple.gg/u/" + nickname)
    bsObject = BeautifulSoup(html, "html.parser")
    user_info = str(bsObject.select('#character-card'))

    return user_info