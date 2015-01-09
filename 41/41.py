#Problem 42 Coded Triangle 
import csv
def fotwo(a):
    list=[]
    with open('42.csv') as f:
        rowdata=[]
        reader = csv.reader(f)
        for row in reader:
            rowdata.append(row)
            print(rowdata[0])
fotwo(1)
       

