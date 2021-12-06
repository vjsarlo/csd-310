import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Qexeoymp4123!",
    "host": "127.0.0.1",
    "database": "willsonFinancial",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

cursor.execute("SELECT client_id, first_name, last_name, start_up_date FROM client")
clients = cursor.fetchall()
print("- - DISPLAYING CLIENT RECORDS - -")
for client in clients:
    print("Client ID: {}".format(client[0]))
    print("First Name: {}".format(client[1]))
    print("Last Name: {}".format(client[2]))
    print("Starting Date: {}\n".format(client[3]))

cursor.execute("SELECT account_id, client_id, billing_structure_id, account_name, account_billing_structure FROM account")
accounts = cursor.fetchall()
print("- - DISPLAYING ACCOUNT RECORDS - -")
for account in accounts:
    print("Account ID: {}".format(account[0]))
    print("Client ID: {}".format(account[1]))
    print("Billing Structure ID: {}".format(account[2]))
    print("Account Name: {}".format(account[3]))
    print("Account Billing Structure: {}\n".format(account[4]))

cursor.execute("SELECT billing_structure_id, billing_structure_name, number_transactions_made, monthly_charge FROM billing_structure")
billings = cursor.fetchall()
print("- - DISPLAYING BILLING STRUCTURE RECORDS - -")
for billing in billings:
    print("Billing Structure ID: {}".format(billing[0]))
    print("Billing Structure Name: {}".format(billing[1]))
    print("Number Transactions Made: {}".format(billing[2]))
    print("Monthly Charge: {}\n".format(billing[3]))

cursor.execute("SELECT asset_id, asset_name, asset_value, asset_type FROM asset")
assets = cursor.fetchall()
print("- - DISPLAYING ASSET RECORDS - -")
for asset in assets:
    print("Asset ID: {}".format(asset[0]))
    print("Asset Name: {}".format(asset[1]))
    print("Asset Value: {}".format(asset[2]))
    print("Asset Type: {}\n".format(asset[3]))

cursor.execute("SELECT transaction_id, account_id, asset_id, transaction_name, transaction_value, transaction_type FROM transaction")
transactions = cursor.fetchall()
print("- - DISPLAYING ACCOUNT RECORDS - -")
for transaction in transactions:
    print("Transaction ID: {}".format(transaction[0]))
    print("Account ID: {}".format(transaction[1]))
    print("Asset ID: {}".format(transaction[2]))
    print("Transaction Name: {}".format(transaction[3]))
    print("Transaction Value: {}".format(transaction[4]))
    print("Transaction Type: {}\n".format(transaction[5]))

    

