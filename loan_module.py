def loanfunction(account_balance, loan, deposit_amount):
    from bankingsystem.deposit_module import depositfunction
    if loan == 0:
        loan = int(input("How much do you need? "))
        if input(f"Are you sure you want to borrow {loan}sh ") == 'y':
            account_balance += loan
            print(f"You have received a loan of {loan}.Your account balance is sh{account_balance} ")

            return account_balance

        else:
            loan -= loan
            print("process succesfullly terminated")
            print(loan)

        return account_balance
    else:
        print(f"You have an already existing loan of {loan} ")
        if input("Do you want to finish off your loan ") == 'y':
            depositfunction(account_balance, deposit_amount ,loan)
        else:
            print("Pay your loan first to get another!")


    return account_balance

