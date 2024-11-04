import csv

class BankAccount:

    def __init__(self, account_id, account_name, balance):
        self.account_id = account_id
        self.account_name = account_name
        self.balance = float(balance)

    def __repr__(self):
        return f"{self.account_id}, {self.account_name}, {self.balance}"

class Bank:
    
    def __init__(self, filename='accounts.csv'):
        self.filename = filename
        self.accounts = self.load_accounts()

    def load_accounts(self):
        accounts = {}
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    account = BankAccount(row['account_id'], row['account_name'], row['balance'])
                    accounts[account.account_id] = account
        except FileNotFoundError:
            print("\nNo accounts file found. Starting with an empty account list.")
        return accounts

    def save_accounts(self):
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ['account_id', 'account_name', 'balance']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for account in self.accounts.values():
                writer.writerow({
                    'account_id': account.account_id,
                    'account_name': account.account_name,
                    'balance': account.balance
                })

    def add_account(self, account_id, account_name, balance):
        if account_id in self.accounts:
            print(f"\nAccount ID {account_id} already exists.")
        else:
            account = BankAccount(account_id, account_name, balance)
            self.accounts[account_id] = account
            print(f"\nAccount {account_name} added successfully.")

    def deposit(self, account_id, amount):
        self.accounts[account_id].balance += amount
        print(f"\n{amount} has been added to account: {account_id}, your total balance is now {self.accounts[account_id].balance}")
        self.save_accounts()

        
    def withdraw(self, account_id, amount):
        self.accounts[account_id].balance -= amount
        print(f"\n{amount} has been removed from account: {account_id}, your total balance is now {self.accounts[account_id].balance}") 
        self.save_accounts()

        
    def remove_account(self, account_id):
        if account_id in self.accounts:
            del self.accounts[account_id]
            print(f"\nAccount ID {account_id} removed successfully.")
        else:
            print(f"\nAccount ID {account_id} not found.")

    def display_accounts(self, account_id=None):
        if account_id == "admin":
            for account in self.accounts.values():
                print(account)
        elif account_id in self.accounts:
            print(self.accounts[account_id])
        else:
            print("Account ID not found.")

def main():
    bank = Bank()

    while True:
        print("\n1. Add Account\n2. Remove Account\n3. Deposit\n4. Withdraw\n5. Display Accounts\n6. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            account_id = input("Enter account ID: ")
            if account_id in bank.accounts:
                print(f"\n An account with this ID number already exist. Please choose a different ID number.")
            else:
                account_name = input("Enter account name: ")
                balance = float(input("Enter initial balance: "))
                bank.add_account(account_id, account_name, balance)

        elif choice == '2':
            account_id = input("Enter account ID to remove: ")
            bank.remove_account(account_id)

        elif choice == '3':
            account_id = input('Enter account ID to deposit money to: ')
            
            if account_id not in bank.accounts:
                print("\nThere is not an account with this ID number.")
                continue  

            try:
                amount = float(input("Enter the amount you want to deposit: "))
                bank.deposit(account_id, amount)
            except ValueError:
                print('Please enter a numeric value only.')

        elif choice == '4':
            account_id = input('Enter account ID to deposit money to: ')
            
            if account_id not in bank.accounts:
                print("\nThere is not an account with this ID number.")
                continue  

            try:
                amount = float(input("Enter the amount you want to withdraw: "))
                bank.withdraw(account_id, amount)
            except ValueError:
                print('Please enter a numeric value only.')

        elif choice == '5':
            account_id = input('\nEnter your ID credentials: ')
            bank.display_accounts(account_id)
                                  
        elif choice == '6':
            bank.save_accounts()
            print("Accounts saved. Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
