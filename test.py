
# aaron = 28500
# leanne = 22000
#
# whole = float(aaron) + float(leanne)
# aaronPercent = aaron / whole * 100
# leannePercent = leanne / whole * 100
#
# print(aaronPercent)
# print(leannePercent)
#
# bill = 120
#
# a = bill / 100 * leannePercent
# print(a)
#
# b = bill / 100 * aaronPercent
# print(b)
#
# print(a + b)


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


def main():
    x = calcPayment(28500, 22000, 1300)
    print(x)


main()
