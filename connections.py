from distutils.log import error
import pyodbc
import psycopg2

# Function to Sql Server Connection
def sqlServerCnx():
    sqlconnect = None
    try:
        cxnxStr = ("Driver={ODBC Driver 18 for SQL Server};"
            "Server=supi.cademsmart.cl  ;"
            "Database=SUPI;"
            "UID=testing_precios;"
            "PWD=Tp#657;"
            "TrustServerCertificate=yes;")
        
        sqlconnect = pyodbc.connect(cxnxStr)

    except pyodbc.error as err:
        print(f'Error is: {err}')

    return sqlconnect

# Function to PostgreSql connection
def postgresServer():
    connPsql = None
    try:
        #establishing the connection
        connPsql = psycopg2.connect(database="supi", user='odoo', password='odoo', host='ec2-3-73-13-155.eu-central-1.compute.amazonaws.com', port= '5432')
        #connPsql = psycopg2.connect(database="supi", user='odoo', password='', host='localhost', port= '5432')
    except psycopg2.Error as err:
        print(f'Error is: {err}')
    
    return connPsql

    
