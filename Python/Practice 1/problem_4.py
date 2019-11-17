'''
Problem 4
Write a function that returns the maximum of 3 parameters.

def maximum_of_three(a, b, c):
    ...
maximum_of_three(5,6,2) → 6
maximum_of_three(-4,3,10) → 10
'''

#This problem will solve the average of three numbers

def average_three (numb1, numb2, numb3):
    return ((numb1+numb2+numb3) / 3)

def main():
    numb1 = int(input("Enter the first number: "))
    numb2 = int(input("Enter the second number: "))
    numb3 = int(input("Enter the third number: "))
    print(f"The average of {numb1}, {numb2}, {numb3} is {average_three(numb1,numb2,numb3)}")

main()
    

    