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
    10: "ten",
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
    hundreds_digit = numb // 100
    tens_digit = (numb % 100) // 10 #if numb is 999, (999 % 100) // 10 = 9
    ones_digit = (numb % 100) % 10
    result = ""
    if numb in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
        return dict_one_digit.get(hundreds_digit) + " hundred"
    if 0 < hundreds_digit < 10:
        result += dict_one_digit.get(hundreds_digit) + " hundred "
    if tens_digit > 0 and tens_digit != 1:
        result += dict_10_digit.get(tens_digit) + " "
    elif tens_digit == 1:
        add = dict_10_digit.get(1)[numb % 100]
        print(add)
        result += add
        return result
    if ones_digit > 0: 
        result += dict_one_digit.get(ones_digit)
        return result

def main():
    print("Welcome to Number of phrase!")
    user_input = int(input("Enter an integer: "))
    result = convert_to_phrase(user_input)
    print(f"phrase for {user_input} is {result}")

main()


