import csv
import re
def remove_place(r):
    n_row=[]
    first=""
    for i in range(0,30):
        first+=r[2][i]
    x = re.findall(("।.*"), first)

    second=""
    for i in range(30,len(r[2])):
        second+=r[2][i]

    if x:
        x[0]=x[0][1:]
        y=x[0]+second
    else:
        y=first+second

    n_row.append(r[0])
    n_row.append(r[1])
    n_row.append(y)
    return n_row
j=0
with open("ok1.csv",'rt',encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)
    for rows in csvreader:        
        if rows and j>0:
            new_row=remove_place(rows)
            with open("new_ok1.csv",'a',encoding='utf-8') as csvfile1:
                csvwriter=csv.writer(csvfile1, delimiter=',' , quotechar="'", quoting=csv.QUOTE_ALL,lineterminator='\n' )
                csvwriter.writerow(new_row)
        j+=1