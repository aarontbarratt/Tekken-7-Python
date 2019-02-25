import pyodbc
from export import exportcsv

driver = 'SQL Server'
sqlserver = 'AARON-PC\\MFDOOM'  # pycharm complains with \
db = 'Budget'


def main():
    conn = pyodbc.connect('Driver={'+driver+'};'
                          'Server='+sqlserver+';'
                          'Database='+db+';'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute('select * from vBudget')

    exportcsv(cursor, 'C:\\temp', 'test')


main()
