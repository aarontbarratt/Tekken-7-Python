import os

import ui

paths = ['C:\\Tekken 7 Frame Data', 'C:\\Tekken 7 Frame Data\\export', 'C:\\Tekken 7 Frame Data\\logs']
rootPath = paths[0]
exportPath = paths[1]
logPath = paths[2]


def makeDirectory(_path_):
    p = _path_
    try:
        os.mkdir(p)
    except OSError:
        if os.path.isdir(p):
            print(p + ' already exists')
        else:
            print(OSError)
    else:
        print('Created Path: ' + p)


def main():
    for path in paths:
        makeDirectory(path)
    app = ui.Tekken7App()
    app.mainloop()


main()
