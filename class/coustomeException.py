# class AgeInvalidException(Exception):
#     pass

# def ageCheck(age):
#     if age <18:
#         raise AgeInvalidException("invalid age")
#     else:
#         print("valid age")

# try:
#     ageCheck(17)
# except Exception as e :
#     print(e)





import random

# Input from user
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

# Validation
if len(first_name) < 2 or len(last_name) < 2:
    print("Please enter at least 2 characters in both names.")
else:
    part1 = first_name[:2]
    part2 = last_name[:2]

    random_number = random.randint(1000, 9999)

    password = part1 + part2 + str(random_number)

    print("Generated Password:", password)




# class InsufficintAmountException(Exception):
#     def __init__(self, msg):
#         super().__init__(msg)

# class bank :
#     balance = 0

#     def check_balance(self):
#         print("current balance is :",self.balance)
    
#     def deposite(self,amt):
#         self.balance+=amt

#     def withdrow(self,amt):
#         if amt > self.balance:
#             raise InsufficintAmountException(f"you need more {amt-self.balance} in your account to withrow")
#         else:
#             self.balance-=amt
# b = bank()
# b.check_balance()
# b.deposite(80000)
# b.check_balance()
# try :
#     b.withdrow(200000)
# except Exception as e:
#     print(e)
# b.check_balance()











# class InvalidStringException(Exception):
#     def __init__(self, msg):
#         super().__init__(msg)

# def alphabet(str):
#     if str.isalpha():
#         print("valid")
#     else:
#         raise InvalidStringException("invalid")

# try:
#     alphabet("abca123")
# except Exception as e:
#     print(e)  