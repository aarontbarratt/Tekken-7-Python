import pyodbc
import csv


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
                   'select * '
                   'from cte ')

    with open('C:\\temp\\employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in cursor:
            employee_writer.writerow(row)

main()
