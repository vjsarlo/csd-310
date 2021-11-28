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
cursor.execute("SELECT team_id, team_name, mascot FROM team")
teams = cursor.fetchall()
print("- - DISPLAYING TEAM RECORDS - -")
for team in teams:
    print("Team ID: {}".format(team[0]))
    print("Team Name: {}".format(team[1]))
    print("Mascot: {}\n".format(team[2]))

cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()
print("- - DISPLAYING PLAYER RECORDS - -")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team ID: {}\n".format(player[3]))
print("Press any key to continue. . .")