import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "Qexeoymp4123!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
db = mysql.connector.connect(**config)

cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
myresult = cursor.fetchall()
print("- - DISPLAYING TEAM RECORDS - -")
for x in myresult:
    print("Player ID: {}".format(x[0]))
    print("First Name: {}".format(x[1]))
    print("Last Name: {}".format(x[2]))
    print("Team Name: {}\n\n\n".format(x[3]))
print("Press any key to continue. . .")