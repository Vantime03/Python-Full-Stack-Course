'''
Lab 10: Average Numbers
We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.
'''
# def process_sum():

def take_user_inputs():
    number_list = []
    add_a_number = True
    while add_a_number:
        number = input("Enter a number, or 'done': ")
        if number != "done":
            number_list.append(int(number))
        else:
            return number_list

def average(user_input_list):
    sum = 0
    for n in user_input_list:
        sum += n

    return sum / len(user_input_list)

def main():
    print("Welcome to Average Numbers! This app will allow you to average a list of numbers.")
    user_input_list = take_user_inputs()
    result_average = average(user_input_list)

    print(f"The average of this list of numbers {user_input_list} is {result_average}")

main()
