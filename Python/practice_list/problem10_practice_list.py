'''
Problem 10
Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

merge([5,2,1], [6,8,2]) → [[5,6],[2,8],[1,2]]
'''
ls1 = [5,2,1]
ls2 = [6,8,2]
result = []
def merge_pair(ls1, ls2):
    for i in range (len(ls1)):
        ls = []
        ls.append(ls1[i])
        ls.append(ls2[i])
        result.append(ls)
    return result

def main(): 
    print(merge_pair(ls1, ls2))

main()

    