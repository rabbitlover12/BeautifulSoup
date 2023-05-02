import datetime
import urllib
from bs4 import BeautifulSoup
import urllib.request as req
import ssl
import requests

# now = datetime.datetime.now()
# nowDate = now.strftime('%Y년 %ㅡ월 %d일 %H시 %M분 입니다.') 

context = ssl._create_unverified_context()

webpage = urllib.request.urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=4&acq=%EC%A7%84%EC%A3%BC+%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EC%A7%84%EC%A3%BC+%EB%82%A0%EC%94%A8")
soup = BeautifulSoup(webpage, "html.parser")
# print(soup)

# temps = soup.find_all('div', 'temperature_text')
# print(temps) 

dl_summary = soup.find('dl', 'summary_list')
print(dl_summary)
print(dl_summary.text.strip())

