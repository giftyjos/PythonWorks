
# Bank[ACC No,balance,ac_type,customer_name]  [initialize,deposit(amount),withdraw(amount),get_balance()]




class Bank:

    acc_no:int

    balance:int

    acc_type:str

    customer_name=str

    def __init__(self,acc_no,acc_type,customer_name,balance):   #__init__means construtor for python  self intance of init
    

       self.acc_no=acc_no

       self.acc_type=acc_type

       self.customer_name=customer_name

       self.balance=balance

    def deposit(self,amount):

        self.balance+=amount

        print(f"your account{self,acc_no} has been credit with amount{amount} avl bal{self,balance}") #f means variable kodkan vendi

    def withdraw(self,amount):
        if self.balance<amount:
            self.balance-=amount
            print(f"your account{self,acc_no} has been debited with amount{amount} avl bal{self,balance}")
        else:

            print("insufficient balance")

    def get_balance(self):

        print("your aval bal",self.balance)


        # nxt object creation


customer_instance=Bank(10000,2500,"savings","assed")

customer_instance1.withdraw(5000)