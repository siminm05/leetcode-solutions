'''
35. Search Insert Position - EASY
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104
'''
def search_position(nums, target):
    start = 0
    end = len(nums) -1
    middle = 0
    found = False

    while found == False and start <= end:
        middle = (start + end)//2
        if nums[middle] == target:
            found = True
        else:
            if nums[middle] < target:
                start = middle+1
            else:
                end = middle-1
    if found:
        return middle
    else:
        return start

def main():
    #nums = [1,3,5,6], target = 2
    #nums = [1,3,5,6], target = 7
    nums = [1, 3, 5, 6]
    target = 5
    print(search_position(nums, target))

main()
