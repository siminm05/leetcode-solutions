'''
3550. Smallest Index With Digit Sum Equal to Index - EASY

You are given an integer array nums.
Return the smallest index i such that the sum of the digits of nums[i] is equal to i.
If no such index exists, return -1.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000
'''

def main():
    nums = [1,2,3] #[1,3,2]   [1,10,11]
    output = smallestIndex(nums)
    print(output)

def smallestIndex(nums):
    sum = 0
    for i in range(len(nums)):
        for j in str(nums[i]):
            sum += int(j)
        if sum == i:
            return i
        sum = 0
    if i == len(nums)-1:
        return -1

main()
