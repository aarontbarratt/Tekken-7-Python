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
