from bankingsystem.withdraw_module import withdrawfun
from bankingsystem.deposit_module import depositfunction
from bankingsystem.loan_module import loanfunction
from bankingsystem.customer import Customer
from passwordcracker import passwordCracker
import random
import time
import webbrowser

customer221 = Customer('Ryan','6646',500,0,0,0,3,'')

account_balance = customer221.account_balance
chances = customer221.chances
password = customer221.password
password_attempt = customer221.password_attempt
withdraw_amount = customer221.withdraw_amount
deposit_amount = customer221.deposit_amount
loan = customer221.loan
passwordCracker(password)

print("Welcome to the iron bank of bravos\n")

while password_attempt!=password and chances!=0:
    password_attempt= input("Enter your password:) ")


    if password_attempt!=password:
        chances-=1
        if chances == 2:
            print("2 chances left😥")
        elif chances == 1:
            print("Last chance🤨")
        elif chances == 0:

            print("Account has been locked please contact our service to get your account unlocked (0708521986)")

    elif password==password_attempt:
        print('Checking accont.')
        time.sleep(1)
        print('Checking accont...')
        time.sleep(1)
        print('Checking accont......')
        time.sleep(1)

        print("**************Succesfull logged in!******************** ")

        while True:
            print("""
 Press 1 to Withdraw
 Press 2 to Deposit
 Press 3 for a Loan
 Press 4 to check account balance
 press 9 to change your password
 Press 0 to quit
            """)
            try:
                try:
                    user_input=0
                    user_input=int(input(":> "))
                except(ValueError):
                    print("Invalid input!")

                if user_input==1:
                    withdraw_amount = int(input("how much do you need? "))
                    if withdraw_amount > customer221.account_balance:
                        print(f"your account balance is {account_balance}sh")
                        if input("Do you need a loan ") == 'y':
                            loanfunction(account_balance, loan, deposit_amount)

                    elif withdraw_amount <= account_balance:
                        account_balance -= withdraw_amount
                        print(f"You have received sh{withdraw_amount} your account balance is {account_balance}")

                elif user_input==2:
                    deposit_amount=int(input("Enter the amount you want to deposit: "))
                    if loan > 0:
                        if deposit_amount > loan:
                            deposit_amount -= loan
                            account_balance += deposit_amount
                            print(f"sh {loan} has been deducted to pay of your loan.")
                            print(f"Your balance is{account_balance}sh")
                        elif deposit_amount < loan:
                            loan -= deposit_amount
                            print(f"sh{deposit_amount} has been deducted to pay of your loan.")
                            print(f"You still have {loan} left to pay from your loan.")
                    else:
                        account_balance += deposit_amount
                        print(f"Succesfully deposited {deposit_amount}")
                        print(f"Your account balance is {account_balance}sh")

                elif user_input==3:
                    if loan == 0:
                        loan = int(input("How much do you need? "))
                        if input(f"Are you sure you want to borrow {loan}sh ") == 'y':
                            account_balance += loan
                            print(f"You have received a loan of {loan}.Your account balance is sh{account_balance} ")
                            interest = loan+(loan*0.05)
                            loan+=interest
                        else:
                            loan -= loan
                            print("process succesfullly terminated")
                            print(loan)

                    else:
                        print(f"You have an already existing loan of {loan} ")
                        if input("Do you want to finish off your loan ") == 'y':
                            depositfunction(account_balance, deposit_amount, loan)
                        else:
                            print("Pay your loan first to get another!")


                elif user_input==4:
                    print(f"your account balance is {account_balance} ")
                    if loan>0:
                        print(f"with a loan of {loan}")

                elif user_input==9:
                    if input("type in your previous password: ")==password:
                        password=input("Type in your new password: ")
                        if len(password)<5:
                            print("Password is too weak")
                        elif password == int:
                            print("you should use a mixture of numeric and alphabets for a stronger password")
                        elif len(password)>6 and password!=int:
                            print("Your password is OK!")

                        print("password changed sucessfully. ")
                    else:
                        print("Incorrect password!")

                elif user_input==0:
                    print("Goodbye!")
                    break
                else:
                    webbrowser.open('How to use mikes bank system ')
                    print("Incorrect input!")
            except(ValueError):
                print("Invalid input! ")

