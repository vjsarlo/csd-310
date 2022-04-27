from __future__ import print_function
import mysql.connector
from datetime import date
from mysql.connector import errorcode

# # CONNECT TO MYSQL !!!(INSERT PASSWORD)!!!
config = {
    "user": "root",
    "password": "x",
    "host": "127.0.0.1",
    "raise_on_warnings": True
}
# !!!INSERT PASSWORD ABOVE!!!
db = mysql.connector.connect(**config)
cursor = db.cursor()

# DROP DATABASE IF EXISTS
cursor.execute("DROP DATABASE IF EXISTS willsonFinancial")

# DEFINE DATABASE IN GLOBAL VARIABLE
DB_NAME = 'willsonFinancial'

# DEFINE CREATE_DATABASE FUNCTION
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed Creating Database: {}".format(err))
        exit(1)

# TRY CHANGE TO GLOBAL DATABASE
try:
    cursor.execute("USE {}".format(DB_NAME))
# CHECK IF ERROR = DATABASE DOES NOT EXIST
# SHOW ERROR NUMBER IF ANY OTHER ERROR
except mysql.connector.Error as err:
    print("Database {} Does Not Exist.".format(DB_NAME))
    # CREATE DATABASE IF ERROR = DOES NOT EXIST
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} Successfully Created.".format(DB_NAME))
        db.database = DB_NAME
    else:
        print(err)
        exit(1)

# DROP TABLES IF ALREADY EXISTS
sql = ("DROP TABLE IF EXISTS client, account, asset")

# CREATE DICTIONARY FOR TABLES
TABLES = {}

# DEFINE TABLES
TABLES['client'] = (
    "CREATE TABLE `client` ("
    "  `client_id`          int             NOT NULL    AUTO_INCREMENT,"
    "  `first_name`         varchar(75)     NOT NULL,"
    "  `last_name`          varchar(75)     NOT NULL,"
    "  `start_up_date`      date     NOT NULL,"
    "  PRIMARY KEY (`client_id`)"
    ") ENGINE=InnoDB")

TABLES['asset'] = (
    "  CREATE TABLE `asset` ("
    "  `asset_id`                 int             NOT NULL    AUTO_INCREMENT,"
    "  `asset_name`               varchar(75)     NOT NULL,"
    "  `asset_value`              int             NOT NULL,"
    "  `asset_type`               varchar(75)     NOT NULL,"
    "  PRIMARY KEY (`asset_id`)"
    ") ENGINE=InnoDB")

TABLES['account'] = (
    "CREATE TABLE `account` ("
    "  `account_id`                              int             NOT NULL    AUTO_INCREMENT,"
    "  `client_id`                               int             NOT NULL,"
    "  `asset_id`                                int             NOT NULL,"
    "  `account_name`                            varchar(75)     NOT NULL,"
    "  `number_of_transactions_made_this_month`  int     NOT NULL,"
    "  PRIMARY KEY (`account_id`), KEY `client_id` (`client_id`),"
    "  KEY `asset_id` (`asset_id`),"
    "  CONSTRAINT `account_fk_1` FOREIGN KEY (`client_id`)"
    "     REFERENCES `client` (`client_id`),"
    "  CONSTRAINT `account_fk_2` FOREIGN KEY (`asset_id`)"
    "     REFERENCES `asset` (`asset_id`)"
    ") ENGINE=InnoDB")

# ITERATE THROUGH TABLES{} DICTIONARY
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("{} Table Created: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("YES")

# CLIENT INSERTS
add_client = """INSERT INTO client (first_name, last_name, start_up_date)
               VALUES (%s, %s, %s)"""
    
# LAST NAMES ARE NUMBERS IN ASC ORDER TO DEMOSTRATE EFFECTIVENESS OF ORDER BY start_up_date
client_data = [('Vince', 'One', '2021-09-01'),
            ('Chad', 'Two', '2021-09-02'),
            ('Tatiyana', 'Three', '2021-08-01'),
            ('Ashley', 'Four', '2021-07-01'),
            ('Mike', 'Five', '2021-06-01'),
            ('Carrol', 'Six', '2021-01-01')]

cursor.executemany(add_client, client_data)
client_id = cursor.lastrowid
print('Client Table: DONE')

# ASSET INSERTS
add_asset = """INSERT INTO asset (asset_name, asset_value, asset_type)
               VALUES (%s, %s, %s)"""

asset_data = [('Walt Disney World Stock', 100 , 'Stock'),
                ('Crypto', 200, 'Stock'),
                ('Apple Stock', 300, 'Stock'),
                ('Index Funds', 400, 'RothIRA'),
                ('Mutual Funds', 500, 'RothIRA'),
                ('Bonds', 600, 'RothIRA')]

cursor.executemany(add_asset, asset_data)
asset_id = cursor.lastrowid
print('Asset Table: DONE')

# ACCOUNT INSERTS
add_account = """INSERT INTO account (client_id, asset_id, account_name, number_of_transactions_made_this_month)
               VALUES (%(client_id)s, %(asset_id)s, %(account_name)s, %(number_of_transactions_made_this_month)s)"""

account_data= [{'client_id': 1, 'asset_id': 1, 'account_name': 'Account One', 'number_of_transactions_made_this_month': 6},
            {'client_id': 1, 'asset_id': 2, 'account_name': 'Account Two', 'number_of_transactions_made_this_month': 6},
            {'client_id': 3, 'asset_id': 3, 'account_name': 'Account Three', 'number_of_transactions_made_this_month': 20},
            {'client_id': 4, 'asset_id': 6, 'account_name': 'Account Four', 'number_of_transactions_made_this_month': 5},
            {'client_id': 5, 'asset_id': 5, 'account_name': 'Account Five', 'number_of_transactions_made_this_month': 4},
            {'client_id': 5, 'asset_id': 4, 'account_name': 'Account Six', 'number_of_transactions_made_this_month': 4}]

cursor.executemany(add_account, account_data)
account_id = cursor.lastrowid
print('Account Table: DONE')

db.commit()

print('Database Created. Tables Created. All Tables Filled.')

cursor.close()
db.close()
