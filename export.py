import csv
import datetime
import logging as log
import os


paths = ['C:\\Tekken 7 Frame Data', 'C:\\Tekken 7 Frame Data\\export', 'C:\\Tekken 7 Frame Data\\logs']
rootPath = paths[0]
exportPath = paths[1]

logPath = paths[2]
logFileName = 'tekken7app.log'
log.basicConfig(filename=logPath + '\\' + logFileName, level=log.DEBUG)


def init():
    def makeDirectory(_path_):
        p = _path_
        try:
            os.mkdir(p)
        except OSError:
            if os.path.isdir(p):
                print('path: "' + p + '" already exists')
            else:
                print(OSError)
        else:
            print('Created Path: ' + p)

    for path in paths:
        makeDirectory(path)


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
