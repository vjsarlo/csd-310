import mysql.connector
from mysql.connector import errorcode
# CONNECT TO DATABASE !!!(INSERT PASSWORD)!!!
config = {
    "user": "root",
    "password": "Qexeoymp4123!",
    "host": "127.0.0.1",
    "database": "willsonFinancial",
    "raise_on_warnings": True
}
# !!!INSERT PASSWORD ABOVE!!!

db = mysql.connector.connect(**config)
cursor = db.cursor()

# INNER JOIN -AND- SUM TO GET CLIENTS' "NUMBER_OF_TRANSACTIONS_MADE_THIS_MONTH"
# CLIENT "VINCE" HAS 2 ACCOUNTS THAT MADE 6 TRANSACTIONS EACH
# CLIENT "MIKE" HAS 2 ACCOUNTS THAT MADE 4 TRANSACTIONS EACH
sqlJoin = " SELECT first_name, SUM(number_of_transactions_made_this_month) FROM client INNER JOIN account USING (client_id) GROUP BY first_name"
cursor.execute(sqlJoin)
print("\n- - Client's Total Transactions From Accounts In The Past Month - -")
for x in cursor:
    print("Client Name: {}".format(x[0]))
    print("{} Transactions\n".format(x[1]))

# SUBQUERY TO GET CLIENTS THAT ONLY MADE OVER 10 TRANSACTIONS IN PAST MONTH
sqlClients = """SELECT o.client_id, c.first_name, total_transactions
FROM client AS c
INNER JOIN
(
    SELECT client_id,
        SUM(number_of_transactions_made_this_month) as total_transactions
    FROM account
    GROUP BY client_id
    HAVING SUM(number_of_transactions_made_this_month) > 10
) AS o ON c.client_id = o.client_id"""

cursor.execute(sqlClients)
print("- - Clients Who Had Over 10 Transactions From Accounts In The Past Month - -")
for x in cursor:
    print("Client: {}".format(x[1]))
    print("{} Transactions\n".format(x[2]))

# SUBQUERY -AND- COUNT TO SHOW NUMBER OF CLIENTS WHO MADE OVER 10 TRANSACTIONS
sqlTotal = """SELECT COUNT(*) AS Clients
FROM(
SELECT o.client_id, c.first_name, total_transactions
FROM client AS c
INNER JOIN
(
    SELECT client_id,
        SUM(number_of_transactions_made_this_month) as total_transactions
    FROM account
    GROUP BY client_id
    HAVING SUM(number_of_transactions_made_this_month) > 10
) AS o ON c.client_id = o.client_id
)as num_above_ten"""

cursor.execute(sqlTotal)
for x in cursor:
    print("- - Number Of Clients Who Have Made Over 10 Transactions In The Past Month - -\n%2s" % x[0])