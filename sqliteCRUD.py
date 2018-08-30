import sqlite3
import csv

conn = sqlite3.connect("EmpDB")

cursor = conn.cursor()

cursor.execute('''drop table if exists Employee''')

#Create DB Table
sqlCreateTable = '''create table Employee(EmpID integer, EmpName text, Mobile integer)'''
cursor.execute(sqlCreateTable)

fin = open("SampleRecords.csv","r")
insertCmd = ""
reader = csv.reader(fin, delimiter=',')
#Insert values from CSV into DB table
for line in reader:    
    insertCmd = '''insert into Employee(EmpID, EmpName, Mobile) values (?,?,?)'''
    cursor.execute(insertCmd,(line[0],line[1],line[2]))

#Read table entries
cursor.execute('''select * from Employee''')
all_rows = cursor.fetchall()
for row in all_rows:
    print(row)

#Update entry
print("Enter empID for whom to change Mobile Number")
Eid = int(input())
print("Enter new mobile number")
mob = int(input())
cursor.execute('''update Employee set Mobile = ? where EmpID = ?''',(mob,Eid))

#Delete Record
print("Enter employee ID for deletion of record")
id = input()
cursor.execute('''delete from Employee where EmpID = ?''',id)

cursor.execute('''select * from Employee''')
all_rows = cursor.fetchall()
for row in all_rows:
    print(row)
