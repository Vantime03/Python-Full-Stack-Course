'''
Lab 25: ATM
Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
calc_interest() returns the amount of interest calculated on the account
'''
trasaction_list = []

class ATM:
    def __init__(self, name, balance, interest):
        self.name = name
        self.balance = balance
        self.interest = interest
    
    def check_balance(self):
        return self.balance
       
    def deposit(self):
        deposit_amount = int(input("how much would you like to deposit?\n"))
        self.balance = self.balance + deposit_amount
        return self.balance
    
    def check_withdrawal(self):
        withdraw_amount = int(input("how much would you like to withdraw?\n"))
        if self.balance >= withdraw_amount:
            self.withdraw(withdraw_amount)
            return withdraw_amount
        else: 
            print(f"Insufficient Fund! Your existing balance is {self.balance}")
            return 0

    def withdraw(self, withdraw_amount):
        self.balance = self.balance - withdraw_amount
        return self.balance

    def calc_interest(self):
        return self.balance * self.interest

def get_name():
    print("Welcome to ATM Demo!\n")
    user_name = input("What is the name for the ATM account?")
    return user_name

def user_action(p1):
    inquery_again = "yes"
    inquery = (input("what would you like to do (deposit, withdraw, check balance, history, or exit)?\n")).lower()
    
    while inquery_again in ["yes", "y"]:        
        if inquery == "deposit":
            deposit_amount = p1.deposit()
            trasaction_list.append(f'{p1.name} deposited {deposit_amount}.')
        
        elif inquery == "withdraw":
            withdraw_amount = p1.check_withdrawal()
            if withdraw_amount == 0:
                trasaction_list.append(f'{p1.name} withdrew {withdraw_amount}. This can be due to insufficient fund!')
            else:
                trasaction_list.append(f'{p1.name} withdrew {withdraw_amount}.')
        
        elif inquery == "check balance":
            balance = p1.check_balance()
            print(f"The current balance is ${balance}.\n")
            trasaction_list.append(f'{p1.name} checked balance.')

        elif inquery == "history":
            trasaction_list.append(f'{p1.name} checked history.')
            print_transaction()
        
        elif inquery == "exit":
            exit()

        else:
            print("That is an invalid entry! Please try again!\n")

        inquery = (input("what would you like to do next (deposit, withdraw, check balance, history, or exit)?\n")).lower()
          
def print_transaction():
    for n in trasaction_list:
        print(n)

def main():
    p1 = ATM('', 0, .001)
    user_name = get_name()
    p1.name = user_name
    print(f"Hi {p1.name}, your account is created. Your current balance is ${p1.balance} with the interest rate of {p1.interest * 100}%\n")
    trasaction_list.append(f'An account called {p1.name} was created.')
    user_action(p1)
     
main()




        
