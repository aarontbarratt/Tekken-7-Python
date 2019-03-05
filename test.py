import tkinter as tk
from tkinter import *

characters = ['akuma', 'alisa', 'anna', 'armor-king', 'asuka', 'bob', 'bryan', 'claudio', 'devil-jin', 'dragunov',
              'eddy', 'eliza', 'feng', 'geese', 'gigas', 'heihachi', 'hwoarang', 'jack7', 'jin', 'josie', 'katarina',
              'kazumi', 'kazuya', 'lars', 'lei', 'law', 'lee', 'leo', 'lili', 'lucky-chloe', 'marduk', 'master-raven',
              'miguel', 'nina', 'noctis', 'paul', 'shaheen', 'steve', 'xiaoyu', 'yoshimitsu']


def main():
    global master
    master = tk.Tk()
    master.geometry('200x200')

    variable = StringVar(master)
    variable.set(characters[0])  # default value

    w = OptionMenu(master, variable, *characters)
    w.pack(side=TOP)

    lb = Label(master, text='thing')
    lb.pack(side=LEFT)

    en = Entry(master)
    en.pack(side=LEFT)

    bt = Button(master, text='Exit', command=exitProgram)
    bt.pack(side=BOTTOM)

    mainloop()


def exitProgram():
    master.destroy()


main()
