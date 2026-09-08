'''
Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without 
disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not. 

Constraints:
1 <= s.length <= 2000
s consists of lowercase English letters.
- HARD
'''
def main():
    arr = []
    soln = []
    s = "yezruvnatuipjeohsymapyxgfeczkevoxipckunlqjauvllfpwezhlzpbkfqazhexabomnlxkmoufneninbxxguuktvupmpfspwxiouwlfalexmluwcsbeqrzkivrphtpcoxqsueuxsalopbsgkzaibkpfmsztkwommkvgjjdvvggnvtlwrllcafhfocprnrzfoyehqhrvhpbbpxpsvomdpmksojckgkgkycoynbldkbnrlujegxotgmeyknpmpgajbgwmfftuphfzrywarqkpkfnwtzgdkdcyvwkqawwyjuskpvqomfchnlojmeltlwvqomucipcwxkgsktjxpwhujaexhejeflpctmjpuguslmzvpykbldcbxqnwgycpfccgeychkxfopixijeypzyryglutxweffyrqtkfrqlhtjweodttchnugybsmacpgperznunffrdavyqgilqlplebbkdopyyxcoamfxhpmdyrtutfxsejkwiyvdwggyhgsdpfxpznrccwdupfzlubkhppmasdbqfzttbhfismeamenyukzqoupbzxashwuvfkmkosgevcjnlpfgxgzumktsexvwhylhiupwfwyxotwnxodttsrifgzkkedurayjgxlhxjzlxikcgerptpufocymfrkyayvklsalgmtifpiczwnozmgowzchjiop"
    output = sequence(s)
    print(output)
  
def sequence(s):
    MOD = 10 ** 9 + 7
    count = 1
    previous = {}
    for char in s:
        old_count = count
        if char in previous:
            count = 2*count - previous[char]
        else:
            count = 2*count
        previous[char] = old_count
        count = count%MOD
    return (count-1) % MOD

main()


'''
s = "pcrdhwdxmqdznbenhwjsenjhvulyve"
soln = []
arr = []

for i in s:
    arr.append(i)
    if len(arr) >= 2:
        for j in range (0, len(arr)-1):
            seq = arr[j]+i
            if seq not in arr:
                arr.append(seq)

for i in arr:
    if i not in soln:
        soln.append(i)

print(soln, end="")'''
