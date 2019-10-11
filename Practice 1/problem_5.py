'''
Problem 5:

Print out the powers of 2 from 2^0 to 2^20

1, 2, 4, 8, 16, 32, ...
'''

def power_of_2(i):
    return 2**i

def main():
    for i in range (0, 20):
        result = power_of_2(i)
        print(f"2^{i} = {result}")

main()
