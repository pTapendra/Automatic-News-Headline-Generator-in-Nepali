import csv
with open("ekantipur/final/news.csv",'rt',encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)
    for row in csvreader:
        with open(f"final/news.csv",'a',encoding='utf-8') as csvfile1:
                    csvwriter=csv.writer(csvfile1, delimiter=',' , quotechar="'", quoting=csv.QUOTE_ALL,lineterminator='\n' )
                    csvwriter.writerow(row)


with open(f"onlinekhabar/final/news.csv",'rt',encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)
    for row in csvreader:
        with open(f"final/news.csv",'a',encoding='utf-8') as csvfile1:
                    csvwriter=csv.writer(csvfile1, delimiter=',' , quotechar="'", quoting=csv.QUOTE_ALL,lineterminator='\n' )
                    csvwriter.writerow(row)

with open(f"ratopati/final/news.csv",'rt',encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)
    for row in csvreader:
        with open(f"final/news.csv",'a',encoding='utf-8') as csvfile1:
                    csvwriter=csv.writer(csvfile1, delimiter=',' , quotechar="'", quoting=csv.QUOTE_ALL,lineterminator='\n' )
                    csvwriter.writerow(row)

    
    