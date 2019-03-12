import tkinter as tk

from cleaner import cleanTable
from export import exportToLog
from pagereader import requestPage, exportToFile

characters = ['akuma', 'alisa', 'anna', 'armor-king', 'asuka', 'bob', 'bryan', 'claudio', 'devil-jin', 'dragunov',
              'eddy', 'eliza', 'feng', 'geese', 'gigas', 'heihachi', 'hwoarang', 'jack7', 'jin', 'josie', 'katarina',
              'kazumi', 'kazuya', 'lars', 'lei', 'law', 'lee', 'leo', 'lili', 'lucky-chloe', 'marduk', 'master-raven',
              'miguel', 'nina', 'noctis', 'paul', 'shaheen', 'steve', 'xiaoyu', 'yoshimitsu']


class Tekken7App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)





def run():
    i = 0
    count = len(characters)
    for character in characters:
        i += 1  # increment at the start so 1st loop is 1/40
        page = 'http://rbnorway.org/'+character+'-t7-frames/'
        link = page
        page = requestPage(page)
        page = str(page)
        page = cleanTable(page, character)
        exportToLog('processing: '+link+', '+str(i)+'/'+str(count))
        exportToFile(page, 'C:\\temp', 'fd', 'csv')
