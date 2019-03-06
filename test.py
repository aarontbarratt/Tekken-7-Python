import tkinter as tk
from export import exportToLog


def calcPayment(salaryOne, salaryTwo, cost):
    p1 = float(salaryOne)
    p2 = float(salaryTwo)
    cost = float(cost)

    whole = p1 + p2
    p1Percent = p1 / whole * 100
    p2Percent = p2 / whole * 100

    a = round(cost / 100 * p1Percent, 2)
    b = round(cost / 100 * p2Percent, 2)
    c = round(a + b, 2)

    return a, b, c


class ExpensesApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Expense Split App')
        self.geometry('200x200')
        self.resizable(0, 0)

        # create ui
        self.personOneLb = tk.Label(self, text='Salary 1')
        self.personTwoLb = tk.Label(self, text='Salary 2')
        self.costLb = tk.Label(self, text='Cost')

        self.personOneEn = tk.Entry(self)
        self.personTwoEn = tk.Entry(self)
        self.costEn = tk.Entry(self)

        self.getButton = tk.Button(self, text='Get', command=self.onGet)
        self.resultLb = tk.Label(self, text='result')
        self.exitButton = tk.Button(self, text='Exit', command=self.onExit)

        # pack ui
        self.personOneLb.pack()
        self.personOneEn.pack()

        self.personTwoLb.pack()
        self.personTwoEn.pack()

        self.costLb.pack()
        self.costEn.pack()

        self.getButton.pack()
        self.resultLb.pack()
        self.exitButton.pack()

    def onGet(self):
        a = float(self.personOneEn.get())
        b = float(self.personTwoEn.get())
        c = float(self.costEn.get())
        result = calcPayment(a, b, c)
        self.resultLb.config(text=str(result))

    def onExit(self):
        exportToLog('Exit Test Program')
        self.destroy()


app = ExpensesApp()
app.mainloop()
