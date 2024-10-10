#this is lizzy saldanas what is happening assignment.

class BankAccount: #the bank account that is where everything below is happening (the bank account the user creates and edits)
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount): #This function is how the depositing system works, adding the amount you want to put into your account with the number in your account.
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount): #This function is how the withdrawing system works, minusing the amount you want to take out from your amount you have in the bank account
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self): #Returns what your balance is.
        return self.balance

def create_account():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: ")) #This part will ask for a float, so even if you enter in 5 it will make it 5.00
    return BankAccount(account_number, initial_balance)  #This checks for the things you have previously answered or created, such as the account number and how much is your inital balance. From there if you withdraw or deposit it will either add or divide.

def main():
    accounts = {}
    while True: #while the main function is running and true, it'll go through all the code below.
        print("\n1. Create Account")    #These lines from 31-35 are all the first prints that appear on screen. Each choice has a corressponding number and therefore a different function.
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':  #Choice number 1, which is creating an account.
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        
        elif choice in ['2', '3', '4']: #runs if your choice is 2,3, or 4
            account_number = input("Enter account number: ")
            if account_number in accounts:
                account = accounts[account_number]
                if choice == '2': #If you pick number 2, then you picked the option to deposit
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")
                    else:
                        print("Invalid deposit amount.")
                elif choice == '3': #if you pick number 3 you are now choosing the option to withdraw money
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount):# 
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                else:
                    print(f"Current balance: ${account.get_balance():.2f}")
            else:
                print("Account not found.") #If you havent created an account yet then this will appear if you try to withdraw or deposit money from an invalid account.
        
        elif choice == '5': #if you pick 5 as your answer then this code will run. It is the end.
            print("Thank you for using our banking system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.") #If the user does not input an integer from 1-5 it will print

if __name__ == "__main__": #After the function runs, this last piece of code will run and call back the function so it asks for the choices again.
    main()