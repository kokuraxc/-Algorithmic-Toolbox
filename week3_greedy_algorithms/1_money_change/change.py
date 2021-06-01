# Uses python3
import sys

def getCoins(amount, denomination):
    return divmod(amount, denomination)

def get_change(m):
    #write your code here
    noCoin10, rem = getCoins(m, 10)
    noCoin5, rem = getCoins(rem, 5)
    noCoin1 = rem

    return noCoin10 + noCoin5 + noCoin1

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
