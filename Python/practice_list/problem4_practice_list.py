'''
Problem 4
Print out every other element of a list, first using a while loop, then using a for loop.

>>> nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> print_every_other(nums)
0, 2, 4, 6, 8
'''
def generate_every_other_element_from_a_list():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    return [nums[i] for i in range(len(nums)) if i%2 == 1]

def main():
    print(generate_every_other_element_from_a_list())

main()
