
print("---------- WELCOME TO THE BANK ----------")
print("Card entered please wait.......")

while True:
    password = input("please Enter your password: ")
    if password.isdigit():
        password = str(password)

        if len(password) == 4:

            print("Login Successfully!")
            break

        else:
            print("Password is incorrect!")
    else:
        print("Password is incorrect!")

class Bank:

    def __init__(self , balance = 100):
        self.balance = balance


    def deposit(self):
        while True:
            deposit = input("please enter your deposit amount: ")
            if deposit.isdigit():
                deposit = int(deposit)

                self.balance += deposit
                print("Money deposited successfully!")
                print(self.balance)
                break

            else:
                print("Please enter a valid deposit amount!")


    def withdraw(self):

        while True:
            withdraw = input("please enter your withdraw amount: ")
            if withdraw.isdigit():
                withdraw = int(withdraw)

                self.balance -= withdraw
                print("Money withdrew successfully!")
                print(self.balance)
                break


            else:
                print("Please enter a valid withdraw amount!")


    def transfer(self):

        while True:
            account_pass = input("please enter account number you want to transfer: ")
            if account_pass.isdigit():
                account_pass = int(account_pass)

                digit_count = len(str(account_pass))
                if digit_count == 16:

                    transfer = input("How much money would you like to transfer?: ")
                    if transfer.isdigit():
                        transfer = int(transfer)

                        if self.balance > transfer:

                            self.balance -= transfer
                            print("Money transferred successfully!")
                            print(self.balance)
                            break

                        else:
                            print("Balance is not enough!")

                    else:
                        print("Incorrect input!")

                else:
                    print("Please enter a valid account number!")

            else:
                print("Please enter a valid account number!")





    def show_balance(self):
        print(f"your balance is: {self.balance}")

bank = Bank()


while True:
    print("---------- Operators ----------")
    print("1. Deposit Bank")
    print("2. Withdraw Bank")
    print("3. Transfer Bank")
    print("4. Show Balance")
    print("5. Exit")

    choice = input("please enter your choice: ")
    if choice.isdigit():
        choice = int(choice)

        match choice:
            case 1:
                bank.deposit()
            case 2:
                bank.withdraw()
            case 3:
                bank.transfer()
            case 4:
                bank.show_balance()
            case 5:
                print("Goodbye!")
                break
            case _:
                print("Please enter a valid choice!")








