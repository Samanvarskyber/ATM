from bank import Bank
import random

print('Welcome to Happy Bank')
print('Create your account')
name = str(input('Please enter your name :\t'))

account_number = random.randint(100, 1000000000)
print('Congratulations you successfully created your bank account')

bank = Bank(name, account_number)

while True:
    tran = str(input('Do you want to do any transaction?(y/n)\t')).lower()
    if tran == 'y':
        bank.transaction()
    elif tran == 'n':
        print('Thank you and bye.')
        break
    else:
        print('Error : Enter y or n')
