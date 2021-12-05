import mysql.connector
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
    "  `address`            varchar(75)     NOT NULL,"
    "  `email`              varchar(75)     NOT NULL,"
    "  `phone`              varchar(75)     NOT NULL,"
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
    "  `asset_value`        varchar(75)     NOT NULL,"
    "  `asset_type`         varchar(75)     NOT NULL,"
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

cursor.close()
db.close()