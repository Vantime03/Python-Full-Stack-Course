'''
Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.

nums = [[5,2,3],[4,5,1],[7,6,3]]
combine_all(nums) → [5,2,3,4,5,1,7,6,3]
'''
nums = [[5,2,3],[4,5,1],[7,6,3]]
result = []

def combine_all(nums):
    [result.append(n) for i in nums for n in i]
    return result
    
def main():
    print(f"Result: {combine_all(nums)}")

main()

