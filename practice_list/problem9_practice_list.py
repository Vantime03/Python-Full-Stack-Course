'''
Problem 9
Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number

nums = [5, 6, 2, 3]
target = 7
find_pair(nums, target) → [5, 2]
Optional: return a list of all pairs of numbers that sum to a target value.
'''
nums = [5, 6, 3,1]
target = 7

def find_pairs(nums, target):
    pair = []
    for n in range(len(nums)):
        for i in range (len(nums)):
            if n != i and (nums[n] + nums[i] == 7):
                pair.append(nums[n])
    return pair

def main():
        print(f"Pairs that add up to {target} is: {find_pairs(nums, target)}")
main()