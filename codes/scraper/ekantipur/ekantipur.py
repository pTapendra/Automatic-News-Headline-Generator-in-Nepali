from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome(executable_path=r"E:\seleniumdrivers\chromedriver.exe")

#ekantipur link
driver.get("https://ekantipur.com/news")

count=0
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        continue
    count+=1
    print(count)
    if count==500:
        break

link = driver.page_source
soup = BeautifulSoup(link,features='lxml')
file = open('ent.txt','a')
news=soup.find_all("article",class_='normal')
for each_news in news:
    link=each_news.find('a',href=True).get('href')
    file.write(link)
    file.write('\n')



