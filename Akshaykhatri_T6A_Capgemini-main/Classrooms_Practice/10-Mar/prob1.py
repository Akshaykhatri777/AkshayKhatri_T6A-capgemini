class bank:
    b_name = "JECRC Bank"
    balance = 0
    ifsc = "JEC0101234"

    def __init__(self,name,age,nominee):
        self.name = name
        self.age = age
        self.nominee = nominee
        pass

    def deposit(self,depAmt):
        print("Enter Amount to Deposit:",depAmt)
        self.balance+=depAmt
        print("Updated Bal of User",self.name,':',self.balance)

    def withdrawl(self,WithdAmt):
        print("Enter Amount to Withdrawl:",WithdAmt)
        self.balance-=WithdAmt
        print("Updated Bal of User",self.name,':',self.balance)

    def showBal(self):
        print("Available Amt of User",self.name,':',self.balance)

user1 = bank("Akshay",21,"St")
user2 = bank("Om",22,"Bs")
user1.deposit(1000)
user2.deposit(5000)
user2.withdrawl(3000)
user1.showBal()
user2.showBal()
