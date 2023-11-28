import requests
from bs4 import BeautifulSoup
import re

url = "https://sports.news.naver.com/news?oid=139&aid=0002168397"

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'text/html; charset=utf-8'
}

req = requests.get(url, headers=headers)
results = re.search(r"[\w\.-]+@[\w\.-]+", req.text)[0] #첫번째값을 오브젝트 형식으로
print(results)


matches = re.findall(r"[\w\.-]+@[\w\.-]+", req.text) #전체
print(set(matches)) #set으로 중복제거