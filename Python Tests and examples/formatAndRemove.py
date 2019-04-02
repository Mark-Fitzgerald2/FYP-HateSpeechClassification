import csv
from removeDuplicates import removeDuplicates
from fixCSVFormat import fixCSVFormat
from TwitterStreamer import TwitterStreamer

def main():
	#fixCSVFormat().main()
	#removeDuplicates().main()
	TwitterStreamer().main()

if __name__ == '__main__':
    main()