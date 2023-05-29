class bankAccount:		
    def __init__(self, balance, int_rate):
        self.int_rate=int_rate
        self.account_balance = balance
    def make_deposit(self, amount):	
        self.account_balance += amount

    def make_withdrawl(self,amount):
        self.account_balance -= amount
        return self
    def display_balance(self):
        print( "Balance: $", self.account_balance)
    def yield_interest(self,intr_Rate):
            self.account_balance=self.account_balance*(intr_Rate+1)
            return self



class User:		
    def __init__(self, name, email,balance,int_rate):
        self.name = name
        self.email = email
        self.account =  bankAccount(balance,int_rate)  



rizeek = User("Rezeek","text@gmail.com",0,0.05)
# print(rizeek.email)
acccount1 = bankAccount(2000,0.05)
acccount1.make_deposit(2000)
# print(acccount1.account_balance)
rizeek.account.make_deposit(50).display_balance()

