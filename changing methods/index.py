class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):	
        self.account_balance -= amount	
        return self


    def display_user_balance(self):	
        print(f"User:{self.name}, Balance: {self.account_balance}")
        return self

    def transfer_money(self, amount, user_recipient): 
        self.account_balance -= amount
        user_recipient.account_balance += amount
        return self



Rizek = User("hakeem","ahmad",10000)   
fouad = User("samir","Amir",10000)
Mina = User("dina", "Amir", 10000)


Rizek.make_deposit(500).make_deposit(1000).make_deposit(2500).make_withdrawal(1000).display_user_balance()


fouad.make_deposit(1000).make_deposit(1000).make_withdrawal(500).make_withdrawal(250).display_user_balance()

Mina.make_deposit(1000).make_withdrawal(500).make_withdrawal(500).make_withdrawal(500).display_user_balance()

Rizek.transfer_money(Mina,1000)
Rizek.display_user_balance()
Mina.display_user_balance()