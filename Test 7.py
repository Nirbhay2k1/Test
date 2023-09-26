import csv
with open("file1.txt", "r") as input:	
	
	with open("file2.txt", "w") as output:
				
		for line in input:
			output.write(line)
