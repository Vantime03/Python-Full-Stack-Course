'''
Problem 3
Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

eveneven([5, 6, 2]) → True
eveneven([5, 5, 2]) → False
'''
ls1 = [5, 6, 2, 4, 6]
ls2 = [5, 5, 2]

def is_list_even(ls1):
    count = 0
    for i in ls1: 
        if i%2 == 0:
            count += 1
    return count % 2 == 0

def main():
    print(f"{is_list_even(ls1)}")

main()