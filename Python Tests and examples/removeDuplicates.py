import csv

class removeDuplicates(object):

	def main(self):
		results = []
		file = input("What file do you want to check for duplicates? ")
		with open(file, 'r', encoding='utf-8-sig') as csvfile:
			reader = csv.reader(csvfile)
			dataset = list(reader)
			
			for row in dataset:
				results.append(row[0])
		self.removeDuplicates(results)

	def removeDuplicates(self, results):
		removeDup = set()
		fixedArr = [sentence for sentence in results if sentence not in removeDup and not removeDup.add(sentence)]
		arr = []
		for result in fixedArr:
			print(str(result))
			arr.append([result])
		file = input("What file do you want to write the solution to? ")
		myFile = open(file, 'w', newline='', encoding='utf-8-sig')  
		with myFile:  
			writer = csv.writer(myFile)
			writer.writerows(arr)

	if __name__ == '__main__':
	    main()