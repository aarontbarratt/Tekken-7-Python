
def cleanSQL(result):
    result = result[1:len(result) - 1]  # removes the () from around the result
    return result
