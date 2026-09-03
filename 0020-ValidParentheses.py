'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type. - EASY
'''

def main():
    s = "{[(dfgfth)]}"
    print(validParentheses(s))

def validParentheses(s):
    arr = []
    for i in s:
        if i == "{" or i == "[" or i == "(":
            arr.append(i)
        elif i == "}" and arr[len(arr) - 1] == "{":
            arr.pop(len(arr) - 1)
        elif i == "]" and arr[len(arr) - 1] == "[":
            arr.pop(len(arr) - 1)
        elif i == ")" and arr[len(arr) - 1] == "(":
            arr.pop(len(arr) - 1)
    output = ""
    if arr == []:
        output = True
    else:
        output = False
    return output

main()
