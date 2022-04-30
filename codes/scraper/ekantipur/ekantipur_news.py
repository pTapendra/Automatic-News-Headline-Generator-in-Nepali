import csv
from bs4 import BeautifulSoup
import requests

def extractnews(link):
    article=[]
    response=requests.get(link)
    soup=BeautifulSoup(response.content,'lxml')

    #for title
    try:
        header=soup.find("div",class_="article-header")
        title=header.find("h1").text
        article.append(title)

    # for news
        div=soup.find("div",class_="description current-news-block")
        news=' '
        for each_paragraph in div.find_all("p"):
            news += each_paragraph.text 
        article.append(news)
    
    except:
        return []

    else:
        return article


def writetofile(text):
    with open("national1.csv", 'a', encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL, lineterminator='\n')
        csvwriter.writerow(text)
 

links = open("national1.txt",'r').read().splitlines()
for link in links:
    news=extractnews(link)
    writetofile(news)

    
