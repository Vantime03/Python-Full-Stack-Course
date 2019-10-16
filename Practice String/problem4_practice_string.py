'''
Write a function that returns the number of occurances of 'hi' in a given string.

count_hi('hihi') → 2

'''
import string

def count_hi(input_str):
    return input_str.count("hi")
    
def main():
    input_str = (input("Type \"hi\" multiple times: ")).lower()
    input_str = input_str.replace(" ", "")
    print(f"number of hi: {count_hi(input_str)}")

main()

