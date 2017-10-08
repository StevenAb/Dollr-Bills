import csv

names = []
values = []

with open('top-stocks-to-own-top-intraday-10-08-2017.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        names.append(row[1])
        values.append(row[2])
names.pop(0)
values.pop(0)
def getStock(amount):
    for i in range(len(values)):
        if float(values[i]) <= amount:
            value,index = float(values[i]),i
            break
    name = names[index]
    return [value,name]
