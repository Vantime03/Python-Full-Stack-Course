'''
Problem 5
Write a function that returns the reverse of a list.

def reverse(nums):
'''
nums = [1,2,3,4,5]
def reverse(nums):
    ls = []
    [ls.append(nums[-i]) for i in range(1, len(nums) + 1)]
    return ls 

def main():
    print(reverse(nums))
main()