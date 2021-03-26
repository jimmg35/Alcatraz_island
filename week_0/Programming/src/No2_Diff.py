
# Author : @jimmg35
# using python typing module for static check
# python 3.7.3

X: int = 10
P: int = -2

def myPower(num: int,idx: int) -> int:
    if(idx==1):
       return(num)
    else:
       return(num*myPower(num,idx-1))

if P < 0:
    print(P * 1 / myPower(X, -(P-1)))
elif P == 0:
    print(0)
else:
    if (P-1) == 0:
        print(1)
    else:
        print(P * myPower(X, P-1))
