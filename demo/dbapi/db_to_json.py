# Convert Employees table to JSON

import sqlite3
import json
import dbutil

employees = []
con = sqlite3.connect(dbutil.DBNAME)
cur = con.cursor()
cur.execute("select * from employees")  # SQL Command

for id, name, job, salary in cur.fetchall():
    employees.append({"id": id, "name": name, "job": job, "salary": salary})

cur.close()
con.close()

print(json.dumps(employees))

# Write to file
f = open("employees.json", "wt")
json.dump(employees, f)
f.close()
