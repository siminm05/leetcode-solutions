'''
Seven different symbols represent Roman numerals with the following values:

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral. - MED
'''
def seperating_numbers(num):
    string = str(num)
    reverse = string[::-1]
    seperate_number = []
    for zero, i in enumerate(reverse):
        # print("Index of:", i, zero)
        newNum = ""
        zerocount = ""
        for j in range(zero):
            zerocount = zerocount + "0"
            # print("Number of zero in", i, "is", zerocount)
        newNum = i + zerocount
        seperate_number.append(newNum)
    trueNumber = seperate_number[::-1]
    return trueNumber

def main():
    num = 1996
    trueNumber = seperating_numbers(num)
    output = ""
    for i in trueNumber:
        roman_string = romanNumber(i)
        output = output + roman_string
    print("Output:", output)

def romanNumber(i):
    roman_string = ""
    string_i = str(i)
    if string_i.startswith(("4", "9")):
        if string_i == "4":
            roman_string = "IV"
        elif string_i == "9":
            roman_string = "IX"
        elif string_i == "40":
            roman_string = "XL"
        elif string_i == "90":
            roman_string = "XC"
        elif string_i == "400":
            roman_string = "CD"
        elif string_i == "900":
            roman_string = "CM"
    else:
        i = int(string_i)
        while i != 0:
            if i >= 1000:
                roman_string = roman_string + "M"
                i = i - 1000
            elif i >= 500:
                roman_string = roman_string + "D"
                i = i - 500
            elif i >= 100:
                roman_string = roman_string + "C"
                i = i - 100
            elif i >= 50:
                roman_string = roman_string + "L"
                i = i - 50
            elif i >= 10:
                roman_string = roman_string + "X"
                i = i - 10
            elif i >= 5:
                roman_string = roman_string + "V"
                i = i - 5
            elif i >= 1:
                roman_string = roman_string + "I"
                i = i - 1
    return roman_string

main()
