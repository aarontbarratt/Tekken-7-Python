import pyodbc
from export import exportcsv

# driver = flavour of sql. 'SQL Server' in this instance
# sqlserver = sql instance name
# db = database name

driver = 'SQL Server'
sqlserver = 'AARON-PC\\MFDOOM'  # pycharm complains with \
db = 'Budget'

connectionString = pyodbc.connect('Driver={'+driver+'};''Server='+sqlserver+';''Database='+db+';''Trusted_Connection=yes;')
cursor = connectionString.cursor()


def main():
    sql = 'select * from vBudget'
    cursor.execute(sql)
    exportcsv(cursor, 'C:\\temp', 'budget')
    sql = 'select * from vUsers'
    cursor.execute(sql)
    exportcsv(cursor, 'C:\\temp', 'users')


main()
