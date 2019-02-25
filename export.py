import csv


def exportcsv(cursor, location, filename):
    with open(location +'\\'+filename+'.csv', mode='w', newline='') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in cursor:
            employee_writer.writerow(row)
