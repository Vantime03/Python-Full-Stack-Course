'''
Problem 1
Write a comprehension to generate the first 10 powers of two.

[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
'''
def generate_power_of_two():
    return [2**n for n in range(0,10)]
def main():
    print(f"Result of first 10 powers of two: {generate_power_of_two()}")


main()