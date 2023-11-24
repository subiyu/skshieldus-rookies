import requests
from bs4 import BeautifulSoup

url = "https://www.malware-traffic-analysis.net/2023/index.html"

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'text/html; charset=utf-8'
}

req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "lxml")
links = soup.select("#main_content > div.content > ul > li > a.main_menu")

tmpUrl = url.split("/")[0:-1]
basicUrl = ""
for u in tmpUrl:
    basicUrl += u
    basicUrl += "/"
newFile = "new.txt"

for link in links: 
    if 'href' in link.attrs:
        href = link["href"]
        print(f"제목: {link.text} 링크: {basicUrl + str(href)}")
        with open(newFile, 'a', encoding='utf-8') as f:
            f.write(f"제목: {link.text} 링크: {basicUrl + str(href)}\n")

#tags = soup.select('a')
#print(tags)
##main_content > div.content > ul:nth-child(2) > li:nth-child(1) > a.main_menu