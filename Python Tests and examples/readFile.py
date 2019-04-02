import csv

ArrIn = [] #Create an empty array for Inputs
badWords = ['jiggaboo', 'whitey']	
#open csv file
with open('mondaymot.csv', 'r', encoding='utf-8') as csvfile:
	lines = csv.reader(csvfile)
	#read in csv file and store data in a list
	dataset = list(lines)		
	#loop through the list
	for x in range(len(dataset)):
		ArrIn.append(dataset[x][0])
		#create a loop for the input columns
		#print(dataset[x][0])
		if dataset[x] == []: #or '#AIL' in dataset[x][0]:
			print('Hi')
		else:
			ArrIn.append(dataset[x])
			#if 'strong' in dataset[x][0]:
				#ArrIn.append([dataset[x][0][:18]])
			#	print(dataset[x][0][:18])
			#if 'RT' not in dataset[x][0]:
			if 'b' == dataset[x][0][0]:
				i = len(dataset[x][0])
				ArrIn.append([dataset[x][0][2:i-1]]) #store each row in inputs array
			#else:
		#	for word in badWords:
		#		if word in dataset[x][0]:
		#			ArrIn.append(dataset[x])
		#			break
		#sentence = ''
		#for y in range(len(dataset[x])):
		#	sentence += dataset[x][y]
		#ArrIn.append([sentence])

print(ArrIn)
myFile = open('mondaymot.csv', 'w', newline='', encoding='utf-8') 	
with myFile:  
	writer = csv.writer(myFile)
	writer.writerows(ArrIn)