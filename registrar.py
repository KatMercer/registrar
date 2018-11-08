#!/usr/bin/python
import sqlite3
import sys
import os.path

courseTable = "courses"

if (len(sys.argv) < 2):
    sys.exit("Invalid database argument")

if (not os.path.isfile(sys.argv[1])):
    sys.exit("Not a file") # temp
    # verify creation
    # attempt creation
else:
    print("a file") #DEBUG
    # all good, continue

# open connection
connec = sqlite3.connect(sys.argv[1])
curs = connec.cursor()

# prepare SQL statement for select
selCourse = "SELECT * FROM "+courseTable
for row in curs.execute(selCourse):
    print row

# bind param in statement to input value
choice = str(input("Course number: "))
query = selCourse+" WHERE course="+choice

# execute query
for row in curs.execute(query):
    print row

# close connection
connec.close()

sys.exit(0)
