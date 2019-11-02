'''
Problem 4
Write a dictionary comprehension to print each letter of the alphabet and its correstponding ASCII code (check out ord)

{'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, ...}
'''
import string

def dict_ascii_alphabet():
    return {n: ord(n) for n in string.ascii_lowercase}

def main():
    print(dict_ascii_alphabet())

main()