import csv
import re

def remove_place(r):
    n_row=[]
    first=""
    for i in range(0,40):
        first+=r[1][i]
    x = re.findall(("—.*"), first)

    second=""
    for i in range(40,len(r[1])):
        second+=r[1][i]

    if x:
        x[0]=x[0][2:]
        y=x[0]+second
    else:
        y=first+second

    n_row.append(r[0])
    n_row.append(y)
    return n_row


for i in range(0,10):
    print(i)
    with open(f"national{i}.csv",'rt',encoding='utf-8') as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)
        for rows in csvreader:
            new_row=remove_place(rows)
            with open(f"original/national{i}.csv",'a',encoding='utf-8') as csvfile1:
                csvwriter=csv.writer(csvfile1, delimiter=',' , quotechar="'", quoting=csv.QUOTE_ALL,lineterminator='\n' )
                csvwriter.writerow(new_row)