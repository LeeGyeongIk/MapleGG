from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib

# def get_data(nickname):
#     nickname = urllib.parse.quote(nickname)
#     html = urlopen("https://maplestory.nexon.com/Guide/OtherProbability/cube/red#a")
#     bsObject = BeautifulSoup(html, "html.parser")
#     user_info = str(bsObject.select('#character-card'))

#     return user_info

# print(get_data("설백홍"))