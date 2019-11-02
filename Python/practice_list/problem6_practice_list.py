'''
Problem 6
Write a function to move all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
'''
nums = [1, 2, 3, 5, 7, 10, 13, 14, 16]

def extract_less_than_ten(nums):
    ls = [i for i in nums if i < 10]
    return ls
    
def main():
    print(f"Numbers are less than 10: {extract_less_than_ten(nums)}")

main()