import pyodbc

import export

# driver = flavour of sql. 'SQL Server' in this instance
# sqlserver = sql instance name
# db = database name

driver = 'SQL Server'
sqlserver = 'AARON-LP'  # pycharm complains with \
db = 'Budget'

connectionString = pyodbc.connect('Driver={'+driver+'};'
                                  'Server='+sqlserver+';'
                                  'Database='+db+';'
                                  'Trusted_Connection=yes;')
cursor = connectionString.cursor()


def main():
    sql = 'select * from vBudget'
    cursor.execute(sql)
    export.exportcsv(cursor, 'C:\\temp', 'budget')
    sql = 'select * from vUsers'
    cursor.execute(sql)
    export.exportcsv(cursor, 'C:\\temp', 'users')


main()
