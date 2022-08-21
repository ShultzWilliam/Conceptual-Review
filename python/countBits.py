# Write a function that returns the number of 1 bits for a given int when that int is represented in binary
# Example countBits(12) -> 3  : 3 1's in 1110
#
# Input: num : int
# Output: int

def countBits(num: int) -> int:
    count = 0
    while num:
        count += num & 1
        num >>= 1

    return count


for x in range(17):
    print(str(countBits(x)))
