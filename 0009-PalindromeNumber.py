'''Given an integer x, return true if x is a palindrome, and false otherwise. - EASY'''

def palindrome(x):
    reverse = ""
    for i in str(x):
        reverse = i + reverse

    return str(x) == reverse

#reverse = x[::-1] - another way to reverse

def main():
    x = -151
    output = (palindrome(x))
    print("Int:", x, "\nOutput:", output)

main()
