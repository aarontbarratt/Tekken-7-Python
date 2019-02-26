
def left(string, number):
    string = str(string)
    string = string[:number]
    return string


def right(string, number):
    string = str(string)
    string = string[len(string) - number:]
    return string


def leftright(string, lnum, rnum):
    string = str(string)
    string = left(string, lnum)
    string = right(string, rnum)
    return string


def ltrim(string, number):
    string = str(string)
    string = string[number:]
    return string


def rtrim(string, number):
    string = str(string)
    string = string[:len(string)-number]
    return string


def lrtrim(string, l, r):
    string = str(string)
    string = string[l:]
    string = string[:len(string) - r]
    return string


# cleans and splits table data from RB Norway's site
def cleanTable(string, character):
    string = string[string.find("<table"):string.find("</table")]       # find everything between the <table>
    string = string.replace('</tr>', '\n')                              # break the line at the end of every row
    string = string.replace('\\n', '')                                  # remove html new line tag
    string = string.replace('<tr BGCOLOR="LightGray">', '')             # remove alternating gray <tr> tags
    string = string.replace('<tr>', '')                                 # remove plain <tr> tags
    string = string.replace('<b>', '')                                  # removes <b> tags
    string = string.replace('</b>', '')                                 # removes <b> tags
    string = string.replace('</td><td>', '","')                         # splits between <td> values with ","
    string = string.replace('<table border="1"><td>', '"character","')  # replaces first header position to character
    string = string.replace('<td>', '"'+character+'","')                # places the character name at the front
    string = string.replace('</td>', '"')                               # remove final </td> from each line
    string = string.replace('&#8211;', '')                              # replace hex - with nothing
    string = string.replace('<br />', '')                               # remove break line tags from <td>
    string = string.replace('\\xef\\xbd\\x9e', '~')                     # replace hex value for ~
    return string
