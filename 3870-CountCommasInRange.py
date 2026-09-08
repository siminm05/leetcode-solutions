'''
You are given an integer n.
Return the total number of commas used when writing all integers from [1, n] (inclusive) in 
standard number formatting.

In standard formatting:
A comma is inserted after every three digits from the right.
Numbers with fewer than 4 digits contain no commas.

Constraints:
1 <= n <= 105
- EASY
'''
def main():
    n = 100000
    output = countCommas(n)
    print(output)

def countCommas(n):
    count = n - 999
    if count <= 0:
        return 0
    else:
        return count

main()
