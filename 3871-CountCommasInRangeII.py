'''
3871 - Count Commas in Range II - MED

You are given an integer n.
Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.
In standard formatting:
- A comma is inserted after every three digits from the right.
- Numbers with fewer than 4 digits contain no commas.

Constraints:
1 <= n <= 1015
'''
def main():
    #s = 1,000,000,000,000,000
    s = 1000000000000000
    output = countCommas(s)
    print(output)

def countCommas(s):
    length = len(str(s))
    commas = 0
    if length <= 3:
        return 0
    elif length <= 6:
        return s - 999
    elif length <= 9:
        commas = 999000 + 2*(s - 999999)
        return commas
    elif length <= 12:
        commas = 999000 + 1998000000 + 3*(s - 999999999)
        return commas
    elif length <= 15:
        commas = 999000 + 1998000000 + 2997000000000 + 4*(s - 999999999999)
        return commas
    elif length == 16:
        return 3998998998999005

main()
