from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import json


def get_food_information(urls,SCROLL_PAUSE_TIME,URL_length, FILE_NAME):
    BASE_URL = 'https://www.mangoplate.com/'
    count = 0
    for url in urls:
        count += 1
        if count <= URL_length:
        address = 'chromedriver.exe'
        driver = webdriver.Chrome(address)
        driver.get(url)
        while True:
            try:
                #더보기 버튼 클릭
                driver.find_element_by_css_selector(
                    "#div_list_more").click()
                # 몇 초 대기
                time.sleep(SCROLL_PAUSE_TIME)
                #스크롤 아래로
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
            except:
                #더보기 버튼 없을 때 while문 끝
                break

            # 1.음식점명 2.대표메뉴 3. 식당 키워드 4. 지역정보(주소) 5. 평점
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        li_list = soup.find("ul", attrs={"id":"div_list"}).find_all('li')
        for list in li_list:
        # onouseenter의 속성이 있는 것만 정보가 들어있는 태그
            if list.has_attr('onmouseenter'):
            #음식점 정보
            url_tag = list.find('a', attrs={"class": "blink"})
            url = f'{BASE_URL}{url_tag["href"]}'
            img_url = list.find("span", attrs={"class":"img"})[
                'style'
            ]
            url_img = img_url.split(
                "background:url('")[1].split("no-repeat")[0][:-3]
            name= list.find(
                "span", attrs={"class": "btxt"}).text.split(".")[1]
            best_menu = list.find("span", attrs={"class":"stxt"}).text
            key_word = list.find_all(
                "span", attrs={"class":"ctxt"})[0].text
            loc_list = list.find_all(
                "span", attrs={"class":"ctxt"}}[1]
            for loc in loc_list:
                if len(loc) < 5:
                    loc_dong = loc.text
                else:
                    loc_address=loc.text
                    lat, lon= getLatLng(loc_address)
                    time.sleep(1)

            #평점에 대한정보
            p_list= list.find_all(
                "p", attrs={"class":"favor-review"})
            for list in p_list:
                score= int(list.find("span", attrs={
                        "class":"point"}).text[0:2])
            print(score,url, name, best_menu,
                  key_word, loc_dong, loc_address,lat, lon,url_image)
           
           