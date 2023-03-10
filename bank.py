import sys


class Bank:

    def __init__(self, name, account_number, balance=0):
        # Here we initialize our variables
        self.balance = balance
        self.name = name
        self.account_number = account_number

    def account_detail(self):
        print('----------------ACCOUNT DETAILS----------------\n')
        print(f'Account Holder : {self.name} ')
        print(f'Account Number : {self.account_number}')
        print(f'Available Balance : {self.balance}\n')

    def deposit(self, amount):
        self.balance += amount
        print(f'Balance your account is {self.balance}.\n')

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'your balance is {self.balance} .')
            print(f'your balance is less than the amount your asking.\n')

        else:
            self.balance -= amount
            print(f" {amount} withdraw successful  :)  ")
            print(f'current amount balance {self.balance}\n')

    def check_balance(self):
        print(f'Available balance :  {self.balance}\n')

    def transaction(self):
        print('----------------TRANSACTION-------------------\n')
        print('''                   -Menu-
              1.Account Detail
              2.Check Balance 
              3.Deposit
              4.Withdraw
              5.Receipt & Exit'''
              )
        print()
        while True:
            try:
                option = int(input('Enter one to five :\t'))

            except Exception as e:
                print(f'Error : Invalid option try any number between one to  five :  {e}')
            else:
                if option == 1:
                    self.account_detail()

                elif option == 2:
                    self.check_balance()

                elif option == 3:
                    # User input for amount to be deposited (val)
                    val = int(input('how much do you want to deposit :\t'))
                    self.deposit(val)

                elif option == 4:
                    # User input for amount to be withdrawn (val)
                    val = int(input('how much do you want to withdraw:\t'))
                    self.withdraw(val)

                elif option == 5:
                    print(f'''
                    --------------RECEIPT---------------
                    Account holder : {self.name}
                    Account Number : {self.account_number}
                    Available Balance : {self.balance}
                    Thank you and have a good day.
                    ''')
                    sys.exit()
