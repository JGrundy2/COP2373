# Creates the BankAcct class.
class BankAcct:
    # Initializes the account with the owner's name, account number, balance,
    # and interest rate.
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # A method to change the account's current interest rate.
    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    # A method to add money to the account if the deposit amount is greater
    # than zero.
    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.amount += deposit_amount
            return True
        else:
            return False

    # A method to subtract money from the account if there is enough money
    # available.
    def withdraw(self, withdraw_amount):
        if withdraw_amount > 0 and withdraw_amount <= self.amount:
            self.amount -= withdraw_amount
            return True
        else:
            return False

    # A method to return the current amount of money in the account.
    def get_balance(self):
        return self.amount

    # A method to calculate interest earned based on the balance and the number of
    # days.
    def calculate_interest(self, days):
        interest = self.amount * (self.interest_rate / 100) * (days / 365)
        return interest

    # Displays the account owner's information, balance, and annual interest.
    def __str__(self):
        interest = self.calculate_interest(365)

        return (f'Account Owner: {self.name}\n Account Number: {self.account_number}\n '
                f'Account Balance: ${self.amount:.2f}\n Interest Rate: '
                f'{self.interest_rate:.2f}%\n Annual Interest: ${interest:.2f}')

# Creates a test function to check that each BankAcct method works correctly.
def test_bank_account():
    # Creates a new account with the starting balance and interest rate.
    account = BankAcct('Jaclyn Grundy', 123456, 67.67,
                       5.0)

    # Displays the account information before any transactions.
    print('Initial Account Information')
    print(account)
    print()

    # Deposits $500 and displays the updated account balance.
    print('Deposit Test')
    account.deposit(500.00)
    print(f'Balance after deposit: ${account.get_balance():.2f}')
    print()

    # Withdraws $200 and displays the remaining account balance.
    print('Withdrawal Test')
    account.withdraw(200.00)
    print(f'Balance after withdrawal: ${account.get_balance():.2f}')
    print()

    # Changes the interest rate from 5% to 6% and displays the new interest
    # rate.
    print('Interest Rate Adjustment Test')
    account.adjust_interest_rate(6.0)
    print(f'New interest rate: {account.interest_rate:.2f}%')
    print()

    # Calculates and displays the interest earned over 90 days.
    print('Interest Calculation Test')
    interest = account.calculate_interest(90)
    print(f'Interest earned in 90 days: ${interest:.2f}')
    print()

    # Displays the final account information after all transactions.
    print('Final Account Information')
    print(account)

test_bank_account()