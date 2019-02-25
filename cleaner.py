
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
