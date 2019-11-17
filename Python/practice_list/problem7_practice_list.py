'''
Problem 7
Write a function to find all common elements between two lists.

def common_elements(nums1, nums2):
'''
nums1 = ["hello", 1, 14, "world", "Yo!"]
nums2 = ["hello", 14, 50, 100, "Cool"]

def common_elements(nums1, nums2):
    ls = []
    [ls.append(n) for n in nums1 for i in nums2 if n == i]
    return ls

def main():
    print(f"Common elements from {nums1} and {nums2} are: {common_elements(nums1, nums2)}")
main()
