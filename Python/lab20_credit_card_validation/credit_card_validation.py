'''
Lab 20: Credit Card Validation
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Convert the input string into a list of ints
1. Slice off the last digit. That is the check digit.
2. Reverse the digits.
3. Double every other element in the reversed list.
4. Subtract nine from numbers over nine.
5. Sum all values.
6. Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
Valid!
'''
import string

def check_for_spaces_string(card_numb):
    card_numb = card_numb.replace(" ", "")#remove spaces
    for ind in card_numb: #check for string
        if ind not in string.digits:
            print("This is an invalid number! Enter number only!")
            return getting_card_number()
    return card_numb

def slice_last_digit(card_numb):
    list_numb = list(card_numb)
    del list_numb[-1]
    return list_numb

def reverse_digits(card_numb):
    rev_numb = []
    for n in range (len(card_numb)):
        rev_numb += card_numb[-(n+1)]
    return rev_numb

def double_reverse_list(card_numb):
    for n in range (len(card_numb)):
        card_numb[n] = int(card_numb[n])
    for n in range (0, len(card_numb), 2):
        card_numb[n] = card_numb[n] * 2
    return card_numb

def subtract_nine_over_nine(card_numb):
    for n in range (len(card_numb)):
        if card_numb[n] > 9:
            card_numb[n] = card_numb[n] - 9
    return card_numb

def sum_all_values(card_numb):
    sum = 0
    for n in card_numb: 
        sum += n
    return sum


def getting_card_number():
    card_numb = ""
    card_numb = input("\nEnter your 16 digits credit card number with no spaces: ")
    card_numb = check_for_spaces_string(card_numb) #remove spaces and check for strings from card_numb
    return card_numb

def check_digit_checking(sum, card_numb_string):
    sum = str(sum)
    if sum[-1] == card_numb_string[-1]:
        return "Valid!"
    else: 
        return "Not Valid!"

def main():
    print("Welcome to Credit Card Validation!")
    card_numb_string = getting_card_number()
    card_numb = slice_last_digit(card_numb_string) # slice last digit
    card_numb = reverse_digits(card_numb) #reverse number
    card_numb = double_reverse_list(card_numb)#convert str int list and double digits
    card_numb = subtract_nine_over_nine(card_numb) #Subtract nine from numbers over nine
    sum = sum_all_values(card_numb) #sum all values
    is_valid = check_digit_checking(sum, card_numb_string)
    print(is_valid)

main()
