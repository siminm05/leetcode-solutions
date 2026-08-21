'''You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.
Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. 
At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. 
The player adds the chosen number to their score. The game ends when there are no more elements in the array.
Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. 
You may assume that both players are playing optimally. - MED'''

import random
def main():
    #nums = random.sample(range(1, 11), 4)
    nums = [1,5,233,7]
    print("Input: nums =", nums)
    print("Output: ", winner(nums), sep="")

def winner(nums):
    winning_diff = minimax(nums, 0, len(nums)-1)
    if winning_diff >= 0:
        return True
    else:
        return False
def minimax(nums, left, right):
    if left == right:
        return nums[left]

    go_left = nums[left] - minimax(nums, left+1, right)
    go_right = nums[right] - minimax(nums, left, right-1)

    if go_left >= go_right:
        return go_left
    else:
        return go_right

main()
