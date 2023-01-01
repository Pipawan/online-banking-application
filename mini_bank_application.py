class costumer:
    '''Heartly welcome in our bank...'''
    Bank_name = "Python Bank limited"

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        self.balance = self.balance+amount
        print("After deposite :", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insuffecrnt fund!!!, please deposite amount first.")
        else:
            self.balance = self.balance-amount
            print("After withdraw :", self.balance)


print("Welcome to our ", costumer.Bank_name)
name = input("Enter your name: ")
c = costumer(name)

while True:
    print("d-Deposite\n w-withdraw \n e-exit")

    option = input("Please chose your option...")
    if option.lower() == "d":

        amount = float(input("Enter amount to deposite."))
        c.deposite(amount)
    elif option.lower() == "w":
        amount = float(input("Enter amount to deposite."))
        c.withdraw(amount)
    elif option.lower() == "e":
        print("Thanks for Banking")

        break
    else:
        print('plseae chose valid option.')
