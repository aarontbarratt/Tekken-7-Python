import pyodbc
from export import exportcsv

driver = 'SQL Server'
sqlserver = 'AARON-PC\\MFDOOM'  # pycharm complains with \
db = 'Budget'

conn = pyodbc.connect('Driver={'+driver+'};''Server='+sqlserver+';''Database='+db+';''Trusted_Connection=yes;')
cursor = conn.cursor()


def main():
    sql = 'select * from vBudget'
    cursor.execute(sql)
    exportcsv(cursor, 'C:\\temp', 'budget')
    sql = 'select * from vUsers'
    cursor.execute(sql)
    exportcsv(cursor, 'C:\\temp', 'users')


main()
