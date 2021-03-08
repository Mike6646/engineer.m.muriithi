def withdrawfun(withdraw_amount, account_balance, loan):
    from loan_module import loanfunction
    if withdraw_amount > account_balance:
        print(f"your account balance is {account_balance}sh")
        if input("Do you need a loan ") == 'y':
            loanfunction(account_balance, loan)

    elif withdraw_amount <= account_balance:
        account_balance -= withdraw_amount
        print(f"You have received sh{withdraw_amount} your account balance is {account_balance}")