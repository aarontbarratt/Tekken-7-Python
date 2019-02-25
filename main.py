import pyodbc
from export import exportcsv


def main():
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
                   '    select *, \'cat\' as type from cats '
                   '    union all '
                   '    select *, \'dog\' as type from dogs '
                   ') '
                   'select id, title, type '
                   'from cte ')

    exportcsv(cursor, 'C:\\temp', 'test')


main()
