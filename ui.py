import tkinter as tk

win = tk.Tk()
win.title('Tekken 7 Frame Data')
win.resizable(1, 1)


def submitcall():
    print('click')


def exitcall():
    print('exit')


# create frame
frame = tk.Frame(win, height=200, width=300)    # create frame with width and height
frame.pack_propagate(0)                         # don't shrink
frame.pack()

frame2 = frame

# entry field in frame
entry = tk.Entry(frame)
# submit button in frame
submit = tk.Button(frame, text='submit', command=submitcall)
exit = tk.Button(frame, text='exit', command=exitcall)

entry.pack()
submit.pack()


win.mainloop()
