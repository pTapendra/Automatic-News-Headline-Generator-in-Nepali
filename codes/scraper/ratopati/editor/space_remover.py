import csv
import re
for j in range(1,8):
    with open(f"news{j}.csv",'rt',encoding='utf-8') as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)
        for rows in csvreader:
            news=re.sub("\s\s+" , " ", rows[1])
            rows[1]=news
            with open(f"ratopati/news{j}.csv",'a',encoding='utf-8') as csvfile1:
                csvwriter=csv.writer(csvfile1, delimiter=',' , quotechar="'", quoting=csv.QUOTE_ALL,lineterminator='\n' )
                csvwriter.writerow(rows)