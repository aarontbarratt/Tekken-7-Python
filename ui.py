import tkinter as tk

win = tk.Tk()
win.title('Tekken 7 Frame Data')
win.resizable(1, 1)


def callback():
    print('click')


# create frame
frame = tk.Frame(win, height=200, width=300)    # create frame with width and height
frame.pack_propagate(0)                         # don't shrink
frame.pack()

# entry field in frame
entry = tk.Entry(frame)
# submit button in frame
submit = tk.Button(frame, text='submit', command=callback)

entry.pack()
submit.pack()

win.mainloop()
