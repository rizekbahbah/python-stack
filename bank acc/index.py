class bankAccount:		
    def __init__(self, balance, int_rate):
        self.int_rate=int_rate
        self.account_balance = balance
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self
    def make_withdrawl(self,amount):
        self.account_balance -= amount
        return self
    def display_balance(self):
        print( "Balance: $", self.account_balance)
        return self
    def yield_interest(self,intrstRate):
            self.account_balance=self.account_balance*(intrstRate+1)
            return self


