from __future__ import print_function
import mysql.connector
from datetime import date
from mysql.connector import errorcode


config = {
    "user": "root",
    "password": "Qexeoymp4123!",
    "host": "127.0.0.1",
    "raise_on_warnings": True
}
db = mysql.connector.connect(**config)
cursor = db.cursor()
DB_NAME = 'willsonFinancial'
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        db.database = DB_NAME
    else:
        print(err)
        exit(1)

TABLES = {}
TABLES['client'] = (
    "CREATE TABLE `client` ("
    "  `client_id`          int             NOT NULL    AUTO_INCREMENT,"
    "  `first_name`         varchar(75)     NOT NULL,"
    "  `last_name`          varchar(75)     NOT NULL,"
    "  `start_up_date`      varchar(75)     NOT NULL,"
    "  PRIMARY KEY (`client_id`)"
    ") ENGINE=InnoDB")

TABLES['billing_structure'] = (
    "CREATE TABLE `billing_structure` ("
    "  `billing_structure_id`                 int             NOT NULL    AUTO_INCREMENT,"
    "  `billing_structure_name`               varchar(75)     NOT NULL,"
    "  `number_transactions_made`             varchar(75)     NOT NULL,"
    "  `monthly_charge`                       varchar(75)     NOT NULL,"
    "  PRIMARY KEY (`billing_structure_id`)"
    ") ENGINE=InnoDB")

TABLES['account'] = (
    "CREATE TABLE `account` ("
    "  `account_id`                 int             NOT NULL    AUTO_INCREMENT,"
    "  `client_id`                  int             NOT NULL,"
    "  `billing_structure_id`       int             NOT NULL,"
    "  `account_name`               varchar(75)     NOT NULL,"
    "  `account_billing_structure`  varchar(75)     NOT NULL,"

    "  PRIMARY KEY (`account_id`), KEY `client_id` (`client_id`),"
    "  KEY `billing_structure_id` (`billing_structure_id`),"
    "  CONSTRAINT `account_ibfk_1` FOREIGN KEY (`client_id`)"
    "     REFERENCES `client` (`client_id`),"
    "  CONSTRAINT `account_ibfk_2` FOREIGN KEY (`billing_structure_id`)"
    "     REFERENCES `billing_structure` (`billing_structure_id`)"
    ") ENGINE=InnoDB")

TABLES['asset'] = (
    "  CREATE TABLE `asset` ("
    "  `asset_id`                 int             NOT NULL    AUTO_INCREMENT,"
    "  `asset_name`               varchar(75)     NOT NULL,"
    "  `asset_value`              varchar(75)     NOT NULL,"
    "  `asset_type`               varchar(75)     NOT NULL,"
    "  PRIMARY KEY (`asset_id`)"
    ") ENGINE=InnoDB")

TABLES['transaction'] = (
    "CREATE TABLE `transaction` ("
    "  `transaction_id`                       int           NOT NULL    AUTO_INCREMENT,"
    "  `account_id`                           int           NOT NULL,"
    "  `asset_id`                             int           NOT NULL,"
    "  `transaction_name`                     varchar(75)   NOT NULL,"
    "  `transaction_value`                    varchar(75)   NOT NULL,"
    "  `transaction_type`                     varchar(75)   NOT NULL,"
    "  PRIMARY KEY (`transaction_id`), KEY `account_id` (`account_id`),"
    "  KEY `asset_id` (`asset_id`),"
    "  CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`account_id`)"
    "     REFERENCES `account` (`account_id`),"
    "  CONSTRAINT `transaction_ibfk_2` FOREIGN KEY (`asset_id`)"
    "     REFERENCES `asset` (`asset_id`)"
    ") ENGINE=InnoDB")


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Create table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
# CLIENT INSERTS
add_client = """INSERT INTO client (first_name, last_name, start_up_date)
               VALUES (%s, %s, %s)"""
    

client_data = [('Vince', 'One', '2021/6/14'),
            ('Chad', 'Two', '2021/6/14'),
            ('Tatiyana', 'Three', '2021/6/14'),
            ('Ashley', 'Four', '2020/6/14'),
            ('Mike', 'Five', '2020/6/14'),
            ('Carrol', 'Six', '2020/6/14')]
