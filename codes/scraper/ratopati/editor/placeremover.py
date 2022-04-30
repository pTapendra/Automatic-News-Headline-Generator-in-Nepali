import csv
import re

def remove_place(r):
    n_row=[]
    first=""
    for i in range(0,30):
        first+=r[1][i]
    x = re.findall(("।.*"), first)

    second=""
    for i in range(30,len(r[1])):
        second+=r[1][i]

    if x:
        x[0]=x[0][1:]
        y=x[0]+second
    else:
        y=first+second

    n_row.append(r[0])
    n_row.append(y)
    return n_row


for i in range(1,8):
    print(i)
    with open(f"original/news{i}.csv",'rt',encoding='utf-8') as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)
        for j,rows in enumerate(csvreader):
            if len(rows[1])>30:
                new_row=remove_place(rows)
                with open(f"news{i}.csv",'a',encoding='utf-8') as csvfile1:
                    csvwriter=csv.writer(csvfile1, delimiter=',' , quotechar="'", quoting=csv.QUOTE_ALL,lineterminator='\n' )
                    csvwriter.writerow(new_row)