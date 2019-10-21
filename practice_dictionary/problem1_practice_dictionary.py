'''
Problem 1
Given a the two lists below, combine them into a dictionary.

def combine(a, b):
    ...
fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]
combine(fruits, prices) -> {'apple':1.2, 'banana':3.3, 'pear':2.1}
'''
prices = [1.2, 3.3, 2.1]
fruits = ['apple', 'banana', 'pear']

def combine():
    fruit_price_dict = {}
    for i in range(len(fruits)):
        fruit_price_dict[fruits[i]] = prices[i]
    return fruit_price_dict

def main():
    print(f"Dictionary for Fruit-Price: {combine()}")

main()