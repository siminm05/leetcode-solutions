'''
3524. Find X Value of Array I - MED

You are given an array of positive integers nums, and a positive integer k.
You are allowed to perform an operation once on nums, where in each operation you can remove any non-overlapping prefix and suffix from nums such that nums remains non-empty.
You need to find the x-value of nums, which is the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x when divided by k.
Return an array result of size k where result[x] is the x-value of nums for 0 <= x <= k - 1.
A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.
A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.
Note that the prefix and suffix to be chosen for the operation can be empty.

Constraints:
- 1 <= nums[i] <= 109
- 1 <= nums.length <= 105
- 1 <= k <= 5
'''

nums = [1,2,3,4,5]    #nums = [1,1,2,1,1]  k = 2, nums = [1,2,4,8,16,32]  k = 4
k = 3
counter = [0] * k
previous = [0] * k

for i in nums:
    current = [0] * k
    remainder = i % k
    current[remainder] += 1

    for l in range(k):
        new_remainder = (l * i) % k
        current[new_remainder] += previous[l]
    for l in range(k):
        counter[l] += current[l]
    previous = current

print(counter)


'''
nums = [1,2,3,4,5]
k = 3
counter = [0] * k
for i in range(len(nums)):
    j = i
    product = 1
    while j < len(nums):
        product = product * nums[j]
        remainder = product % k
        j += 1
        for m in range(len(counter)):
            if remainder == m:
                counter[m] += 1
print(counter)
'''
