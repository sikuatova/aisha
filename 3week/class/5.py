     
class Account:
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
        
    def __str__(self):
        return('Account owner: {} \nAccount balance {}'.format(self.owner, self.balance))
        
    def deposit(self, deposit_amt):
        
        self.balance = self.balance + deposit_amt
        print('You have been credited with {} and your current balance is {}'.format(deposit_amt, self.balance))
        
    def withdraw(self, withdraw_amt):
         
            if withdraw_amt > self.balance:
                print('Funds Unavailable, You have only {} in your account'.format(self.balance))
            else:
                self.balance = self.balance - withdraw_amt
                print('Withdrawal Accepted and your current balance is {}'.format(self.balance))
                
                
print(Account("aisha",10000))
        
    
