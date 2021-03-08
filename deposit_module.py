def depositfunction(account_balance, deposit_amount, loan):
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

    return account_balance, loan, deposit_amount

