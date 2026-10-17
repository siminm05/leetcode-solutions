'''
66. Plus One - EASY

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Constraints:
- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- digits does not contain any leading 0's.
'''

def plus_one(digits):
    num = ""
    sum = 1
    for i in digits:
        num += str(i)
    sum += int(num)

    str_sum = str(sum)
    digits = [0] * len(str_sum)
    for i in range(len(str_sum)):
        digits[i] = int(str_sum[i])

    return digits

def main():
    digits = [4,3,2,1]  #[1,2,3]   [9]
    print(plus_one(digits))

main()
