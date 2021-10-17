import csv

filename = "actor.csv"

with open(filename, 'r') as myfile:
    csvreader = csv.reader(myfile)

    contents = [row for row in csvreader]

for row in contents:
    for cell in row:
        print("{:12}".format(cell), end=" ")
    print()
