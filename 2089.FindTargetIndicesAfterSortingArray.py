'''
2089. Find Target Indices After Sorting Array - EASY

You are given a 0-indexed integer array nums and a target element target.
A target index is an index i such that nums[i] == target.
Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. 
The returned list must be sorted in increasing order.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i], target <= 100
'''

def target_index(nums, target):
    nums = sorted(nums)
    list = []
    for i in range(len(nums)):
        if target == nums[i]:
            list.append(i)

    return list

def main():
    nums = [1,2,5,2,3]
    target = 4           # target = 2  ||  target = 3
    print(target_index(nums, target))

main()
