import csv
count=0
for i in range(1,10):
    with open(f"ok{i}.csv",'rt',encoding='utf-8') as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)
        for rows in csvreader:
            if len(rows[2])<800:
                with open(f"small/s_ok{i}.csv",'a',encoding='utf-8') as csvfile1:
                    csvwriter=csv.writer(csvfile1, delimiter=',' , quotechar="'", quoting=csv.QUOTE_ALL,lineterminator='\n' )
                    csvwriter.writerow(rows)

            elif len(rows[2])>800 and len(rows[2])<3000:
                with open(f"medium/m_ok{i}.csv",'a',encoding='utf-8') as csvfile1:
                    csvwriter=csv.writer(csvfile1, delimiter=',' , quotechar="'", quoting=csv.QUOTE_ALL,lineterminator='\n' )
                    csvwriter.writerow(rows)

            elif len(rows[2])>3000 and len(rows[2])<6000:
                with open(f"large/l_ok{i}.csv",'a',encoding='utf-8') as csvfile1:
                    csvwriter=csv.writer(csvfile1, delimiter=',' , quotechar="'", quoting=csv.QUOTE_ALL,lineterminator='\n' )
                    csvwriter.writerow(rows)