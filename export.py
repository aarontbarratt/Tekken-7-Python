import csv
import datetime
import logging as log

logFileName = 'tekken7app.log'
logLocation = 'C:\\temp'
log.basicConfig(filename=logLocation+'\\'+logFileName, level=log.DEBUG)


# this exports data from a sql query cursor
def exportcsv(cursor, location, filename):
    with open(location + '\\' + filename+'.csv', mode='w', newline='') as exportfile:
        exportfile = csv.writer(exportfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        exportfile.writerow(cursor.description)     # provides header information, although very verbose
        for row in cursor:
            exportfile.writerow(row)


# exports data from RB Norway's website into a csv
def createCsv(string, character, flag):
    if flag is True:    # gives separate file for each character
        f = open('C:\\temp\\' + character + '.csv', 'w+')
        f.write(string)
    if flag is False:   # exports all data into one file. Currently does not work
        f = open('C:\\temp\\export.csv', 'w+')
        f.write(string)


def exportToFile(string, location, filename, extension):
    f = open(location+'\\'+filename+'.'+extension, 'a+')    # a = append, + = create if not exist
    f.write(string)
    f.close()
    return 0


def exportToLog(message):
    message = str(message)
    now = datetime.datetime.now()
    now = str(now)
    log.debug(str(now)+' > '+message)
    return message
