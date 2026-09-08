'''
3. Longest Substring Without Repeating Characters - MED

Given a string s, find the length of the longest substring without duplicate characters.

Constraints:
0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces.
'''
def main():
    s = "abcgdyawight"
    output = longest_substring(s)
    print(output)

def longest_substring(s):
    seq = ""
    final_answer = ""
    for i in s:
        if i not in seq:
            seq = seq + i
        else:
            if len(seq) > len(final_answer):
                final_answer = seq
            seq = seq[seq.index(i) + 1:]
            seq = seq + i
    if len(seq) > len(final_answer):
        final_answer = seq
    return len(final_answer)

main()
