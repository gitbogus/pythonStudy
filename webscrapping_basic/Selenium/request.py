import requests
from bs4 import BeautifulSoup

# Naver 서버에 대화를 시도
response = requests.get("https://ucloud.lgcns.com/vmCube/Login")
# html 번역 선생님
html = response.text
soup = BeautifulSoup(html, 'html.parser')
# id 값이 NM_set_home_btn
word = soup.select_one('#NM_set_home_btn')
print(word)