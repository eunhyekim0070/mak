from bs4 import BeautifulSoup
import requests
import sys

query = sys.argv[1]
##추가 

# if len(sys.argv) > 1:
#     query = sys.argv[1]

# else:
#     query = "default_query"

html = requests.get(f"https://search.naver.com/search.naver?where=nexearch&query={query}+날씨")
soup = BeautifulSoup(html.text, 'html.parser')

# 위치
address = soup.find('div', {'class': 'title_area _area_panel'}).find('h2', {'class' : 'title'}).text
print(address)

# 날씨 정보
weather_data = soup.find('div', {'class': 'weather_info'})
#print(weather_data)

# 현재 온도
tempertaure = weather_data.find('div', {'class': 'temperature_text'}).text.strip()[5:]
print(tempertaure)

# 날씨 상태
weather_status = weather_data.find('span', {'class': 'weather before_slash'}).text
print(weather_status)

# 공기 상태
air_status = soup.find('ul', {'class': 'today_chart_list'})
infos = air_status.find_all('li', {'class': 'item_today'})

# for info in infos:
    # print(info.text.strip())
print()
print('*' * 100)
print("\n시간대 별 날씨 정보")
weather_time = soup.find_all('li', {'class': '_li'})

for i in weather_time[:24]:
    print(i.text.strip())
