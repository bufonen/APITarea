import pyodbc

server = 'SANTIAGO\\SQLEXPRESS' #nombre del servidor sql
database = 'MIBASE' #nombre de la base de datos
connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
)

 
####CAROLINA####

def get_connection():
    return pyodbc.connect(connection_string)
