# creates ui layout

import tkinter as tk

# ui events
#   might be best to move into a different file in the future


def connectSQL():
    print('connect')


def exitProgram():
    global win
    win.destroy()


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
bt = tk.Button(win, text='exit', command=exitProgram())
bt.grid(column=1, row=2)

win.mainloop()
