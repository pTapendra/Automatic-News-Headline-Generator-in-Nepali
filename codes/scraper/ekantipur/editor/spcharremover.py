import csv
import re
spchar=['(' , ')' , '÷' , ',' , '-' , '“' , '”' , '‘' , '’' , '"',"''"]
count=0
for i in range(0,10):
    with open(f"national{i}.csv",'rt',encoding='utf-8') as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)
        for rows in csvreader:
            news=""
            title=""
            for char in rows[0]:
                if char not in spchar:
                    title+=char
            for char in rows[1]:
                if char not in spchar:
                    news+=char

            rows[0]=title
            rows[1]=news
            with open(f"original/national{i}.csv",'a',encoding='utf-8') as csvfile1:
                csvwriter=csv.writer(csvfile1, delimiter=',' , quotechar="'", quoting=csv.QUOTE_ALL,lineterminator='\n' )
                csvwriter.writerow(rows)