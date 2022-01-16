# binarysearchlist.py
# contains a function for conducting a binary search through a sorted list
# In the binary sort, first check the middle number (pivot) of a list for a given target
# if the target equals the pivot, just return the pivot index/
# if the target is smaller than the pivot, search the left half [beginning of the list : pivot]
# if the target is larger than the pivot, search the right half [pivot: end of the list]
# Created by: William Shultz
# Date: January 15, 2022

def binarySearch(inputList: list, target: int) -> int:
    left = 0
    right = len(inputList) - 1

    while left <= right:
        pivot = left + (right - left) // 2
        if inputList[pivot] == target:
            return pivot
        elif target > inputList[pivot]:
            left = pivot + 1
        else:
            right = pivot - 1

    return -1

#testList = [-50,-27,-18,0,7,9,11,14,19,22,35,74,115]
#target = 19
#test = binarySearch(testList, target)
#print(f"The target number {target}, for list {testList} is in index {test}.")