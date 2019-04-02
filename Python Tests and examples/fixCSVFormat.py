import csv

class fixCSVFormat(object):

	def main(self):
		results = []
		file = input("What file do you want to fix the CSV file format? ")
		columns = eval(input("What is the max number of columns in the file? "))
		print(columns)
		with open(file, 'r') as csvfile:
			reader = csv.reader(csvfile)
			dataset = list(reader)
			
			for x in range(0, len(dataset)):
				result = ''
				for y in range(0, columns):
					if dataset[x][y] != '':
						if y > 0:
							result += ','
						result += dataset[x][y]
				results.append([result])
		self.printResults(results)

	def printResults(self, results):
		for result in results:
			print(str(result))
		#print(results)
		#give write permission to the file
		file = input("What file do you want to write the solution to? ")
		myFile = open(file, 'w', newline='')  
		with myFile:  
			writer = csv.writer(myFile)
			writer.writerows(results)

	if __name__ == '__main__':
		main()