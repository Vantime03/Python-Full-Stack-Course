'''
Problem 1
Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.

def random_element(a):
    ...

fruits = ['apples', 'bananas', 'pears']
random_element(fruits) could return 'apples', 'bananas' or 'pears'
'''
import random
fruits = ['apples', 'bananas', 'pears']

def random_element(fruits):
    x = random.randint(0, len(fruits)-1)
    return fruits[x]


def main():
    print(f"Result from random: {random_element(fruits)}")

main()