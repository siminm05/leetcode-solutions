'''
125. Valid Palindrome - EASY
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and
backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Constraints:
- 1 <= s.length <= 2 * 105
- s consists only of printable ASCII characters.
'''

from string import ascii_lowercase

def palindrome(s):
    string = ""
    if len(s) >= 1:
        for i in s:
            if i.lower() in ascii_lowercase or i.isdigit():
                string = string+i.lower()
        reverse = string[::-1]
        if reverse == string:
            return True
        else:
            return False
    else:
        return False

def main():
    #s = "A man, a plan, a canal: Panama"
    #s = "race a car"
    #s = "0p"
    s = " "
    print(palindrome(s))

main()
