import csv


def exportcsv(cursor, location, filename):
    with open(location +'\\'+filename+'.csv', mode='w', newline='') as exportfile:
        exportfile = csv.writer(exportfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        exportfile.writerow(cursor.description)     # provides header information, although very verbose
        for row in cursor:
            exportfile.writerow(row)
