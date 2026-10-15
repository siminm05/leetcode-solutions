'''
28. Find the Index of the First Occurrence in a String - EASY

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Constraints:
-1 <= haystack.length, needle.length <= 104
-haystack and needle consist of only lowercase English characters.
'''

def first_index(haystack, needle):
    if len(haystack) >= len(needle) and len(needle) != 0:
        for i in range(len(haystack) - len(needle) + 1):
            string = ""
            j = i
            if haystack[i] == needle[0]:
                while len(string) < len(needle):
                    string += haystack[j]
                    j += 1
                if string == needle:
                    return i
        return -1
    else:
        return -1


def main():
    # haystack = "leetcode", needle = "leeto"  ||  haystack = "sadbutsad", needle = "sad"
    haystack = "mississippi"
    needle = "issip"
    print(first_index(haystack, needle))


main()
