import mysql.connector
from datetime import date
from mysql.connector import errorcode
# CONNECT TO DATABASE !!!(INSERT PASSWORD)!!!
config = {
    "user": "root",
    "password": "x",
    "host": "127.0.0.1",
    "database": "willsonFinancial",
    "raise_on_warnings": True
}
# !!!INSERT PASSWORD ABOVE!!!

db = mysql.connector.connect(**config)
cursor = db.cursor()


query = """SELECT first_name, start_up_date FROM client
        WHERE start_up_date BETWEEN %s AND %s
        GROUP BY start_up_date 
        ORDER BY start_up_date DESC"""

sqlMonths = """SELECT start_up_date,
    count(*) AS total
FROM client
WHERE EXTRACT(MONTH FROM start_up_date) >= '6'
GROUP BY EXTRACT(month FROM start_up_date)
ORDER BY EXTRACT(month FROM start_up_date) DESC"""

hire_start = date(2021, 6, 1)
hire_end = date(2021, 12, 31)

cursor.execute(query, (hire_start, hire_end))

print("- - Number Of Clients Who Have Joined In The Past 6 Months - -")
for (x, joined_date) in cursor:
  print("{} Joined On {:%b-%d-%Y}\n".format(
    x, joined_date))
cursor.execute(sqlMonths)

print("- - Number Of Clients Who Have Joined In The Past 6 Months - -")
for x in cursor:
    if x[1] > 1:
        print(" {:%b-%Y}: {} Clients\n".format(x[0], x[1]))
    else:
        print(" {:%b-%Y}: {} Client\n".format(x[0], x[1]))
    

