
# Author : @jimmg35
# using python typing module for static check
# python 3.7.3


def checkNarciss(num: int) -> bool:
    if ((num//100)**3 + (num//10 % 10)**3 + (num%10)**3) == num:
        return True

for i in range(100, 1000):
    if checkNarciss(i):
        print("{} is Narcissistic number!".format(i))
    