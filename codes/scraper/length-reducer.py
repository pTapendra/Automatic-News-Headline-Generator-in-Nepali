#coding=utf8
import random
import numpy as np
def totalchar(list):
    sum=0
    for sentence in list:
        sum+=len(sentence)
    return sum

def delist(list):
    news=""
    for e in list:
        for char in e:
            news+=char
    return news
terminate=['।', '!', '?']

#long news here
paragraph=""

new_paragraph=""
for char in paragraph:
    if char != '\n':
        new_paragraph+=char

paragraph=new_paragraph

print(len(paragraph))
new_para=[]
news_list=[]
news=""
for char in paragraph:
    news+=char
    if char in terminate:
        news_list.append(news)
        news=""

while True and len(news_list)>5 and len(paragraph)>800:
    l=len(news_list)
    rdm=random.randint(1, l)
    if l==rdm:
        rdm-=1
    del news_list[rdm]
    length=totalchar(news_list)
    if length>=500 and length <= int(np.random.normal(loc=800, scale=50, size=1)):
        break
if len(news_list)>5:
    new_para=delist(news_list)

#result
print(new_para)