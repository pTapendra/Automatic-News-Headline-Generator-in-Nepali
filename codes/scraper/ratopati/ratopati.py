from bs4 import BeautifulSoup
import requests
file=open("news.txt",'a')
for i in range(1,1000):

    http="https://www.ratopati.com/category/news?page=" + str(i)

    response=requests.get(http)
    soup=BeautifulSoup(response.content,'lxml')
    news=soup.find_all("div",class_="item")
    for each_news in news:
        link=each_news.find('a',href=True).get('href')
        link="https://www.ratopati.com"+link
        file.write(link)
        file.write("\n")
