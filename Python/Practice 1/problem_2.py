'''
problem 2

Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.

def opposite(a, b):
    ...
opposite(10, -1) → True
opposite(2, 3) → False
opposite(-1, -1) → False

'''
def opposite(numb1, numb2):
    if numb1 > 0 and numb2 < 0:
        return True
    elif numb1 < 0 and numb2 > 0: 
        return True
    else:
        return False

def main():
    print("Note: this will determine if one integer is positive and one is negative.\n")
    numb1 = int(input("Enter first integer (e.g. 5): "))
    numb2 = int(input("Enter second integer (e.g. 5): "))
    is_opposite = opposite(numb1, numb2)
    print(f"Opposite is {is_opposite}")

main()