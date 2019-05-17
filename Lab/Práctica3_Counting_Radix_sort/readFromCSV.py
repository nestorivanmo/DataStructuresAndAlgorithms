import csv 

with open('info.csv') as info:
	spamreader = csv.reader(info, delimiter=',')
	for row in spamreader:
		print(row[0] + ", " + row[1])