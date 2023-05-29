class User:
    def __init__(self, first_name,last_name,balance): 
        self.first_name = first_name 
        self.last_name = last_name
        self.balance = balance
        

    def make_deposit(self,amount):
        self.balance += amount 
        return self

    def make_withdrawal(self,amount):
        self.balance -= amount
        return self


    def display_user_balance(self):
        print(f'User: {self.first_name} {self.last_name}, Balance: ${self.balance}')
        return self


    def transfer_money(self,other_user,amount):
        self.balance -= amount
        other_user.balance += amount
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