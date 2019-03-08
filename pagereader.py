import urllib.request

import cleaner as clean
import export

wiki = 'https://tekken.fandom.com/wiki/'
charactersWiki = ['Bryan_Fury', 'Yoshimitsu']


# returns html in single line
def requestPage(webpage):
    w = webpage
    w = urllib.request.urlopen(w)
    w = w.read()
    return w


# for each character request character wiki page
def main():
    for character in charactersWiki:
        print(wiki+character)
        page = requestPage(wiki+character)
        page = str(page)
        page = clean.leftright(page, page.find('<aside '), page.find('</aside>'))
        page = page.replace('\\n\\n', '')
        page = page.replace('\\n', '\n')
        page = page.replace('\\t', '  ')
        page = page.replace('<br />', '\n')
        export.exportToFile(page, 'C:\\temp', character, '.html')
