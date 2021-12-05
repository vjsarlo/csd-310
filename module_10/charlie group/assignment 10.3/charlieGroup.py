import mysql.connector
from mysql.connector import errorcode


config = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= "Qexeoymp4123!"
)

charlie_db = config.cursor()
charlie_db.execute("CREATE DATABASE willsonFinancial")

try:
    charlie_db = mysql.connector.connect(**config)
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    cursor = charlie_db.cursor()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specific database does not exist")
    else:
        print(err)
else:
    charlie_db.close()

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

TABLES['account'] = (
    "CREATE TABLE `account` ("
    "  `account_id`                 int             NOT NULL    AUTO_INCREMENT,"
    "  `account_name`               varchar(75)     NOT NULL,"
    "  `account_billing_structure`  varchar(75)     NOT NULL,"
    "  PRIMARY KEY (`account_id`)"
    "  CONSTRAINT `fk_client` FOREIGN KEY (`client_id`) "
    "     REFERENCES `client` (`client_id`)"
    "  CONSTRAINT `fk_billing_structure` FOREIGN KEY (`billing_structure_id`) "
    "     REFERENCES `billing_structure` (`billing_structure_id`)"
    ") ENGINE=InnoDB")

TABLES['billing_structure'] = (
    "CREATE TABLE `billing_structure` ("
    "  `billing_structure_id`                 int             NOT NULL    AUTO_INCREMENT,"
    "  `billing_structure_name`               varchar(75)     NOT NULL,"
    "  `number_transactions_made`             varchar(75)     NOT NULL,"
    "  `monthly_charge`                       varchar(75)     NOT NULL,"
    "  PRIMARY KEY (`billing_structure`)"
    ") ENGINE=InnoDB")

TABLES['transaction'] = (
    "CREATE TABLE `transaction` ("
    "  `transaction_id`                       int           NOT NULL    AUTO_INCREMENT,"
    "  `transaction_name`                     varchar(75)   NOT NULL,"
    "  `transaction_value`                    varchar(75)   NOT NULL,"
    "  `transaction_type`                     varchar(75)   NOT NULL,"
    "  PRIMARY KEY (`transaction_id')"
    "  CONSTRAINT `fk_account_id` FOREIGN KEY (`account_id`) "
    "     REFERENCES `account` (`account_id`)"
    "  CONSTRAINT `fk_asset_id` FOREIGN KEY (`asset_id`) "
    "     REFERENCES `asset` (`asset_id`)"
    ") ENGINE=InnoDB")

TABLES['asset'] = (
    "  CREATE TABLE `asset` ("
    "  `asset_id`           int             NOT NULL    AUTO INCREMENT,"
    "  `asset_name`         varchar(75)     NOT NULL,"
    "  `asset_value`        varchar(75)     NOT NULL,"
    "  `asset_type`         varchar(75)     NOT NULL,"
    "  PRIMARY KEY (`asset_id`),"
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