from bs4 import BeautifulSoup
from selenium import webdriver
import time

def get_cube_probability_data(grade, parts, level):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(r"C:\Users\aaaaa\Desktop\maplegg_fb\public\server\src\static\chromedriver\chromedriver.exe", options=options);
    url = "https://maplestory.nexon.com/Guide/OtherProbability/cube/black#a";
    driver.get(url);

    driver.find_element_by_xpath('//*[@id="selectGrade"]/a')
    driver.execute_script('$("#selectGrade select").val(' + grade + ')')

    driver.find_element_by_xpath('//*[@id="selectPartsType"]/a')
    driver.execute_script('$("#selectPartsType select").val(' + parts + ')')

    driver.find_element_by_xpath('//*[@id="lv"]').send_keys(level)

    driver.find_element_by_xpath('//*[@id="CubeSearchGroupArea"]/div[1]/button').click()

    time.sleep(1)
    html = driver.page_source
    bsObject = BeautifulSoup(html, "html.parser")
    data = str(bsObject.select('.cube_data'))

    return data