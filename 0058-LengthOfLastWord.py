'''
58. Length of Last Word - EASY

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Constraints:
- 1 <= s.length <= 104
- s consists of only English letters and spaces ' '.
- There will be at least one word in s.
'''

def len_of_last_word(s):
    list = s.split()
    return len(list[-1])

def main():
    s = "Hello World"
    print(len_of_last_word(s))

main()
