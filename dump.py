import tkinter as tk


def calculate_payment(one, two, cost):
    p1 = float(one)
    p2 = float(two)
    cost = float(cost)

    whole = p1 + p2
    p1percent = p1 / whole * 100
    p2percent = p2 / whole * 100

    a = round(cost / 100 * p1percent, 2)
    b = round(cost / 100 * p2percent, 2)
    c = round(a + b, 2)

    return a, b, c


class ExpensesApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # window config
        self.title('Expense Split App')
        self.geometry('200x200')
        self.resizable(0, 0)

        # labels
        self.personOneLb = tk.Label(self, text='Salary 1')
        self.personTwoLb = tk.Label(self, text='Salary 2')
        self.costLb = tk.Label(self, text='Cost')

        # entry fields
        self.personOneEn = tk.Entry(self)
        self.personTwoEn = tk.Entry(self)
        self.costEn = tk.Entry(self)

        # buttons
        self.getButton = tk.Button(self, text='Get', command=self.get)
        self.resultLb = tk.Label(self, text='result')
        self.exitButton = tk.Button(self, text='Exit', command=self.exit)

        # pack UI
        # person 1
        self.personOneLb.pack()
        self.personOneEn.pack()

        # person 2
        self.personTwoLb.pack()
        self.personTwoEn.pack()

        # cost
        self.costLb.pack()
        self.costEn.pack()

        # get button
        self.getButton.pack()
        self.resultLb.pack()

        # exit button
        self.exitButton.pack()

    def get(self):
        a = float(self.personOneEn.get())
        b = float(self.personTwoEn.get())
        c = float(self.costEn.get())
        result = calculate_payment(a, b, c)
        self.resultLb.config(text=str(result))

    def exit(self):
        self.destroy()
