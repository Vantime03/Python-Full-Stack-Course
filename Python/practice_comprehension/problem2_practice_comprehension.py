'''
Problem 2
Write a comprehension to generate the first 10 even numbers.
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''
def generate_first_10_even():
    return [n for n in range(21) if n%2 == 0]

def main():
    print(f"Even number: {generate_first_10_even()}")
main()