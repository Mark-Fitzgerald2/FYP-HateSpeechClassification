import csv

myFileOut = open('NonHate.csv', 'w', newline='', encoding='utf-8')   
for num in range(1,18):
	file = open("File"+str(num)+".csv")
	for line in file:
		myFileOut.write(line)
	file.close()
myFileOut.close()