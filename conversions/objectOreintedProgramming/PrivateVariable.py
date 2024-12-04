class BankAccount:
    mpin: int
    account_type: str

    def __init__(self, customer_name, mpin, account_type, balance):
        self.customer_name = customer_name
        self.__mpin = mpin
        self._account_type = account_type
        self.balance = balance

    def __str__(self):
        return self.customer_name

    def get_balance(self):
        return self.balance

# Create an instance of BankAccount
bank_account_instance = BankAccount("hari", 2345, "savings", 5000)

# Use the instance
print(bank_account_instance)
print(bank_account_instance.get_balance())


# objectOrientedProgramming
   #class
   #object
   #constructor __init__
   #__str__
   #self
   #super()
   #inheritance(signal,multiple,multipler)
   #polymorphism(method_overloading,method_overridding)
   #abstration(ABC,abstraction)
   #__private_variable
   #Encapsulation
# python core and advanced=>exam

# aug_12
# sept_12
# oct_12
# nov 2.5 months


# collections list,dictionary
# oops class,object,inheritance,method_overriding

# threading>project


# FrontEnd>creativity
# backend->logic
# django=>python