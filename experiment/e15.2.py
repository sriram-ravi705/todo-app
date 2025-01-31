import csv

with open("mod.csv","r") as files:
    print(list(csv.reader(files)))