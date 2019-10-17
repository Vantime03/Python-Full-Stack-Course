'''
Problem 3
Write a dictionary comprehension to swap keys and values of a given dictionary. So {'a': 1, 'b': 2} would become {1: 'a', 2: 'b'}.
'''
dict_s = { "a": 1, "b": 2}

def swap_dict_key():
    return {value: key for key, value in dict_s.items()}

def main():
    print(swap_dict_key())

main()

