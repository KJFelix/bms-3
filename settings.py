import os
# Uncomment once https://github.com/theskumar/python-dotenv/issues/113 is fixed
# from dotenv import load_dotenv
# load_dotenv()

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': os.environ['BMS_USERNAME'],
    'password': os.environ['BMS_PASSWORD'],
    'database': os.environ['BMS_DATABASE']
}
