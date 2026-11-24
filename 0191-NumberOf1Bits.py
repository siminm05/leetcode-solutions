'''
191. Number of 1 Bits - EASY
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

Constraints:
- 1 <= n <= 231 - 1
'''

def num_0f_1_bits(n):
  binary = 2**31
  ans = ""
  while binary >= 1:
      if n >= binary:
          n = n - binary
          ans = ans + "1"
      else:
          ans = ans + "0"
      binary = binary/2
  #print(ans)
  
  count=0
  for i in str(ans):
      if i == "1":
          count += 1
  
  return count

def main():
  # n = 2147483645, n = 128, n = 11
  n = 8

main()
