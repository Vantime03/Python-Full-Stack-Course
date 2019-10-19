'''
Lab 25: ATM
Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
calc_interest() returns the amount of interest calculated on the account
'''
class ATM:
    def __init__(self, name, balance, interest):
        self.name = name
        self.balance = balance
        self.interest = interest
    
    def check_balance(self):
        return self.balance
       
    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        return self.balance
    
    def check_withdrawal(self, withdraw_amt):
        if self.balance < withdraw_amt:
            return True
        else: 
            return False

    def withdraw(self, withdraw_amt):
        if self.balance > withdraw_amt:
            self.balance = self.balance - withdraw_amt
            return self.balance
        else:
            print("This will bring a negative balance !!!")

    def calc_interest(self):
        return self.balance * self.interest

def main():
    p1 = ATM('Van', 100, .001)
    p2 = ATM('Justin', 1000, .001)
    
    #check balance
    print(f'The balance for {p1.name}\'s account is {p1.check_balance()}')
    print(f'The balance for {p2.name}\'s account is {p2.check_balance()}')

    #deposit $100 for each account
    deposit_amount = 100
    print(f'After deposited ${deposit_amount}, the balance for {p1.name}\'s account is {p1.deposit(deposit_amount)}')
    print(f'After deposited ${deposit_amount}, the balance for {p2.name}\'s account is {p2.deposit(deposit_amount)}')
    print(p1.balance)

    #check withdrawal
    withdraw_amt = 300
    print(f'If {p1.name} withdraws ${withdraw_amt}, it is {p1.check_withdrawal(withdraw_amt)} that the balance will be negative.')
    print(f'If {p2.name} withdraws ${withdraw_amt}, it is {p2.check_withdrawal(withdraw_amt)} that the balance will be negative.')

    #withdraw amount 
    withdraw_amt = 150
    print(f'After {p1.name} withdrew ${withdraw_amt}, the balance is {p1.withdraw(withdraw_amt)}')
    print(f'After {p2.name} withdrew ${withdraw_amt}, the balance is {p2.withdraw(withdraw_amt)}')

    #calculate interest amount
    print(f'With the annual interest rate of {p1.interest} and a balance of ${p1.balance}, the total interest amount is ${round(p1.calc_interest(), 2)}')
    print(f'With the annual interest rate of {p2.interest} and a balance of ${p2.balance}, the total interest amount is ${round(p2.calc_interest(), 2)}')
    
    













    # user_account = {}
    # print("Welcome to ATM demo!\n")
    # user_name = input("Enter your name to create an account: ")
    # Is_deposit = (input(f"{user_name}, Your balance is currently $0. Would you like to make a deposit (y/n)? ")).lower()
    # if Is_deposit in ["y", "yes"]:
    #     deposit_amount = int(input("Enter the deposit amount: "))
    #     if deposit_amount > 0:
    #         account = ATM(user_name, deposit_amount, .001 )
    #         user_account[account.name] = {"balance": account.balance, "interest": account.interest}


main()




        
