'''
67. Add Binary - EASY

Given two binary strings a and b, return their sum as a binary string.

Constraints:
- 1 <= a.length, b.length <= 104
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.
'''

# 0 1 10 11 100 101 110 111
def decimal(num):
    if num == 0 or num == 1:
        return str(num)
    else:
        list = []
        while num >= 1:
            list.append(num % 10)
            num = num//10

        sum = 0
        for i in range(len(list)):
            if list[i] == 1:
                sum = sum + 2**i

        return sum

def binary_sum(a,b):
    decimal_a = decimal(a)
    decimal_b = decimal(b)
    sum = decimal_a + decimal_b

    if sum == 0 or sum == 1:
        return sum
    else:
        list = []
        while sum > 0:
            list.append(sum % 2)
            sum = sum // 2

        string = ""
        for i in list:
            string = str(i) + string

        return string


def main():
    # a = "1010", b = "1011"
    a = 11
    b = 1
    print(binary_sum(a,b))

main()
