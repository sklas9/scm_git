fout = open("SampleRecords.csv","w+")

fout.write("EmpID,EmpName,Mobile\n")

EmpName = ["John","Jack", "Bill"]
EmpMobile = ["9876", "3243", "3425"]

for i in range(3):
		fout.write(str(i+1)+","+EmpName[i]+","+EmpMobile[i]+"\n")

fout.close()