cursor.executemany(add_client, client_data)

client_id = cursor.lastrowid

print('Client OK')
db.commit()

# BILLING_STRUCTURE INSERTS
add_billing_structure = """INSERT INTO billing_structure (billing_structure_name, number_transactions_made, monthly_charge)
               VALUES (%s, %s, %s)"""

billing_structure_data = [('Small Account', 'Under 10', 'Small Account Charge'),
                        ('Large Account', 'Over 10', 'Large Account Charge')]

cursor.executemany(add_billing_structure, billing_structure_data)

billing_structure_id = cursor.lastrowid

print('Billing OK')

# ASSET INSERTS
add_asset = """INSERT INTO asset (asset_name, asset_value, asset_type)
               VALUES (%s, %s, %s)"""

asset_data = [('Walt Disney World Stock', '$100', 'Stock'),
('Crypto', '$200', 'Stock'),
('Apple Stock', '$300', 'Stock'),
('Index Funds', '$400', 'RothIRA'),
('Mutual Funds', '$500', 'RothIRA'),
('Bonds', '$600', 'RothIRA')]

cursor.executemany(add_asset, asset_data)

asset_id = cursor.lastrowid

print('Asset OK')

# ACCOUNT INSERTS
add_account = """INSERT INTO account (client_id, billing_structure_id, account_name, account_billing_structure)
               VALUES (%(client_id)s, %(billing_structure_id)s, %(account_name)s, %(account_billing_structure)s)"""

account_data= [{'client_id': client_id, 'billing_structure_id': billing_structure_id, 'account_name': 'Account One', 'account_billing_structure': 'See Billing Structure ID'},
            {'client_id': client_id, 'billing_structure_id': billing_structure_id, 'account_name': 'Account Two', 'account_billing_structure': 'See Billing Structure ID'},
            {'client_id': client_id, 'billing_structure_id': billing_structure_id, 'account_name': 'Account Three', 'account_billing_structure': 'See Billing Structure ID'},
            {'client_id': client_id, 'billing_structure_id': billing_structure_id, 'account_name': 'Account Four', 'account_billing_structure': 'See Billing Structure ID'},
            {'client_id': client_id, 'billing_structure_id': billing_structure_id, 'account_name': 'Account Five', 'account_billing_structure': 'See Billing Structure ID'},
            {'client_id': client_id, 'billing_structure_id': billing_structure_id, 'account_name': 'Account Six', 'account_billing_structure': 'See Billing Structure ID'}]

cursor.executemany(add_account, account_data)

account_id = cursor.lastrowid

print('Account OK')

# TRANSACTION INSERT
add_transaction = """INSERT INTO transaction (account_id, asset_id, transaction_name, transaction_value, transaction_type)
              VALUES (%(account_id)s, %(asset_id)s, %(transaction_name)s, %(transaction_value)s, %(transaction_type)s)"""

transaction_data = [{'account_id': account_id, 'asset_id': asset_id, 'transaction_name': 'Transaction One', 'transaction_value': '$100', 'transaction_type': 'Type One'},
                    {'account_id': account_id, 'asset_id': asset_id, 'transaction_name': 'Transaction Two', 'transaction_value': '$200', 'transaction_type': 'Type Two'},
                    {'account_id': account_id, 'asset_id': asset_id, 'transaction_name': 'Transaction Three', 'transaction_value': '$300', 'transaction_type': 'Type Three'},
                    {'account_id': account_id, 'asset_id': asset_id, 'transaction_name': 'Transaction Four', 'transaction_value': '$400', 'transaction_type': 'Type Four'},
                    {'account_id': account_id, 'asset_id': asset_id, 'transaction_name': 'Transaction Five', 'transaction_value': '$500', 'transaction_type': 'Type Five'},
                    {'account_id': account_id, 'asset_id': asset_id, 'transaction_name': 'Transaction Six', 'transaction_value': '$600', 'transaction_type': 'Type Six'}]
                    

cursor.executemany(add_transaction, transaction_data)

transaction_id = cursor.lastrowid

print('Transaction OK')

db.commit()

print('Db created. Tables Created. All Tables filled.')

cursor.close()
db.close()