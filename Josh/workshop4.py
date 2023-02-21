# creat class bob with attributes of name, pin, password
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name): # name method
        self.name = new_name

    def change_pin(self, new_pin): # pin method
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password


# create a class BankUser, inherit the User class, attributes of name,pin, and password
class Bankuser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0      # BankUser own instance attribute (These attributes are not passed from arguments list)

# Task 4 Add BankUser class instance methods
# 3 methods for bank user - show_balance(), withdraw(), and deposit()

    def show_balance(self):
        print(self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

# user2 = Bankuser("Bob",1234,"password")
# print("Bob has an account balance of: ", user2.balance)
# user2.deposit(1000)
# print("Bob has an account balance of: ",user2.balance)
# user2.withdraw(500)
# print("Bob has an account balance of: ",user2.balance)

# Task 5 Transfer an request money              (Transfer money IF.....)
    def transfer_money(self, amount, recipient): 
        pin_input = input("Input Your Pin: ")
        print('pin is: ', type(self.pin),'user input:', type( pin_input))
        if self.pin == int(pin_input): # transfer money if correct pin given return boolean of True if not correct return false
            print('Correct Pin!')
            if self.balance >= amount: # if person asked has amount or more
                self.balance -= amount # take money requested from balance
                recipient.balance += amount   #money moved to recipients balance
                return True
            return False

    def request_money(self, amount, recipient): # transfer money to user requesting (Alice)
        if recipient.pin == int(input("Enter recipient's PIN: ")): # (Alice PIN)
            if recipient.transfer_money(amount, self):
                    return True
        return False

user1 = Bankuser("Alice", 5678, "password")
user2 = Bankuser("Bob", 1234, "password")

user2.deposit(5000)
print('balances, user1 then user2')
user1.show_balance()
user2.show_balance()
testAmount = user1.balance
user2.transfer_money(500, user1)
print('balances, user1 then user2')
user1.show_balance()
user2.show_balance()
if user1.balance > testAmount:
  user2.request_money(500, user1)
print('balances, user1 then user2')
user1.show_balance()
user2.show_balance()


