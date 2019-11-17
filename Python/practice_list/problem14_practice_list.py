'''
Problem 14
Write a function which takes a list as a parameter and returns a new list with any duplicates removed.

def find_unique(nums):
    ...
nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique_nums = find_unique(nums) → [12, 24, 35, 88, 120, 155]
'''
nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

def find_unique(nums):
    unique = []
    for i in nums:
            if unique.__contains__(i):
                continue
            else: 
                unique.append(i)
    return unique


def main():
    unique_nums = find_unique(nums)
    print(f"Unique number: {unique_nums}")
main()
