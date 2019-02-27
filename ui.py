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
    win.geometry('500x450')
    win.resizable(1, 1)

    # sql instance label and field
    lb = tk.Label(win, text='SQL Instance:')
    lb.grid(column=0, row=0)

    fd = tk.Entry(win)
    fd.grid(column=1, row=0)

    # database label and field
    lb = tk.Label(win, text='Database')
    lb.grid(column=0, row=1)

    fd = tk.Entry(win)
    fd.grid(column=1, row=1)

    # connect button
    bt = tk.Button(win, text='connect', command=connectSQL)
    bt.grid(column=0, row=2)

    # exit button
    bt = tk.Button(win, text='exit', command=exitProgram)
    bt.grid(column=1, row=2)

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
