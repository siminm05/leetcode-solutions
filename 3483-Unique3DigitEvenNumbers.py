'''
3483. Unique 3-Digit Even Numbers - EASY
You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

Constraints:
- 3 <= digits.length <= 10
- 0 <= digits[i] <= 9

'''
s = [2,0,2] #[1,3,5] [1,2,3,4], [6,6,6]
arr = []

for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            if i != j and j != k and i != k:
                num = str(s[i]) + str(s[j]) + str(s[k])
                num_string = int(num)
                if num_string % 2 == 0 and len(str(num_string)) == 3 and num not in arr:
                    arr.append(num)

print(arr)
print(len(arr))




