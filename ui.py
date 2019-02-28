import tkinter as tk
from export import exportToLog
from pagereader import requestPage, exportToFile
from cleaner import cleanTable

characters = ['akuma', 'alisa', 'anna', 'armor-king', 'asuka', 'bob', 'bryan', 'claudio', 'devil-jin', 'dragunov',
              'eddy', 'eliza', 'feng', 'geese', 'gigas', 'heihachi', 'hwoarang', 'jack7', 'jin', 'josie', 'katarina',
              'kazumi', 'kazuya', 'lars', 'lei', 'law', 'lee', 'leo', 'lili', 'lucky-chloe', 'marduk', 'master-raven',
              'miguel', 'nina', 'noctis', 'paul', 'shaheen', 'steve', 'xiaoyu', 'yoshimitsu']


def createUI():
    global win
    # create window
    win = tk.Tk()
    win.title('Tekken 7 Frame Data')
    win.geometry('200x200')
    win.resizable(1, 1)

    # run button
    bt = tk.Button(win, text='Run', command=dat)
    bt.grid(column=0, row=0)
    bt.flash()

    # exit button
    bt = tk.Button(win, text='Exit', command=exitProgram)
    bt.grid(column=1, row=0)

    win.mainloop()


def connectSQL():
    # use field data to connect
    exportToLog('connected')
    print('connect')
    dat()


def exitProgram():
    exportToLog('exit app')
    win.destroy()   # needs () to work


def dat():
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
