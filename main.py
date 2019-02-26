import urllib.request
from cleaner import cleanTable
from export import createCsv

characters = ['akuma', 'alisa', 'anna', 'armor-king', 'asuka', 'bob', 'bryan', 'claudio', 'devil-jin', 'dragunov',
              'eddy', 'eliza', 'feng', 'geese', 'gigas', 'heihachi', 'hwoarang', 'jack7', 'jin', 'josie', 'katarina',
              'kazumi', 'kazuya', 'lars', 'lei', 'law', 'lee', 'leo', 'lili', 'lucky-chloe', 'marduk', 'master-raven',
              'miguel', 'nina', 'noctis', 'paul', 'shaheen', 'steve', 'xiaoyu', 'yoshimitsu']


def main():
    for x in range(len(characters)):
        page = urllib.request.urlopen('http://rbnorway.org/'+str(characters[x])+'-t7-frames/')
        print(characters[x])
        page = str(page.read())
        page = cleanTable(page, characters[x])
        createCsv(page, characters[x], True)


def getCharacters():
    for x in range(len(characters)):
        y = characters[x]
        print(y)


main()
