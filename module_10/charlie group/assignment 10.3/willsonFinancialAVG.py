import mysql.connector
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

# COUNT TOTAL AMOUNT OF ASSESTS
sqlCount = "SELECT count(*) FROM asset"
cursor.execute(sqlCount)
for x in cursor:
    print("- - Amount Of Assets From Clients - -\n" + str(x[0]) + " Assets\n")

# RETRIEVE SUM() OF ALL ASSETS IN THE ASSET_VALUE COLUMN
sqlSum = "SELECT sum(asset_value) FROM asset"
cursor.execute(sqlSum)
for x in cursor:
    print("- - Sum Of All Clients' Assets - -\n$" + str(x[0]) + "\n")

# RETRIEVE THE ASSET_VALUE AVG AND ROUND AVG 
sql = "Select ROUND (AVG(asset_value),2) AS average from asset;"
cursor.execute(sql)
avg = cursor.fetchall()
for x in avg:
    print("- - Average Of All Assets - -\n$" + str(x[0]) + "\n")
    

