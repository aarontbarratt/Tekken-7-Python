import pyodbc
from cleaner import left, right, leftright

driver = 'SQL Server'
sqlserver = 'AARON-PC\\MFDOOM'  # pycharm complains with \
db = 'invu'


conn = pyodbc.connect('Driver={'+driver+'};'
                      'Server='+sqlserver+';'
                      'Database='+db+';'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('with cte as '
               '( '
               '    select * from cats '
               '    union all '
               '    select * from dogs '
               ') '
               'select * '
               'from cte ')

for row in cursor:
    row = str(row)

    print(row)
