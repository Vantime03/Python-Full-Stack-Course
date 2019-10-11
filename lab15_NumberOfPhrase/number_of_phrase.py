'''
Lab 15: Number to Phrase
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint 2: use the digit as an index for a list of strings.

'''
dict_10_to_19 = {
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}
dict_one_digit = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
dict_10_digit = {
    1: dict_10_to_19,
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}
def convert_to_phrase(numb):
    tens_digit = numb // 10
    ones_digit = numb % 10
    if numb < 10:
        return dict_one_digit.get(numb)
    elif 10 <= numb < 20:
        return dict_10_digit.get(tens_digit)[numb]
    else:
        return dict_10_digit.get(tens_digit) + "-" + dict_one_digit.get(ones_digit)

def main():
    print("Welcome to Number of phrase!")
    user_input = int(input("Enter an integer: "))
    print(f"phrase for {user_input} is {convert_to_phrase(user_input)}")

main()
