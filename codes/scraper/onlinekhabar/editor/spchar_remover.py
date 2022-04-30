import csv
import re
spchar=['(' , ')' , '÷' , ',' , '-' , '“' , '”' , '‘' , '’']
count=0
for i in range(1,10):
    with open(f"ok{i}.csv",'rt',encoding='utf-8') as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)
        for rows in csvreader:
            news=""
            title=""
            for char in rows[1]:
                if char not in spchar:
                    title+=char
            for char in rows[2]:
                if char not in spchar:
                    news+=char
            rows[1]=title
            rows[2]=news
            with open(f"original/ok{i}.csv",'a',encoding='utf-8') as csvfile1:
                csvwriter=csv.writer(csvfile1, delimiter=',' , quotechar="'", quoting=csv.QUOTE_ALL,lineterminator='\n' )
                csvwriter.writerow(rows)