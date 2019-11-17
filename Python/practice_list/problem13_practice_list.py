'''
Problem 13
Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.
'''
nums = [12, 45, 36, 66, 66, 245, 66, 11, 33, 44, 55, 66, 45, 45]


def minimum(nums):
    result = maximum(nums)
    for n in nums:
        if n < result:
            result = n
    return result

def maximum(nums):
    result = 0
    for n in nums:
        if n > result:
            result = n
    return result

def mean(nums):
    result = 0
    for n in nums:
        result+= n
    return result/(len(nums))

def mode(nums):
    result = {}
    max = 0
    for n in nums:
        if nums.count(n) > 2:
            result[n] = nums.count(n)
    for n in result:
        if n > max:
            max = n
    return max

def main():
    print(f"maximum: {maximum(nums)}\nminimum: {minimum(nums)}\nmean: {mean(nums)}\nmode: {mode(nums)}")

main()