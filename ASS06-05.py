"""
Q.5. Write a Python program for the following: 
 Define a class accountHolder consisting of attributes accNo, accName, accEmail. 
It consists a method dispDetails to display the details in appropriate format. 
 Inherit two classes viz. depositAccount (accountBalance) and loanAccount 
(loanAmount, EMI, loanBalance). The depositAccount contains methods 
debitAmt(amt)-which debits amt amount from the accountBalance, creditAmt(amt)
which credits the amt amount to the accountBalance and dispTrans()-which 
displays the whole transaction in appropriate format showing initial balance, 
debit/credit amount and final amount.
"""

class accountHolder:
    def __init__(self, accNo, accName, accEmail):
        self.accNo = accNo
        self.accName = accName
        self.accEmail = accEmail

    def dispDetails(self):
        """
        Displays account holder details.
        """
        print("Account Details:")
        print(f"Account Number: {self.accNo}")
        print(f"Account Name  : {self.accName}")
        print(f"Account Email : {self.accEmail}")
        print("-" * 40)


class depositAccount(accountHolder):
    def __init__(self, accNo, accName, accEmail, accountBalance):
        super().__init__(accNo, accName, accEmail)
        self.accountBalance = accountBalance
        # Transactions will be stored as a list of tuples:
        # (initial_balance, transaction_description, final_balance)
        self.transactions = []

    def creditAmt(self, amt):
        """
        Credits the given amount to the accountBalance and records the transaction.
        """
        initial_balance = self.accountBalance
        self.accountBalance += amt
        final_balance = self.accountBalance
        self.transactions.append((initial_balance, f"Credit: {amt}", final_balance))
        print(f"Credited {amt}. Balance updated from {initial_balance} to {final_balance}.")

    def debitAmt(self, amt):
        """
        Debits the given amount from the accountBalance if sufficient funds exist,
        and records the transaction.
        """
        initial_balance = self.accountBalance
        if amt > self.accountBalance:
            print("Insufficient funds to debit the amount.")
            return
        self.accountBalance -= amt
        final_balance = self.accountBalance
        self.transactions.append((initial_balance, f"Debit: {amt}", final_balance))
        print(f"Debited {amt}. Balance updated from {initial_balance} to {final_balance}.")

    def dispTrans(self):
        """
        Displays all recorded transactions in a formatted manner.
        """
        print("Transaction History:")
        for idx, trans in enumerate(self.transactions, start=1):
            init_bal, trans_desc, final_bal = trans
            print(f"Transaction {idx}: Initial Balance = {init_bal}, {trans_desc}, Final Balance = {final_bal}")
        print("-" * 40)


class loanAccount(accountHolder):
    def __init__(self, accNo, accName, accEmail, loanAmount, EMI):
        super().__init__(accNo, accName, accEmail)
        self.loanAmount = loanAmount
        self.EMI = EMI
        self.loanBalance = loanAmount  # Initially, the outstanding loan is the full loan amount

    def dispLoanDetails(self):
        """
        Displays the loan details.
        """
        print("Loan Account Details:")
        print(f"Loan Amount     : {self.loanAmount}")
        print(f"EMI             : {self.EMI}")
        print(f"Remaining Balance: {self.loanBalance}")
        print("-" * 40)


# Main program to demonstrate functionality
if __name__ == "__main__":
    # Create a deposit account holder
    depositHolder = depositAccount("A101", "Alice Smith", "alice@example.com", 1000)
    depositHolder.dispDetails()
    
    # Perform some transactions on the deposit account
    depositHolder.creditAmt(500)   # Credit an amount
    depositHolder.debitAmt(300)    # Debit an amount
    depositHolder.debitAmt(1500)   # Attempt a debit that exceeds the balance
    depositHolder.creditAmt(200)   # Another credit
    depositHolder.dispTrans()      # Display transaction history

    # Create a loan account holder
    loanHolder = loanAccount("B202", "Bob Johnson", "bob@example.com", 5000, 250)
    loanHolder.dispDetails()
    loanHolder.dispLoanDetails()
