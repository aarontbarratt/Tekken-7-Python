import tkinter as tk

import cleaner as clean
import pagereader

# in the format of the tekken 7 wiki
dutchCharacters = ['All', 'akuma', 'alisa', 'anna', 'armor-king', 'asuka', 'bob', 'bryan', 'claudio', 'devil-jin',
                   'dragunov', 'eddy', 'eliza', 'feng', 'geese', 'gigas', 'heihachi', 'hwoarang', 'jack7', 'jin',
                   'josie', 'katarina', 'kazumi', 'kazuya', 'lars', 'lei', 'law', 'lee', 'leo', 'lili', 'lucky-chloe',
                   'marduk', 'master-raven', 'miguel', 'nina', 'noctis', 'paul', 'shaheen', 'steve', 'xiaoyu',
                   'yoshimitsu']

rbAddress = 'http://rbnorway.org/'
rbExtension = '-t7-frames/'

# in the format of frame data site
wikiCharacters = ['']

wikiAddress = 'https://tekken.fandom.com/wiki/'


class Tekken7App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Tekken 7 Frame Data')
        self.geometry('500x500')
        self.resizable(0, 0)

        # labels
        self.characterLb = tk.Label(self, text='Character')

        # drop downs
        self.charDropDownValue = tk.StringVar(self)
        self.charDropDownValue.set(dutchCharacters[0])    # set default value
        self.characterDropDown = tk.OptionMenu(self, self.charDropDownValue, *dutchCharacters)

        # entries

        # buttons
        self.getButton = tk.Button(self, text='Go', command=self.onGo)
        self.exitButton = tk.Button(self, text='Exit', command=self.onExit)

        # pack UI
        self.characterLb.pack()
        self.characterDropDown.pack()
        self.getButton.pack()
        self.exitButton.pack()

    def onGo(self):
        x = rbAddress + self.charDropDownValue.get() + rbExtension
        print(x)
        webpage = pagereader.requestPage(x)
        webpage = clean.cleanTable(str(webpage), self.charDropDownValue.get())
        print(webpage)

    def onExit(self):
        self.destroy()


# def run():
#     i = 0
#     count = len(characters)
#     for character in characters:
#         i += 1  # increment at the start so 1st loop is 1/40
#         page = 'http://rbnorway.org/'+character+'-t7-frames/'
#         link = page
#         page = requestPage(page)
#         page = str(page)
#         page = cleanTable(page, character)
#         exportToLog('processing: '+link+', '+str(i)+'/'+str(count))
#         exportToFile(page, 'C:\\temp', 'fd', 'csv')
