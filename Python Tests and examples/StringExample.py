import csv

trantab = str.maketrans({"-":  r"\-", "]":  r"\]", "\\": r"\\", "^":  r"\^", "$":  r"\$", "*":  r"\*", ".":  r"\.", "'": r"\'", "&": r"\&"})

byte = b"Hi I have Mark's stuff & I am great"
other = "Hi I have Mark's stuff & I am great"
arr = []
arr.append(byte)
arr.append(other)
arr.append(other.translate(trantab))
file = input("What file do you want to write the solution to? ")
myFile = open(file, 'w', newline='', encoding='utf-8') 	
with myFile:  
	writer = csv.writer(myFile)
	writer.writerows(arr)
