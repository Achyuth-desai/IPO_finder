import csv

f=open("diff.csv","w",encoding="utf-8")

match = 0;
with open("file.csv") as file1:
	read1 = csv.DictReader(file1)
	with open("file1.csv") as file2:
		read2 = csv.DictReader(file2)
		for row1 in read2:
			for row2 in read1:
				if row1 == row2 :
					match=1
			if match==1:
				f.write(row2)
				f.write("\n")
				break
		match=0
f.close()