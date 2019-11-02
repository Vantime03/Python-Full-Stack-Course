'''
Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.

fibonacci(8) → [1, 1, 2, 3, 5, 8, 13, 21]
'''
import math

def fibonacci(count):
    result = [1, 1]
    
    for n in range (100):
        if n >= result[-1] and  (result[-1] + result[-2]) == n:
            result.append(n) 
            if len(result) == count:
                break
    return result



def main():
    n = int(input("Enter an integer from 2 to 11 for fibonacci: "))
    print(f"fibonacci for {n} is: {fibonacci(n)}")

main()

