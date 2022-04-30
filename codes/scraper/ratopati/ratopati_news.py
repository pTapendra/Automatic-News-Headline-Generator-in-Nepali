import csv
from bs4 import BeautifulSoup
import requests

def extractnews(link):
    article=[]
    response=requests.get(link)
    soup=BeautifulSoup(response.content,'lxml')

    #for title
    try:
        header=soup.find("div",class_="article-head")
        title=header.find('h1').text
        article.append(title)

    # for news
        div=soup.find("div",itemprop="mainEntityOfPage")
        news=' '
        for each_paragraph in div.find_all("p"):
            news += each_paragraph.text 
        article.append(news)
    
    except:
        return []

    else:
        return article

def writetofile(text):
    with open("news7.csv", 'a', encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL, lineterminator='\n')
        csvwriter.writerow(text)
 
links = open("news7.txt",'r').read().splitlines()
for link in links:
    news=extractnews(link)
    if news:
        writetofile(news)
    print(link)
