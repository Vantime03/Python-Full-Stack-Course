'''
Problem 8
Write a function to combine two lists of equal length into one, alternating elements.

def combine(nums1, nums2):
    ...
combine(['a','b','c'],[1,2,3]) → ['a', 1, 'b', 2, 'c', 3]
'''
ls1 = ['a','b','c']
ls2 = [1,2,3]

def combine (ls1, ls2):
    ls = []
    for i in range(len(ls1)):
        ls.append(ls1[i])
        ls.append(ls2[i])
    return ls 
    
def main():
    print(f"The combine list is: {combine(ls1, ls2)}")

main()