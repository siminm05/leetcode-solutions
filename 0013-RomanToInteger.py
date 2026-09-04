'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. - EASY
'''

def main():
    roman_num = "MCMXCIV"
    number_arr = []
    for i in roman_num:
        if i == "I":
            number_arr.append(1)
        elif i == "V":
            number_arr.append(5)
        elif i == "X":
            number_arr.append(10)
        elif i == "L":
            number_arr.append(50)
        elif i == "C":
            number_arr.append(100)
        elif i == "D":
            number_arr.append(500)
        elif i == "M":
            number_arr.append(1000)

    #print(number_arr)

    for i in range(len(number_arr)-1):
        if number_arr[i] == 1:
            if number_arr[i+1] == 5:
                number_arr[i] = 4
                number_arr[i+1] = 0
            elif number_arr[i+1] == 10:
                number_arr[i] = 9
                number_arr[i+1] = 0
        elif number_arr[i] == 10:
            if number_arr[i+1] == 50:
                number_arr[i] = 40
                number_arr[i+1] = 0
            elif number_arr[i+1] == 100:
                number_arr[i] = 90
                number_arr[i+1] = 0
        elif number_arr[i] == 100:
            if number_arr[i+1] == 500:
                number_arr[i] = 400
                number_arr[i+1] = 0
            elif number_arr[i+1] == 1000:
                number_arr[i] = 900
                number_arr[i+1] = 0
    #print(number_arr)

    sum = 0
    for i in number_arr:
        sum = sum+ i

    print(sum)

main()
