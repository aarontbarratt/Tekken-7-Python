import tkinter as tk
from tkinter import *
from cleaner import cleanTable
from export import exportToLog
from pagereader import requestPage, exportToFile

# add Negan and Julia when frame data is available
characters = ['akuma', 'alisa', 'anna', 'armor-king', 'asuka', 'bob', 'bryan', 'claudio', 'devil-jin', 'dragunov',
              'eddy', 'eliza', 'feng', 'geese', 'gigas', 'heihachi', 'hwoarang', 'jack7', 'jin', 'josie', 'katarina',
              'kazumi', 'kazuya', 'lars', 'lei', 'law', 'lee', 'leo', 'lili', 'lucky-chloe', 'marduk', 'master-raven',
              'miguel', 'nina', 'noctis', 'paul', 'shaheen', 'steve', 'xiaoyu', 'yoshimitsu']


def createUI():
    global win
    # create window
    win = tk.Tk()
    win.title('Tekken 7 Frame Data')
    win.geometry('250x250')
    win.resizable(0, 0)

    # run button
    bt = tk.Button(win, text='CSV', command=CSVWindow)
    bt.grid(column=0, row=0)

    # csv button
    bt = tk.Button(win, text='SQL', command=SQLWindow)
    bt.grid(column=1, row=0)

    # exit button
    bt = tk.Button(win, text='Exit', command=exitProgram)
    bt.grid(column=2, row=0)

    # start loop
    win.mainloop()


def SQLWindow():
    global SQLWin
    SQLWin = tk.Tk()
    SQLWin.title('SQL')
    SQLWin.geometry('350x75')
    SQLWin.resizable(0, 0)

    # labels
    lb = tk.Label(SQLWin, text='SQL Server')
    lb.grid(column=0, row=0)

    lb = tk.Label(SQLWin, text='DB')
    lb.grid(column=1, row=0)

    # entry fields
    en = tk.Entry(SQLWin)
    en.grid(column=0, row=1)

    en = tk.Entry(SQLWin)
    en.grid(column=1, row=1)

    # buttons
    bt = tk.Button(SQLWin, text='Connect', command=testSQLConnection)
    bt.grid(column=2, row=1)

    bt = tk.Button(SQLWin, text='Exit', command=closeSQLWindow)
    bt.grid(column=3, row=1)

    # start loop
    SQLWin.mainloop()


def CSVWindow():
    global CSVWin
    CSVWin = tk.Tk()
    CSVWin.title('SQL')
    CSVWin.geometry('150x300')
    CSVWin.resizable(0, 0)

    # character drop down menu
    var = StringVar(CSVWin)
    var.set(characters[0])  # default value
    om = OptionMenu(CSVWin, var, *characters)
    om.pack(fill=X)

    bt = tk.Button(CSVWin, text='Export', command=run)
    bt.pack(fill=X)

    bt = tk.Button(CSVWin, text='Exit', command=closeCSVWindow)
    bt.pack(fill=X)


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


def testSQLConnection():
    exportToLog('Test SQL Connection')
    # test sql connection and set label to success or fail


def exitProgram():
    exportToLog('Exit App')
    win.quit()
    win.destroy()   # need both to completely close program


def closeSQLWindow():
    exportToLog('Close SQL Window')
    SQLWin.destroy()


def closeCSVWindow():
    exportToLog('Close CSV Window')
    CSVWin.destroy()
