import os

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': os.environ['BMS_USERNAME'],
    'password': os.environ['BMS_PASSWORD'],
    'database': os.environ['BMS_DATABASE']
}
