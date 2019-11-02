'''
Problem 7
Convert input strings to lowercase without any surrounding whitespace.

lower_case("SUPER!") → 'super!'
lower_case("        NANNANANANA BATMAN        ") → 'nannananana batman'

'''
def lower_str(input_str):
    return input_str.lower()

def strip_str(input_str):
    return input_str.strip()

def main():
    input_str = input("Enter a string with whitespaces or/and capitalized: ")
    input_str = lower_str(input_str)
    input_str = strip_str(input_str)
    print(f"Result: {input_str}")

main()
