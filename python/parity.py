#The parity of a given number can be found by the following method:
#   - if the number of ones in a number's binary representaion is odd, it has a parity of 1
#   - if the number of ones in a number's binary representation is even, it has a parity of 0
#

def getParity(num: int) -> int:
    parity = 0
    while num:
        parity ^= num & 1
        num >>= 1


    return parity


def testGetParity():
    for x in range(10):
        print(f"Parity of {x}: {getParity(x)}")

#testGetParity()

