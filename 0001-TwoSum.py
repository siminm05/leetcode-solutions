'''You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. - EASY'''

import random
def main():
    #nums = random.sample(range(1, 11), 4)
    nums = [3,3]
    print("Input: nums =", nums)
    target = 6
    print(winner(nums,target))


def winner(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    return i, j

main()
