import csv

data = []
with open('transposecsv.csv') as f:
    for row in csv.reader(f):
        data.append(row)
    print(data)

#find index of header, then get the same index position for each row
